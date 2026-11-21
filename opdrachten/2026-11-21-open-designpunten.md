# Open designpunten (verzameld 21-11-2026)

**Bron:** directie-opdracht 15-11 (`2026-11-15-125443-directie-opdracht-mark-open-designpunten-oppakken.md`) en Mark 18-11 (`2026-11-18-232825-mark-verder-met-de-punten-van-design.md`), beide nu in `verwerkt/`. Opgesteld bij het opschonen van de inbox op verzoek van Mark (21-11); in deze ronde is niets gebouwd.
**Uitvoering:** Design Lead plant, `theme-developer` bouwt op een ontwikkelthema. Geen specialist nodig zolang het om deze bugfixes gaat; de Reviewer volgt pas als Mark een fix live wil.
**Regels:** alleen ontwikkelthema, screenshots voor en na (1440 en 390 px, voor de tablet ook 768 en 1024 px), changelog met rollback, Mark publiceert zelf. Geen koppen, markup of links wijzigen.

## Stand per punt uit de opdracht van 15-11

| # | Punt | Stand 21-11 |
|---|---|---|
| 1 | SEO-berichten mobiel nagelezen live thema en Judge.me | Afgehandeld, beide in `verwerkt/` (28-10). |
| 2 | Knop "Kies decor" rechts afgesneden op Bunzlau | **Open op tabletbreedte.** De fix van 28-10 (`changelog/2026-10-28-ronde2-collectie-product-mobiel.md`) laat de kaartvoet alleen tot 700 px afbreken; tussen ongeveer 701 en 1024 px kan prijs plus knop nog steeds te breed zijn voor de kaart. Ook "Bestel nu" op Blond nalopen. |
| 3 | USP-balk glitcht bij scrollen op de collectiepagina | **Open.** De fix van 28-10 (`changelog/2026-10-28-ronde1-knoppen-mobiel.md`) ging live met 204338659592, maar de melding van 15-11 komt daarna. Eerst opnieuw meten op het huidige live thema (205262029064, controleren met `shopify theme list`), welke collectie en welke breedte, dan pas bouwen. |
| 4 | Desktopmenu klapt niet goed open | Afgehandeld: akkoord Mark 16-11 (besluit 483019d07a), menufix staat op live 205262029064 (gecontroleerd 17-11). |
| 5a | Designreview incl. mobiel afmaken | **Deels open.** Punt 1 tot 6 van `opdrachten/2026-10-28-review-webshop.md` zijn in de rondes 1 tot 4 opgepakt. Niet afgerond: punt 7 (hero homepage mobiel, knop "Ons verhaal") en punt 8 (kleine punten), plus het label "Op voorraad in 1 decor" dat op Bunzlau-kaarten over twee regels breekt. |
| 5b | Oude thema's opruimen | Lijst klaar in `opdrachten/2026-11-20-thema-opruimlijst.md`; wacht op akkoord van Mark per thema-id (komt als nieuw bericht). |
| 5c | Design-repo naar GitHub | Afgehandeld, main gelijk aan origin/main (21-11). |

## Ook lopend, buiten deze lijst

V134 eenheidsprijs losse thee: gebouwd op ontwikkelthema 205914898696 (`changelog/2026-11-20-eenheidsprijs-losse-thee.md`). Het tonen wacht op V137 (vinkje Eenheidsprijs tonen) bij Mark; daarna preview met screenshots naar Mark en Rich Results Test door SEO.

## Raakt de stijlgids

Punt 2 en 3 zijn bugfixes binnen de bestaande stijl. Punt 7 van de review (knop "Ons verhaal") en de knopkleur raken open punten van de stijlgids; daar kiest Mark, niet Design.

## Succescriterium

Op 768 en 1024 px staat op alle collectiekaarten geen element buiten zijn kaart; de USP-balk verspringt niet tijdens scrollen op de gemelde collectie, gemeten op 390, 768 en 1440 px; Mark krijgt een preview met screenshots en publiceert zelf.
