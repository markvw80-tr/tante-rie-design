# Stijlgids Tante Rie

Vastgelegd op 28-10-2026 uit `~/TanteRie-Theme-Editor` (config/settings_data.json, assets/tr-design.css, assets/tr-base.css, sections/tr-collection-*.liquid) en gemeten op https://tanterie.nl/collections/zwarte-thee. Het oude subdomein webshop.tanterie.nl is een 301-restant; het merk draait op tanterie.nl. Bronnen: [T] thema-instelling, [C] CSS-bestand, [L] live gemeten.

## 1. Kleuren

Basispalet [C tr-design.css]

| Token | Waarde | Gebruik |
|---|---|---|
| --cream | #faf8f2 | pagina- en sectieachtergrond (schema 1) |
| --cream-dark | #e0dbd0 | randen, scheidingslijnen |
| --page-bg | #eef1ea | zachte vlakken, kaartachtergrond (schema 3) |
| --white | #ffffff | kaarten, tekst op donker |
| --text | #2a2a1a | lopende tekst (live 81 procent dekking) |
| --text-muted | #6b6152 | bijschriften, broodkruimels |
| --brown-dark | #1c1c14 | koppen, knoppen in eigen secties |
| --brown | #6b4c30 | hover, accent |
| --brown-light | #c8c4b8 | randen, deler |
| --green | #3b5240 | primaire knop in themaschema's |
| --green-dark | #263830 | donker groen |
| --green-mid / --green-light / --green-pale | #5c7a67 / #4f6e58 / #e9efea | ondersteunend groen |

Kleurschema's [T]: schema 1 (achtergrond #faf8f2), 2 (#f0ece2), 3 (#eef1ea) zijn de merkschema's met knop #3b5240, hover #2e4033, tekst wit. Schema 4 (#e1edf5), 5 (#333333) en 6 (transparant, wit) wijken af van het merk, zie open punten.

Collectie-accenten [C in sections/tr-collection-*.liquid]: elke theecollectie heeft een eigen accentset. Zwarte thee: #3D1E0A, #8B4513, #C4762A, #F5EBD8, #2A1005. Groene thee: #122A1C, #1E3D2A, #3A7D52, #6B8F3E, #E6F2EB. Kruidenthee: #27134A, #3D1F5C, #7D3C98, #9B59B6, #F4ECF7. Joeff: #7A331C, #B5502E, #D97B54, #FBEEE6. Bunzlau: #1A3D5C, #2C5F8A, #4A7BAF, #E8F1F8. Vruchtenthee heeft #853718 en #E67E22. Rooibos, witte thee, Rice en Blond niet apart uitgelezen.

## 2. Typografie

Lettertypen [T, L bevestigd]: koppen Playfair Display 400 (live ook 700 geladen); lopende tekst Inter 400/500/700; subkoppen Inter 500. DM Sans 300 tot 600 wordt extra geladen via Google Fonts [theme.liquid] en gebruikt in alle eigen tr-secties, knoppen en menu. Lora is verwijderd in Sprint 3 (commit 4700743).

Schaal [T, desktop]: H1 56 px, H2 48, H3 32, H4 24 (Playfair); H5 14, H6 12 (Inter). Regelhoogte kop display-tight, letterspatiëring heading-tight; lopende tekst 16 px, body-loose. Live gemeten op een collectiepagina: H1 48 px, H2 35,2 px, letterspatiëring -1,44 en -1,06 px, dus de eigen secties gebruiken clamp-waarden en niet de themaschaal. Knoptekst: DM Sans 500, 13 px (compact 11 px), hoofdletters, letterspatiëring .07em [C tr-base.css].

## 3. Spacing en layout

Geen spacingschaal als tokens. Vaste waarden [C]: paginamarge 5vw (mobiel 4vw), maximale inhoudsbreedte 1440 px, sectie-opvulling 48 tot 64 px boven en onder, kaartraster 4 kolommen met 20 px tussenruimte (3 kolommen onder 1100 px, 2 kolommen met 12 px onder 700 px, 1 kolom onder 400 px), kaartopvulling 16 px 16 px 18 px. Breekpunten die terugkomen: 1100, 900, 768, 700, 600 en 400 px. Themainstelling paginabreedte: smal [T].

## 4. Knoppen en vormen

