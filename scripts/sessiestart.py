"""Compacte sessiestart voor het Design-team.

Haalt tante-rie-hq op en toont alleen wat nodig is: nieuwe berichten voor
Design in de Markdown-mailbox van tante-rie-seo en de nieuwste statusblokken.

Gebruik: python3 scripts/sessiestart.py [aantal_statusblokken]
"""
import subprocess
import sys
from pathlib import Path

HQ = Path.home() / "tante-rie-hq"
SEO = Path.home() / "Tante Rie SEO"
BLOKKEN = int(sys.argv[1]) if len(sys.argv) > 1 else 3

pull = subprocess.run(["git", "-C", str(HQ), "pull", "-q"], capture_output=True, text=True)
print("hq pull:", "ok" if pull.returncode == 0 else pull.stderr.strip()[:200])

print("\nMailbox design:")
subprocess.run(["python3", str(SEO / "scripts/mailbox.py"), "lijst", "design"])

blokken, huidig = [], None
for regel in (HQ / "team/status.md").read_text().splitlines():
    if regel.startswith("## "):
        huidig = [regel]
        blokken.append(huidig)
    elif huidig is not None:
        huidig.append(regel)
print(f"\nStatus, nieuwste {BLOKKEN} van {len(blokken)} blokken:")
for blok in blokken[:BLOKKEN]:
    print("\n".join(r for r in blok if r.strip()))
