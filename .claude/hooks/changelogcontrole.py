#!/usr/bin/env python3
"""Stop-hook Design: elke themawijziging krijgt een changelog (CLAUDE.md regel 2).

Is er in een werkkopie onder .theme-werkkopie een bestand gewijzigd na het
nieuwste bestand in changelog/ (en niet ouder dan 6 uur), dan houdt de hook de
sessie een keer open met de vraag om changelog/JJJJ-MM-DD-<onderwerp>.md te schrijven.
"""
import json
import os
import sys
import time
from pathlib import Path

data = json.load(sys.stdin)
if data.get("stop_hook_active"):
    sys.exit(0)
root = Path(os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd()))
werk = root / ".theme-werkkopie"
if not werk.is_dir():
    sys.exit(0)

grens = time.time() - 6 * 3600
nieuwste_werk, bestand = 0.0, None
for p in werk.rglob("*"):
    if p.is_file() and ".shopify" not in p.parts and p.suffix in {".liquid", ".json", ".css", ".js"}:
        m = p.stat().st_mtime
        if m > nieuwste_werk:
            nieuwste_werk, bestand = m, p
if nieuwste_werk < grens:
    sys.exit(0)

logs = [p.stat().st_mtime for p in (root / "changelog").glob("*.md")]
if logs and max(logs) >= nieuwste_werk:
    sys.exit(0)

print(json.dumps({"decision": "block", "reason":
      f"Themabestand {bestand.relative_to(root).as_posix()} is gewijzigd zonder bijgewerkte changelog. "
      "Schrijf changelog/JJJJ-MM-DD-<onderwerp>.md (wat, bestanden, ontwikkelthema-id, preview-URL, "
      "waarom, akkoord Mark, rollback-notitie) of meld waarom het niet nodig is."}))