Eigen secties [C tr-base.css]: primair zwarte achtergrond #1c1c14, witte tekst, hoek 50 px (pil), hover #6b4c30 met 1 px omhoog; secundair transparant, rand 1,5 px #c8c4b8, pil, hover #e0dbd0; winkelwagenknop op kaarten 11 px, opvulling 8 px 16 px. In collecties wisselt de hoofdknopkleur naar het collectie-accent (bijvoorbeeld #8B4513 bij zwarte thee). Themaknoppen [T]: primair groen #3b5240, geen rand, hoek 14 px; secundair rand 1 px groen, hoek 14 px. Overige hoeken [T]: invoervelden 4 px, kaarten 4 px, labels 4 px, popover 14 px, variantknoppen 14 px, swatches 34 px rond. Eigen secties: filterpillen 50 px, dropdown 14 px, informatiekaarten 20 px, verhaalafbeelding 20 px.

## 5. Beeldgebruik

Productkaart: vierkant (1:1), `object-fit: contain` met 16 px opvulling op #eef1ea, zodat de productfoto nooit wordt bijgesneden. Hero van collecties: foto met 20 procent dekking over een donkere accentkleur, tekst in wit. Verhaalblok: 4:3, hoek 20 px, `object-fit: cover`. Productfoto's komen uit Shopify (cdn.shopify.com/s/files); een product komt pas online met minstens één foto (afspraak PIM). Alt-teksten zijn van PIM. Logo: Logo-Tante-Rie-blok-1.png, 100 px hoog desktop, 28 px mobiel [T]. Favicon favicon3.png.

## 6. Interactie

Kaart-hover lift [T], paginaovergang aan [T], `prefers-reduced-motion` wordt gehonoreerd in de collectiesecties. Reviews via Judge.me, gestijld in tr-design.css (pilknoppen #1c1c14, sterren #6b4c30).

## Besluiten van Mark (28-10-2026, in de chat)

1. Lettertype lopende tekst en knoppen: DM Sans overal (Inter vervalt). Sluit open punt 1.
2. Knopstijl: zwart (#1c1c14) in pilvorm (50 px) is leidend, ook voor Afrekenen in de winkelwagen; hover #6b4c30. Sluit open punt 2.
3. Collectiekleuren per categorie blijven; Design bewaakt contrast (minimaal AA) en maakt alleen tekst donkerder die onder AA valt. Sluit open punt 3.
4. Donkergrijze footer (kleurschema 5) blijft zoals hij is. Sluit open punt 4; kleurschema's 4 en 6 blijven onbeoordeeld.

## Open punten (niet geraden, besluit Mark nodig)

1. (BESLOTEN 28-10: DM Sans) Twee schreefloze lettertypen live: Inter (themainstelling, body) en DM Sans (alle tr-secties, knoppen, menu). Welk lettertype is de merkstandaard voor lopende tekst en knoppen?
2. (BESLOTEN 28-10: zwart pil) Twee knopstijlen naast elkaar: thema groen #3b5240 met hoek 14 px, tr-secties zwart #1c1c14 met pil 50 px, collecties met accentkleur. Welke is leidend voor nieuwe knoppen?
3. (BESLOTEN 28-10: houden) Zijn de collectie-accentkleuren (bruin, groen, paars, blauw, klei, oranje) bewust per categorie, of moet elke collectie één merkaccent krijgen?
4. (BESLOTEN 28-10 voor schema 5: footer blijft; schema 4 en 6 nog open) Thema-kleurschema's 4 (blauw), 5 (donkergrijs) en 6 (wit transparant) passen niet bij het palet. In gebruik of restant? Niet nagelopen waar ze worden toegepast.
5. Geen spacingschaal en geen vaste breekpuntenset. Wil Mark een schaal vastleggen (bijvoorbeeld 8/16/24/48/64) of de huidige waarden bevriezen?
6. Paginabreedte: thema "smal" tegenover 1440 px in tr-design.css. Welke geldt op welke pagina?
7. Koptypografie: themaschaal (H1 56) wijkt af van live (H1 48, clamp). Is de clamp de bedoelde schaal?
8. Fotografierichtlijn ontbreekt (stijl, achtergrond, sfeerbeeld versus productfreisteller). Alleen de technische verhoudingen zijn vastgelegd.
9. Header, footer, menu en productpagina zijn nog niet uitgelezen voor kleur en maat; alleen collectiepagina's en globale instellingen. Aanvullen bij de eerste opdracht die daaraan raakt.
10. Bronstatus: `~/TanteRie-Theme-Editor` heeft 40 niet-gecommitte wijzigingen ten opzichte van de laatste commit en kan afwijken van het live thema 204204900616. Voor waarden altijd het live thema vers ophalen (zie CLAUDE.md).
