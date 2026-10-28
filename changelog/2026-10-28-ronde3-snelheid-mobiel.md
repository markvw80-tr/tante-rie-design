# 2026-10-28, ronde 3 designreview: snelheid en toegankelijkheid mobiel

Bouwt voort op ronde 1 en 2 (zelfde werkkopie plus onderstaande wijzigingen). Bron: `opdrachten/2026-10-28-review-webshop.md`, punt 6.

## Uitgangssituatie (live, 28-10, PageSpeed mobiel, lab)
Prestatiescore home 64, zwarte thee 75 (tweede ronde 63 tot 64), Earl Grey 60. LCP 8,4 s, 5,1 tot 10,5 s en 11,1 s. De lab-uitkomsten schommelen van run tot run met meer dan 3 s. **Echte gebruikers (CrUX via PageSpeed, origin-niveau): LCP 1,4 s, FCP 1,2 s, CLS 0, TTFB 0,43 s, alles "snel".** Het probleem is dus vooral zichtbaar op trage telefoons en in de lab-test, niet bij de gemiddelde bezoeker. Paginagewicht 2,9 tot 3,5 MB. In een echte browser (zonder throttling) staat de LCP-afbeelding al op 0,3 tot 0,6 s en laadt eager.

## Wat is gewijzigd
1. **Collectiehero** (9 `tr-collection-*`-secties met `collection.image`): `srcset` 600/900/1200/1600 met `sizes="100vw"` en `fetchpriority="high"`. Voorheen altijd 1600 px breed (op 390 px nu 900 px) en zonder prioriteit; PageSpeed meldde "LCP request discovery" op de collectiepagina.
2. **Productkaarten in collecties** (9 secties zonder `srcset`): `srcset` 250/375/500 met `sizes` zoals Bunzlau al had; voorheen altijd 500 px, ook voor kaarten van 183 px breed.
3. **Footer-contrast** (`assets/tr-base.css`): copyrighttekst en links van #787a6d (3,83 : 1 op #eef1ea, onder AA) naar #5f6155 (5,53 : 1 op #eef1ea, 5,94 : 1 op #faf8f2). Gevonden door PageSpeed op alle drie de pagina's. Alleen de footer-regel; kleurkeuzes elders niet geraakt (zie stijlgids open punt 3).

## Gemeten (gedrosseld Slow 4G, CPU 4x, mobiel 390 px, 4 runs per kant, zwarte thee)
LCP live mediaan 6,2 s (5,9 tot 6,3), dev-thema 5,3 s (5,3 tot 5,4): **ongeveer 0,9 s sneller (-15 procent)**, in elke run. FCP en gewicht zijn niet te vergelijken: de Shopify-previewbalk voegt ongeveer 15 verzoeken en scripts toe (FCP dev 2,7 s tegen live 2,0 s). PageSpeed-lab op de preview (2 runs): LCP 7,3 en 8,2 s tegen 10,3 en 10,5 s live, maar de preview scoort lager op interactiviteit door de previewbalk; als score niet bruikbaar. Bij een telefoonscherm met 2x pixeldichtheid levert `srcset` op de kaartjes weinig bytes op (de browser kiest dan toch 500 px); op 1x en 1,75x schermen (lab, oudere telefoons) wel.

## Niet gedaan, wel gevonden (volgende stappen)
- **Judge.me** laadt op de productpagina ongeveer 25 CSS-bestanden (ReviewWidget, Stack, Button, enz.) plus script; dat is een app en niet in het thema aan te passen zonder het widget later te laden (risico voor reviewweergave en SEO-markup van SEO). Eerst met SEO afstemmen.
- **Rendergeblokkeerde CSS:** `compiled_assets/styles.css` (43 KB), `base.css` (15 KB) en vijf losse tr-bestanden; samenvoegen of kritieke CSS inlijnen is een grotere wijziging.
- **Paginagewicht 2,9 tot 3,5 MB:** kaartfoto's zijn webp van ongeveer 100 KB op 500 px; kleinere varianten of lagere kwaliteit vergen nieuwe afbeeldingen (PIM) of een app.
- **Winkelfoto-banner op home:** LCP-afbeelding home 230 KB; niet bijgesneden naar mobiel formaat.
- "Console error" in PageSpeed komt van Shopify (Monorail weigert de Lighthouse-useragent) en is geen sitefout.
- Contrast van "OVER ZWARTE THEE" (amber op bruin): hangt aan de collectiekleuren (stijlgids open punt 3), niet aangepast.

## Ontwikkelthema en rollback
Thema-id 204337217800, naam `design-ronde3-snelheid-mobiel-2026-10-28` (unpublished). Dit thema bevat ronde 1, 2 en 3. Omdat de winkel maximaal 20 thema's toestaat is de inhoud van het oude testthema (alleen die ene H2 boven het raster van Zwarte Thee) overschreven; die test staat beschreven in `changelog/2026-10-28-zwarte-thee-h2.md` en is niet nodig. Nog geen ruimte voor een volgend ontwikkelthema zonder een ander thema te verwijderen. Preview: https://0qkm31-r6.myshopify.com/?preview_theme_id=204337217800
Live thema 204204900616 ongewijzigd. Rollback: niet publiceren; of live terugzetten op 204204900616; voor `tr-base.css` en `theme.liquid` de backups van ronde 1.

## Review
Perf- en toegankelijkheidscontrole door de Design Lead zelf (Reviewer-agent niet ingezet), met PageSpeed, een gedrosselde browsermeting en contrastberekening. Niet getest: schermlezers, toetsenbordbediening, de nieuwe `srcset` op alle collecties visueel (alleen zwarte thee en Bunzlau bekeken in eerdere rondes; geen layoutwijziging verwacht).
