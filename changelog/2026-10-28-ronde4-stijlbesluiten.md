# 2026-10-28, ronde 4: besluiten van Mark in het thema (lettertype en knoppen), winkelwagen

Bron: antwoorden van Mark in de chat (28-10-2026), vastgelegd in `stijlgids/tante-rie/stijlgids.md` onder "Besluiten van Mark". Bouwt voort op ronde 1, 2 en 3.

**Wat:**
1. `config/settings_data.json`: lopende tekst en subkoppen van Inter naar DM Sans (`type_body_font: dm_sans_n4`, `type_subheading_font: dm_sans_n5`). Koppen blijven Playfair Display.
2. Zelfde bestand: themaknoppen volgen de zwarte pilstijl: kleurschema 1, 2 en 3 hebben primaire knop #1c1c14 met hover #6b4c30 (was groen #3b5240 en #2e4033), secundaire knoppen tekst en rand #1c1c14, hoek 50 px voor primair en secundair (was 14 px). Kleurschema 4, 5 en 6 niet aangeraakt (footer blijft donkergrijs, besluit Mark).
3. `layout/theme.liquid`: zwevende winkelwagenknop ook verborgen op de winkelwagenpagina (nutteloos naast de header-wagen).
Collectiekleuren: geen wijziging (besluit: houden; alleen onder AA aanpassen, geen overtreding gevonden buiten "OVER ZWARTE THEE", zie ronde 3).

**Ontwikkelthema:** id 204338659592, naam `design-ronde4-stijlbesluiten-2026-10-28` (bevat ronde 1 t/m 4; het eerdere inhoud van dit thema, ronde 1, zit erin opgenomen). Preview: https://0qkm31-r6.myshopify.com/?preview_theme_id=204338659592. Thema 204337217800 (ronde 3) en 204342395144 (ronde 2) blijven zoals ze zijn. Live 204204900616 ongewijzigd.
**Gemeten, 390 en 360 px:** hoofdtekst is DM Sans op alle gemeten pagina's (home, 4 collecties, product, theewinkel); geen horizontale scroll en geen element buiten zijn kaart; "Afrekenen" is nu zwart (rgb 28,28,20), hoek 50 px, DM Sans. Toevoegen aan winkelwagen op de productpagina getest en werkt (wagen telt 1, "Toegevoegd" op de knop, daarna winkelwagenpagina). Screenshots: `screenshots/2026-10-28-cart/m-cart-ronde4.png`, `m-product-ronde4.png`.
**Niet getest:** desktop, tablet, productpagina's van Bunzlau, Rice, Blond en Joeff en de cart-drawer na deze instellingswijziging; checkout is Shopify-gehost en volgt de themakleuren niet. Letterbreedte van DM Sans is iets groter dan Inter: let bij publicatie op lange productnamen in smalle kaarten.
**Rollback:** `changelog/2026-10-28-ronde4.backup-settings_data.json` terugzetten en `theme.liquid` uit de ronde 1 backup; of niet publiceren.

## Aanvulling: drawer na toevoegen, snelbetaalknoppen, controle voor publicatie

**Wat:** `config/settings_data.json`: `auto_open_cart_drawer: true` (de winkelwagen-drawer opent na toevoegen, het script `tr-cart.js` ondersteunde dit al). `assets/tr-base.css`: snelbetaalknoppen (Shop Pay, PayPal, Google Pay) 44 px hoog met 8 px tussenruimte; in de drawer staan ze naast elkaar onder "Afrekenen", op de winkelwagenpagina onder elkaar maar lager. Backup van de instellingen vóór deze stap: `changelog/2026-10-28-ronde4b.backup-settings_data.json`.
**Getest op 204338659592:** toevoegen via de hoofdknop opent de drawer (item, totaal, "Afrekenen" zwart, snelknoppen eronder); snelknoppen 44 px.
**Controle voor publicatie, mobiel 390 px en desktop 1440 px:** productpagina's van Earl Grey (redesign), Bunzlau boeren mok, Rice L, Blond mok, Joeff basishouder en kruidenthee Sterke Vrouw: hoofdknop met label zichtbaar (48 tot 52 px hoog, 14 px tekst), vaste balk 45 px waar aanwezig, DM Sans, geen horizontale scroll. Home, zwarte thee en winkelwagen: geen horizontale scroll, DM Sans. Desktop zwarte thee visueel bekeken: onveranderd van opzet.
**Nog niet gedaan / opgemerkt:** de broodkruimel op de Rice-productpagina staat links tegen de rand zonder opvulling en met krappe scheidingstekens (ook op het live thema zo; mijn aanraakdoelregel maakt het 4 px krapper). Niet aangepast. Servies- en accessoire-productsjablonen niet aangeraakt of getest (geen producten in de collectie gevonden voor de test). Reviewer niet ingezet.
