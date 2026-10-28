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

## Aanvulling 28-10-2026: USP-balk op collectiepagina's tijdens het scrollen

**Probleem (gemeten op het live thema, zwarte thee):** een script in `layout/theme.liquid` zette bij `scrollY > 80` de klasse `tr-usp-compact` op elke USP-balk. Daardoor kromp de balk terwijl hij nog midden op de pagina stond (mobiel 221 naar 104 px, desktop 82 naar 35 px) en sprong alles eronder 117 px (mobiel) of 47 px (desktop) omhoog; scrollen rond 80 px liet de balk heen en weer klappen. Daarnaast waren USP-balk én filterbalk vast (mobiel ongeveer 245 van 844 px bedekt), en bleef de compacte USP-balk op mobiel alsnog drie regels hoog. Ik kon het scherm van Mark niet zien (geen collectietab open); dit is wat de meting toont.
**Wat:** `assets/tr-base.css`: compact-blok vervangen door `[class*="-usp-bar"] { position: static !important; box-shadow: none !important }`. `layout/theme.liquid`: compact-script vervangen door een script dat de vaste balk (`*-sticky-bar`) zo ver omhoog laat vastklikken als de USP-balk hoog is. Resultaat: USP-balk scrolt gewoon weg, alleen de filterbalk blijft vast onder de header, niets verandert van hoogte tijdens het scrollen.
**Gemeten op ontwikkelthema 204338659592, 390 en 1440 px:** zwarte thee en Bunzlau: paginahoogte constant tijdens scrollen (alleen de bestaande header-inklapping van 32 px), filterbalk blijft op 77 px (mobiel) en 175 px (desktop) onder de header, geen compact-klasse meer. Screenshots `screenshots/2026-10-28-ronde1/na-usp-*.png`.
**Let op, gedragsverandering:** de USP-balk blijft niet meer vast staan. Op de collecties zonder filterbalk in de vaste balk (`collection.json`, thee, accessoires, theeblikken, filtersmaatschepjes) blijft nu niets vast staan; daar bleef voorheen alleen de USP-balk vast. Als Mark de USP-balk op desktop toch compact vast wil houden, kan dat zonder sprong (vaste hoogte), maar dat is een ontwerpkeuze voor Mark.
**Niet nagelopen:** de oudere scripts in Bunzlau, Joeff, Blond en Rice die `filter-toolbar` een `top` geven; ze veranderen niets zichtbaars. Rice, Joeff, Blond, rooibos, kruiden-, vruchten-, groene en witte thee niet apart gemeten; ze delen dezelfde opbouw.
**Rollback:** zelfde als hierboven; de backups van `tr-base.css` en `theme.liquid` bevatten de oorspronkelijke compact-code.
