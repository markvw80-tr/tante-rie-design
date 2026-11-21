# Reviewkaartje kassa Borne (21-11-2026)

**Doel:** klanten in de winkel in Borne vragen om een Google-review, met een drukklaar kaartje in de huisstijl. Draagt bij aan het hoofddoel via lokale vindbaarheid in Google Maps (zie statusblok Klant 21-11).

**Opdrachtgever:** Mark, via het Huis. Tekst goedgekeurd door Mark. QR-code aangeleverd en ongewijzigd (`qr-review.svg`, link naar de Google-reviewpagina van Tante Rie).

**Pagina's / thema:** geen. Er gaat niets naar Shopify of het thema, dus geen ontwikkelthema, geen voor- en na-screenshots en geen SEO- of PIM-eisen nodig.

**Uitvoering:** Design Lead zelf (drukwerk in HTML, geen themacode). Geen specialist ingezet: merkcontrole doet de Design Lead, contrast en QR-leesbaarheid zijn hieronder gecontroleerd.

**Levering** in `opdrachten/2026-11-21-reviewkaartje/`:

| Formaat | Snijmaat | Met afloop | HTML | PDF | Voorbeeld |
|---|---|---|---|---|---|
| Visitekaartje (in de tas) | 85 x 55 mm | 91 x 61 mm | visitekaartje-85x55.html | visitekaartje-85x55.pdf | visitekaartje-85x55-voorbeeld.png |
| Toonbankkaartje (bij de kassa) | A6 staand, 105 x 148 mm | 111 x 154 mm | toonbankkaartje-a6.html | toonbankkaartje-a6.pdf | toonbankkaartje-a6-voorbeeld.png |

Opnieuw renderen: `python3 scripts/drukwerk.py <html> [...]` (PDF op @page-maat, PNG op 300 dpi, stopt als DM Sans niet laadt).

**Ontwerp:** DM Sans 400 en 600, achtergrond crème #faf8f2, kop #1c1c14, tekst #2a2a1a, scheidingslijn #c8c4b8. QR in #1c1c14 op een wit vlak. Veilige zone 4 mm (visitekaartje) en 6 mm (A6) binnen de snijlijn.

**Succescriterium en controle:**
- QR minstens 2 cm: visitekaartje 27 mm, A6 50 mm. Stilte rond de code ruim 4 modules (2 in de svg plus het witte vlak).
- Contrast QR #1c1c14 op wit ongeveer 17:1, tekst #2a2a1a op #faf8f2 ongeveer 14:1.
- Beide voorbeelden en de originele PNG decoderen naar dezelfde link (search.google.com/local/writereview?placeid=ChIJSV7D_q0PuEcRcNdTRtisMbw).
- Geen korting, beloning of winactie. Alleen de goedgekeurde tekst plus de naam Tante Rie.

**Opmerkingen en vragen voor Mark:**
1. Logo: het enige logo dat ik vond (Logo-Tante-Rie-blok-1.png op de site) is 150 x 98 px, te klein voor drukwerk. Daarom staat de naam als tekst in DM Sans. Is er een vectorlogo (svg, pdf of ai) en wil je dat erop?
2. Koppen zijn in DM Sans gezet zoals gevraagd. De stijlgids noemt Playfair Display voor koppen op de site; als je de kop liever in Playfair wilt, is dat één regel.
3. A6-PDF is 111,2 x 154,2 mm (Chromium rondt af op hele pixels). Het teveel van 0,2 mm valt in de egale afloop; meld het de drukker als die exact 111 x 154 mm eist.
4. Kaartjes zijn enkelzijdig. Papier en afwerking (bijvoorbeeld 350 g mat) kiest Mark met de drukker.
