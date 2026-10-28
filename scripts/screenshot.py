"""Screenshots voor en na op desktop (1440 px) en mobiel (390 px).

Gebruik:
  python3 scripts/screenshot.py <url> <map> <voor|na> [--selector CSS]

Schrijft <map>/<voor|na>-desktop.png en <voor|na>-mobiel.png. Met --selector
scrolt de pagina naar dat element (100 px marge) zodat het gewijzigde deel
in beeld staat. Alleen lezen; er wordt niets op de site gewijzigd.
"""
import argparse
from pathlib import Path
from playwright.sync_api import sync_playwright

FORMATEN = {"desktop": {"width": 1440, "height": 900}, "mobiel": {"width": 390, "height": 844}}

p = argparse.ArgumentParser()
p.add_argument("url")
p.add_argument("map")
p.add_argument("fase", choices=("voor", "na"))
p.add_argument("--selector")
a = p.parse_args()
Path(a.map).mkdir(parents=True, exist_ok=True)

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    for naam, vp in FORMATEN.items():
        ctx = browser.new_context(viewport=vp, device_scale_factor=1, is_mobile=(naam == "mobiel"))
        page = ctx.new_page()
        page.goto(a.url, wait_until="networkidle", timeout=60000)
        page.add_style_tag(content="*{animation:none!important;transition:none!important}")
        # privacyvriendelijkste keuze in de lege testbrowser: niet-essentiële cookies afwijzen
        page.evaluate("()=>{const b=document.getElementById('shopify-pc__banner__btn-decline'); if(b) b.click();}")
        page.wait_for_timeout(500)
        if a.selector:
            page.evaluate("s=>{const e=document.querySelector(s); if(e){e.scrollIntoView({block:'start'}); window.scrollBy(0,-100);}}", a.selector)
        page.wait_for_timeout(1200)
        pad = Path(a.map) / f"{a.fase}-{naam}.png"
        page.screenshot(path=str(pad))
        print(pad)
        ctx.close()
    browser.close()
