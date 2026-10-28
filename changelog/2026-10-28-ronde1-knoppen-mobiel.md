# 2026-10-28, ronde 1 designreview: knoppen en aanraakdoelen op mobiel

**Wat (bronnen: `opdrachten/2026-10-28-review-webshop.md`, punt 1, 2 en 5):**
1. `assets/tr-base.css`: de mobiele regel die toevoegen-knoppen tot een cirkel zonder tekst maakt geldt nu alleen voor kaartknoppen. Hoofdknoppen (`*-btn-primary`) en de vaste balk (`*sticky-atc-btn`) houden hun tekst en breedte. Kaartcirkels van 40 naar 44 px.
2. `layout/theme.liquid`: de zwevende winkelwagenknop (FAB) is verborgen op pagina's met een vaste toevoegen-balk (`body:has([class*="sticky-atc"])`). Elders onveranderd.
3. `assets/tr-base.css`, nieuw mobiel blok (max 767 px): broodkruimel-links 44 px aanraakgebied (zonder layoutverschuiving), "alle theesoorten"-links, `.tr-card-btn` en filterpillen minimaal 44 px hoog, kleine labels (10 tot 11 px) naar 12 px.
Geen wijziging aan producttekst, SEO-markup, koppen, links of kleuren. Desktop ongewijzigd (alles zit in `max-width: 767px`, behalve de FAB-regel die al alleen mobiel bestond).

**Ontwikkelthema:** `design-ronde1-knoppen-mobiel-2026-10-28`, id 204338659592 (unpublished). Preview: https://0qkm31-r6.myshopify.com/?preview_theme_id=204338659592
**Live thema:** 204204900616, ongewijzigd (gecontroleerd). Het ontwikkelthema is gemaakt van een verse pull van het live thema, dus zonder de test-H2 van thema 204337217800.
**Gemeten, mobiel 390 px, voor naar na (product earl-grey):** hoofdknop 40x40 zonder tekst naar 358x52 met tekst; vaste balkknop 307x40 zonder tekst naar 307x45 "In winkelwagen"; FAB zichtbaar naar verborgen; broodkruimel 34x14 naar 43x47 aanraakgebied; kaartknop 141x32 naar 141x44; collectie: filterpil 35 naar 44 px, labels 10 naar 12 px.
**Screenshots:** `screenshots/2026-10-28-ronde1/` (voor en na, mobiel; lokaal). De preview-balk van Shopify bedekt onderaan de vaste balk; `na-product-sticky-mobiel.png` is zonder die balk gemaakt. Desktop-screenshots niet gemaakt omdat desktop niet verandert; niet visueel gecontroleerd.
**Akkoord Mark:** gegeven voor bouwen (28-10); publiceren nog niet.

## Rollback
Niets live gewijzigd. Na publicatie terugdraaien: live zetten van thema 204204900616, of `assets/tr-base.css` en `layout/theme.liquid` terugzetten met `changelog/2026-10-28-ronde1.backup-tr-base.css` en `changelog/2026-10-28-ronde1.backup-theme.liquid`.

## Review
Reviewer niet ingezet (team start met twee rollen). Basischecks door Design Lead: meting hierboven; contrast ongewijzigd; geen nieuwe scripts of afbeeldingen. Niet getest: werkelijk toevoegen aan winkelwagen via de nieuwe knop op de ontwikkelthema (zou de winkelwagen vullen); knop gebruikt hetzelfde `data-tr-atc`-attribuut als voorheen, alleen de weergave is veranderd. Dat testen vóór publicatie, bij voorkeur door Mark of de Reviewer.
