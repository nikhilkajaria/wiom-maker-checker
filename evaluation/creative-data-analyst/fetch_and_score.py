"""Creative Data Analyst — data engine.

Pulls the Wiom Growth Portal, builds clean creative pools, scores every
active creative on the 5-lens framework (see framework.md), and writes a
machine-readable data.json + human-readable tables.md into runs/.

The judgment half (quadrant narrative, divergence-pair reads, candidate
learnings) is done by the creative-data-analyst agent on top of this output.

Usage:
    python fetch_and_score.py                     # last 14 completed days
    python fetch_and_score.py --days 7
    python fetch_and_score.py --start 2026-06-01 --end 2026-06-30

Token: read at runtime from C:\\credentials\\.env — key GROWTH_DASHBOARD_TOKEN
(fallback WIOM_DASHBOARD_TOKEN, the name used in Kashish's setup doc).
Never hardcode, print, or commit the token.

Network note: some home routers (JioFiber) refuse DNS for *.up.railway.app.
If normal DNS fails we resolve via Google DNS (8.8.8.8) and pin the IP while
keeping SNI/Host as the real hostname.
"""
import argparse
import json
import os
import socket
import ssl
import subprocess
import sys
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone

HOST = "growth-portal.up.railway.app"
ENV_PATH = r"C:\credentials\.env"
HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- config
CONFIG = {
    # spend floor per geo per 14 days (INR); scaled linearly to window length.
    # Bharat CPMs are ~3x cheaper than Delhi, hence the lower floor.
    # Mumbai floor assumed = Delhi (metro CPMs); revisit when Mumbai goes live.
    "floor_per_14d": {"Delhi": 5000, "Mumbai": 5000, "Bharat": 1500},
    "floor_unknown_geo": 5000,
    "active_last_n_days": 3,      # active = any spend in the window's last N dates
    "low_n_installs": 50,         # below this, cost reads are direction-only
    "fatigue_cpi_ratio": 1.3,     # 2nd-half CPI > 1.3x 1st-half = fatigue flag
    "fatigue_min_installs": 20,   # per half, else trend not judged
    # campaign family tags, matched as whole '_'-separated tokens (uppercased)
    "known_families": [
        "BFC-VOLUME", "RETARGETING", "CREATIVE-TESTING", "ACC-LEARN",
        "AWARENESS", "SEARCH", "UAC", "DEMANDGEN",
    ],
    "geo_prefix": {"DEL": "Delhi", "BHARAT": "Bharat", "MUM": "Mumbai",
                   "MUMBAI": "Mumbai"},
}

