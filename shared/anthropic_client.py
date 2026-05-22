"""Anthropic SDK client wrapper. Loads API key from C:\\credentials\\.env."""
from __future__ import annotations

import os
from pathlib import Path

from anthropic import Anthropic
from dotenv import load_dotenv

CREDENTIALS_PATH = r"C:\credentials\.env"
MODEL_SONNET = "claude-sonnet-4-6"
MODEL_HAIKU = "claude-haiku-4-5"


def _load_key() -> str:
    # override=True is required because the Claude Code shell injects ANTHROPIC_API_KEY=""
    # (empty string), which dotenv's default behaviour will not replace.
    load_dotenv(CREDENTIALS_PATH, override=True)
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        raise RuntimeError(
            f"ANTHROPIC_API_KEY not found in {CREDENTIALS_PATH}. "
            "Add `ANTHROPIC_API_KEY=...` to that file."
        )
    return key


def get_client() -> Anthropic:
    return Anthropic(api_key=_load_key())


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]
