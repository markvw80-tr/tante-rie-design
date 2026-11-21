"""Drukwerk-HTML omzetten naar PDF (paginamaat uit @page) en een PNG-voorbeeld.

Gebruik:
  python3 scripts/drukwerk.py <bestand.html> [<bestand.html> ...]

Schrijft naast elk HTML-bestand <naam>.pdf en <naam>-voorbeeld.png (300 dpi,
inclusief afloop). Wacht tot de webfonts geladen zijn. Alleen lokaal.
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

MM_PER_INCH = 25.4
PX_PER_MM_CSS = 96 / MM_PER_INCH
PNG_DPI = 300


def render(page, html: Path) -> None:
    page.goto(html.resolve().as_uri(), wait_until="networkidle", timeout=60000)
    page.evaluate("document.fonts.ready")
    if not page.evaluate("document.fonts.check('600 12px \"DM Sans\"')"):
        raise SystemExit(f"DM Sans niet geladen voor {html.name}")
    page.pdf(path=str(html.with_suffix(".pdf")), prefer_css_page_size=True,
             print_background=True, margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
    page.screenshot(path=str(html.with_name(html.stem + "-voorbeeld.png")), full_page=False)
    print(html.with_suffix(".pdf"), html.with_name(html.stem + "-voorbeeld.png"))


def main(paden: list[str]) -> None:
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for pad in map(Path, paden):
            # paginamaat in mm uit body-afmetingen halen via een eerste lading
            probe = browser.new_page()
            probe.goto(pad.resolve().as_uri(), wait_until="networkidle")
            w, h = probe.evaluate("[document.body.offsetWidth, document.body.offsetHeight]")
            probe.close()
            schaal = PNG_DPI / 96
            ctx = browser.new_context(viewport={"width": w, "height": h}, device_scale_factor=schaal)
            render(ctx.new_page(), pad)
            ctx.close()
        browser.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    main(sys.argv[1:])