# ---------------------------------------------------------------- network
def load_token():
    if not os.path.exists(ENV_PATH):
        sys.exit(f"credentials file not found: {ENV_PATH} — see README.md")
    token = None
    with open(ENV_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            for key in ("GROWTH_DASHBOARD_TOKEN", "WIOM_DASHBOARD_TOKEN"):
                if line.startswith(key + "="):
                    token = line.split("=", 1)[1].strip().strip('"').strip("'")
    if not token:
        sys.exit("GROWTH_DASHBOARD_TOKEN / WIOM_DASHBOARD_TOKEN not found in "
                 f"{ENV_PATH} — ask Kashish for the dashboard token")
    return token


def _pin_ip_if_dns_blocked():
    try:
        socket.getaddrinfo(HOST, 443)
        return
    except socket.gaierror:
        pass
    out = subprocess.run(["nslookup", HOST, "8.8.8.8"],
                         capture_output=True, text=True, timeout=30).stdout
    ips, seen = [], False
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("Name:"):
            seen = True
        elif seen and line.startswith(("Address:", "Addresses:")):
            ips.append(line.split(":", 1)[1].strip())
    if not ips:
        sys.exit(f"cannot resolve {HOST} (local DNS blocked, 8.8.8.8 failed)")
    ip = ips[0]
    orig = socket.getaddrinfo
    socket.getaddrinfo = (lambda host, *a, **k:
                          orig(ip if host == HOST else host, *a, **k))
    print(f"[net] local DNS blocked; pinned {HOST} -> {ip}")


def api_get(path, token):
    req = urllib.request.Request(f"https://{HOST}{path}",
                                 headers={"X-Dashboard-Token": token})
    with urllib.request.urlopen(req, timeout=300) as resp:
        return json.loads(resp.read().decode("utf-8"))


# ---------------------------------------------------------------- parsing
def campaign_family(campaign, questions):
    tokens = [t.upper() for t in (campaign or "").split("_")]
    for fam in CONFIG["known_families"]:
        if fam in tokens:
            return fam
    questions.add(f"Campaign '{campaign}' matches no known family tag "
                  f"{CONFIG['known_families']} — classify it (then add the "
                  f"tag to CONFIG['known_families']).")
    return "UNCLASSIFIED"


def adset_geo(ad_set, questions):
    prefix = (ad_set or "").split("_")[0].upper()
    geo = CONFIG["geo_prefix"].get(prefix)
    if geo is None:
        questions.add(f"Ad set '{ad_set}' has unknown geo prefix '{prefix}' — "
                      "which geography is this?")
        return "UNKNOWN"
    return geo


def actions_count(row, atype):
    for a in row.get("actions") or []:
        if a.get("action_type") == atype:
            return float(a.get("value") or 0)
    return 0.0


def video_metric(row, field):
    v = row.get(field)
    if not v:
        return 0.0
    if isinstance(v, list):
        return sum(float(x.get("value") or 0) for x in v)
    return float(v)


# ---------------------------------------------------------------- pipeline
def build(dates, records, master, questions):
    half = len(dates) // 2
    first_half, active_days = set(dates[:half]), set(dates[-CONFIG["active_last_n_days"]:])

    fmt_map = {}
    for r in master:
        if r.get("format") in ("Static", "Video") and r.get("creative"):
            fmt_map[r["creative"]] = r["format"]

    ads = defaultdict(lambda: defaultdict(float))
    meta = {}
    google_spend = 0.0
    for day in records:
        date = day.get("date") or ""
        for ms in day.get("meta_spend") or []:
            if ms.get("channel") == "GOOGLE":
                google_spend += float(ms.get("spend") or 0)
                continue
            if ms.get("channel") != "META":
                continue
            key = (ms.get("campaign_name"), ms.get("adset_name"), ms["ad_name"])
            a, h = ads[key], ("h1" if date in first_half else "h2")
            for src, dst in (("spend", "spend"), ("impressions", "impr"),
                             ("clicks", "clicks")):
                v = float(ms.get(src) or 0)
                a[dst] += v
                a[f"{dst}_{h}"] += v
            a["v3s"] += actions_count(ms, "video_view")
            a["thruplay"] += video_metric(ms, "video_thruplay_watched_actions")
            if float(ms.get("spend") or 0) > 0 and date in active_days:
                a["active"] = 1
            meta.setdefault(key, {})
        for at in day.get("attribution") or []:
            if not at.get("ad_name"):          # Google/UAC rows have no ad name
                continue
            key = (at.get("campaign"), at.get("ad_set"), at["ad_name"])
            if key in ads:
                h = "h1" if date in first_half else "h2"
                ads[key]["installs"] += float(at.get("app_installs") or 0)
                ads[key][f"installs_{h}"] += float(at.get("app_installs") or 0)

    rows = []
    for (campaign, ad_set, ad_name), a in ads.items():
        if a["spend"] <= 0:
            continue
        fmt = fmt_map.get(ad_name)
        if fmt is None:
            if a["thruplay"] > 0 or a["v3s"] > 0:
                fmt = "Video"
            elif a["impr"] > 1000:
                fmt = "Static"
            else:
                fmt = "Unknown"
                questions.add(f"Cannot determine format for '{ad_name}' "
                              "(no master-export entry, no video signals, "
                              "<1k impressions) — static or video?")
        r = {
            "family": campaign_family(campaign, questions),
            "geo": adset_geo(ad_set, questions),
            "format": fmt,
            "campaign": campaign, "ad_set": ad_set, "ad": ad_name,
            "concept": ad_name.split("_")[0],
            "spend": round(a["spend"]), "impr": int(a["impr"]),
            "clicks": int(a["clicks"]), "installs": int(a["installs"]),
            "active": bool(a.get("active")),
            "cpm": round(1000 * a["spend"] / a["impr"], 1) if a["impr"] else None,
            "ctr": round(100 * a["clicks"] / a["impr"], 3) if a["impr"] else None,
            "cvr": round(100 * a["installs"] / a["clicks"], 1) if a["clicks"] else None,
            "cpi": round(a["spend"] / a["installs"], 1) if a["installs"] else None,
            "hook": None, "hold": None, "tp_rate": None,
        }
        if fmt == "Video":
            if a["impr"]:
                r["hook"] = round(100 * a["v3s"] / a["impr"], 2)
                r["tp_rate"] = round(100 * a["thruplay"] / a["impr"], 2)
            if a["v3s"]:
                r["hold"] = round(100 * a["thruplay"] / a["v3s"], 1)
        for h in ("h1", "h2"):
            r[f"spend_{h}"] = round(a[f"spend_{h}"])
            r[f"ctr_{h}"] = (round(100 * a[f"clicks_{h}"] / a[f"impr_{h}"], 3)
                             if a[f"impr_{h}"] else None)
            r[f"cpi_{h}"] = (round(a[f"spend_{h}"] / a[f"installs_{h}"], 1)
                             if a[f"installs_{h}"] else None)
        r["fatigue_flag"] = bool(
            r["cpi_h1"] and r["cpi_h2"]
            and a["installs_h1"] >= CONFIG["fatigue_min_installs"]
            and a["installs_h2"] >= CONFIG["fatigue_min_installs"]
            and r["cpi_h2"] > CONFIG["fatigue_cpi_ratio"] * r["cpi_h1"])
        rows.append(r)
    return rows, google_spend


def rank(vals, reverse=True):
    """1 = best. None values rank last."""
    order = sorted(range(len(vals)),
                   key=lambda i: (vals[i] is None,
                                  -vals[i] if reverse and vals[i] is not None
                                  else (vals[i] if vals[i] is not None else 0)))
    out = [0] * len(vals)
    for pos, i in enumerate(order):
        out[i] = pos + 1
    return out


def score_pools(rows, window_days, questions):
    floor_scale = window_days / 14.0
    pools = defaultdict(list)
    excluded = {"below_floor": 0, "inactive": 0}
    for r in rows:
        floor = CONFIG["floor_per_14d"].get(r["geo"], CONFIG["floor_unknown_geo"])
        r["qualified"] = r["active"] and r["spend"] >= floor * floor_scale
        if not r["active"]:
            excluded["inactive"] += 1
        elif not r["qualified"]:
            excluded["below_floor"] += 1
        if r["format"] == "Unknown":
            continue
        pools[(r["family"], r["geo"], r["format"])].append(r)

    pool_out = []
    for (family, geo, fmt), members in sorted(pools.items()):
        q = [r for r in members if r["qualified"]]
        pool = {"family": family, "geo": geo, "format": fmt,
                "n_total": len(members), "n_qualified": len(q),
                "adsets": sorted({r["ad_set"] for r in q}),
                "creatives": [], "pairs": []}
        if len(pool["adsets"]) > 1:
            pool["caveat_mixed_adsets"] = (
                "Pool mixes more than one ad set — check targeting is "
                "comparable before trusting cross-ad-set gaps.")
        if len(q) >= 2:
            att_parts = (["hook", "hold", "ctr"] if fmt == "Video" else ["ctr"])
            part_ranks = [rank([r[p] for r in q]) for p in att_parts]
            att = [round(sum(pr[i] for pr in part_ranks) / len(part_ranks), 1)
                   for i in range(len(q))]
            att_rank = rank(att, reverse=False)
            conv_rank = rank([r["cvr"] for r in q])
            med = (len(q) + 1) / 2
            for i, r in enumerate(q):
                r["att_rank"], r["conv_rank"] = att_rank[i], conv_rank[i]
                hi_att, hi_conv = att_rank[i] <= med, conv_rank[i] <= med
                r["quadrant"] = ("all-rounder" if hi_att and hi_conv else
                                 "clickbait" if hi_att else
                                 "honest-but-invisible" if hi_conv else "weak")
                r["low_n"] = r["installs"] < CONFIG["low_n_installs"]
            best, score = None, 0
            for i in range(len(q)):        # i = better attention
                for j in range(len(q)):    # j = better conversion
                    s_att = att_rank[j] - att_rank[i]
                    s_conv = conv_rank[i] - conv_rank[j]
                    if s_att > 0 and s_conv > 0 and s_att * s_conv > score:
                        best, score = (i, j), s_att * s_conv
            if best:
                i, j = best
                pool["pairs"].append({
                    "attention_winner": q[i]["concept"],
                    "conversion_winner": q[j]["concept"],
                    "note": "biggest rank crossing in pool"})
        elif len(q) == 1:
            q[0].update(att_rank=1, conv_rank=1, quadrant="only-one-qualified",
                        low_n=q[0]["installs"] < CONFIG["low_n_installs"])
        pool["creatives"] = sorted(q, key=lambda r: r["cpi"] or 9e9)
        pool_out.append(pool)
    return pool_out, excluded


# ---------------------------------------------------------------- output
COLS = ["concept", "spend", "cpm", "ctr", "hook", "hold", "tp_rate", "cvr",
        "installs", "cpi", "quadrant"]


def to_markdown(pools, meta_info):
    lines = [f"# Creative pools — {meta_info['start']} → {meta_info['end']} "
             f"({meta_info['days']} days)", ""]
    for p in pools:
        if not p["creatives"]:
            continue
        lines.append(f"## {p['family']} · {p['geo']} · {p['format']} "
                     f"({p['n_qualified']}/{p['n_total']} qualified)")
        if p.get("caveat_mixed_adsets"):
            lines.append(f"> ⚠ {p['caveat_mixed_adsets']}")
        lines.append("")
        lines.append("| " + " | ".join(COLS) + " | trend |")
        lines.append("|" + "---|" * (len(COLS) + 1))
        for r in p["creatives"]:
            trend = "⚠fatigue" if r["fatigue_flag"] else ""
            cells = [str(r.get(c) if r.get(c) is not None else "-") for c in COLS]
            if r.get("low_n"):
                cells[-1] += " (low-n)"
            lines.append("| " + " | ".join(cells) + f" | {trend} |")
        for pair in p["pairs"]:
            lines.append(f"\n**Divergence pair:** {pair['attention_winner']} "
                         f"(attention) × {pair['conversion_winner']} (conversion)")
        lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=14)
    ap.add_argument("--start")
    ap.add_argument("--end")
    args = ap.parse_args()

    token = load_token()
    _pin_ip_if_dns_blocked()

    available = api_get("/api/raw/dates", token)["dates"]
    if args.start and args.end:
        dates = [d for d in available if args.start <= d <= args.end]
    else:
        dates = available[-args.days:]
    if not dates:
        sys.exit("no available dates in the requested window")
    start, end = dates[0], dates[-1]
    print(f"[window] {start} -> {end} ({len(dates)} completed days)")

    records = []
    for i in range(0, len(dates), 31):
        chunk = dates[i:i + 31]
        print(f"[fetch] raw days {chunk[0]} -> {chunk[-1]}")
        records += api_get(f"/api/raw/days?start={chunk[0]}&end={chunk[-1]}",
                           token)["records"]
    print("[fetch] master export (format map)")
    master = api_get(f"/api/master_export?start={start}&end={end}", token)

    questions = set()
    rows, google_spend = build(dates, records, master, questions)
    pools, excluded = score_pools(rows, len(dates), questions)

    meta_info = {"start": start, "end": end, "days": len(dates),
                 "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                 "google_spend_excluded_inr": round(google_spend),
                 "excluded": excluded, "config": CONFIG,
                 "questions_for_human": sorted(questions)}
    out_dir = os.path.join(HERE, "runs", f"{end}_{len(dates)}d")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "data.json"), "w", encoding="utf-8") as f:
        json.dump({"meta": meta_info, "pools": pools, "all_rows": rows}, f,
                  indent=1)
    with open(os.path.join(out_dir, "tables.md"), "w", encoding="utf-8") as f:
        f.write(to_markdown(pools, meta_info))
    print(f"[done] {out_dir}")
    print(f"  pools: {len(pools)} | rows: {len(rows)} | "
          f"google spend excluded: Rs {google_spend:,.0f}")
    if questions:
        print(f"  QUESTIONS FOR HUMAN ({len(questions)}):")
        for q in sorted(questions):
            print(f"   - {q}")


if __name__ == "__main__":
    main()
