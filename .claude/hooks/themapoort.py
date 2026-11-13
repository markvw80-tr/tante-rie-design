#!/usr/bin/env python3
"""PreToolUse-hook Design: nooit rechtstreeks naar het live thema.

`shopify theme push` mag alleen met een expliciet --theme/-t (ontwikkelthema)
en zonder --live/-l/--allow-live. `theme publish`, `theme delete` en
`theme share` worden geblokkeerd. Het live thema wijzigt Mark na goedkeuring.
"""
import json
import re
import shlex
import sys

data = json.load(sys.stdin)
if data.get("tool_name") != "Bash":
    sys.exit(0)
cmd = data.get("tool_input", {}).get("command", "")
if not re.search(r"\bshopify\s+theme\s+(push|publish|delete|share)\b", cmd):
    sys.exit(0)


def weiger(reden):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reden + " Werk alleen op een ontwikkelthema en laat Mark het live thema wijzigen na goedkeuring."}}))
    sys.exit(0)


m = re.search(r"\bshopify\s+theme\s+(push|publish|delete|share)\b", cmd)
actie = m.group(1)
if actie != "push":
    weiger(f"Geblokkeerd: shopify theme {actie}.")
try:
    tokens = shlex.split(cmd[m.start():])
except ValueError:
    weiger("Geblokkeerd: opdracht niet te ontleden.")
vlaggen = [t for t in tokens if t.startswith("-")]
if any(v in ("--live", "-l", "--allow-live") or v.startswith("--allow-live") for v in vlaggen):
    weiger("Geblokkeerd: push naar het live thema.")
if not any(v in ("--theme", "-t") or v.startswith("--theme=") or (v.startswith("-t") and len(v) > 2 and not v.startswith("--"))
           for v in vlaggen):
    weiger("Geblokkeerd: shopify theme push zonder --theme <ontwikkelthema-id>.")
