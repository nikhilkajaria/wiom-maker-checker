# -*- coding: utf-8 -*-
"""Download the Google Sheet as xlsx and run the registry export in one step."""
import sys, requests, tempfile, subprocess
from pathlib import Path
import gspread

SHEET_ID = '1ay8EBJ3fRjpx0U80ErEqMwJGXlY0ynh_FzTfGcTGXaA'
REPO_ROOT = Path(__file__).resolve().parent.parent

gc = gspread.oauth(
    credentials_filename=r'C:\Users\nikhi\.config\gspread\credentials.json',
    authorized_user_filename=r'C:\Users\nikhi\.config\gspread\authorized_user.json'
)

token = gc.http_client.auth.token
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=xlsx'
r = requests.get(url, headers={'Authorization': f'Bearer {token}'})
r.raise_for_status()

xlsx_path = REPO_ROOT / 'experiments' / '_latest_sheet_export.xlsx'
xlsx_path.write_bytes(r.content)
print(f'Downloaded: {len(r.content):,} bytes -> {xlsx_path}')

result = subprocess.run(
    [sys.executable, str(REPO_ROOT / 'scripts' / 'export_registry_to_json.py'), str(xlsx_path)],
    capture_output=True, text=True
)
print(result.stdout)
if result.returncode != 0:
    print('STDERR:', result.stderr)
    sys.exit(result.returncode)
