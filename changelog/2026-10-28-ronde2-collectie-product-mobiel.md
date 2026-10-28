# 2026-10-28, ronde 2 designreview: collectie in twee kolommen en productpagina-volgorde (mobiel)

Bouwt voort op ronde 1 (inclusief USP-balkfix). Bron: `opdrachten/2026-10-28-review-webshop.md`, punt 3 en 4.

**Wat:**
1. Alle `sections/tr-collection-*.liquid` (11 bestanden): de regel die onder 400 px één kolom toont geldt nu pas onder 340 px; de `sizes`-waarde in `tr-collection-bunzlau.liquid` is daarop aangepast. Telefoons van 340 tot 400 px (o.a. iPhone 390 en veel Android) krijgen twee kolommen.
2. `assets/tr-base.css`, nieuw mobiel blok (max 700 px): kaartopvulling 12 px en beschrijving afgekapt op drie regels in het raster.
3. Productpagina `tr-product-redesign` (via `.tr-product-info`, max 700 px): volgorde titel, ondertitel, beoordelingen, varianten, prijs en aantal, hoofdknop, verlanglijst, voorraad, vertrouwensregel, daarna tags, zetadvies, smaakprofiel en verhaal. Alleen de weergavevolgorde (CSS `order`); de markup, koppen en tekst blijven hetzelfde en in dezelfde DOM-volgorde, dus SEO-technisch geen verschil.
Desktop ongewijzigd (alles zit in mobiele media queries).

**Ontwikkelthema:** `design-ronde2-collectie-product-mobiel-2026-10-28`, id 204342395144 (unpublished). Preview: https://0qkm31-r6.myshopify.com/?preview_theme_id=204342395144. Live thema 204204900616 ongewijzigd.
**Gemeten, zwarte thee, 390 px:** paginahoogte 28.845 naar 14.081 px, kolommen 1 naar 2 (kaart 173 px breed, 372 px hoog tegen 359 en 538), geen horizontale scroll. 360 px: 27.941 naar 14.168 px. 412 px: ongewijzigd (had al twee kolommen).
**Gemeten, Earl Grey, 390 px:** hoofdknop van 1513 px naar 950 px vanaf de paginatop; titel van 769 naar 688 px. Titel staat net op de rand van het eerste scherm (foto en miniaturen nemen nog ongeveer 650 px in); de hoofdknop komt na een halve schermlengte scrollen in beeld.
**Screenshots:** `screenshots/2026-10-28-ronde2/` voor en na, mobiel (lokaal).
**Niet getest:** een product met meerdere varianten op dit sjabloon, andere productsjablonen (Bunzlau, Rice, Blond, Joeff hebben eigen secties en zijn niet aangepast), Reviewer niet ingezet, toevoegen aan de winkelwagen.
**Open ontwerpkeuze (niet gedaan):** de productfoto op mobiel kleiner of lager maken zodat titel en prijs in het eerste scherm passen; dat raakt de beeldverhouding en is aan Mark.
**Rollback:** thema niet publiceren, of live terugzetten op 204204900616. Voor losse bestanden: de backups van ronde 1 (`changelog/2026-10-28-ronde1.backup-*`) voor `tr-base.css` en `theme.liquid`; de 11 collectiesecties zijn terug te zetten door `339px` weer `400px` te maken.
**Akkoord Mark:** gegeven voor bouwen (28-10); publiceren nog niet.

## Aanvulling: knop "Kies decor" afgesneden op Bunzlau (gemeld door Mark)

**Oorzaak:** een gevolg van de twee kolommen uit deze ronde. Prijs (1,4 rem) en de knop "Kies decor" (101 px) stonden naast elkaar in de kaartvoet, maar de kaart is op 390 px maar 173 px breed met 149 px bruikbaar; de knop stak 8 px buiten de kaart (gemeten op 390 en 360 px). Dezelfde fout zat in "Bestel nu" bij Blond.
**Wat:** in `sections/tr-collection-bunzlau.liquid` en `sections/tr-collection-blond.liquid` mag de kaartvoet op mobiel (max 700 px) afbreken: de knop staat op een eigen regel over de volle kaartbreedte, minimaal 44 px hoog.
**Gemeten op 204342395144:** alle 13 collecties op 390 en 360 px: geen enkel element meer buiten zijn kaart; Blond ook op 412 px schoon; geen horizontale scroll. Screenshot: `screenshots/2026-10-28-ronde2/bunzlau-na-fix-kaarten.png`.
**Open (klein):** het label "Op voorraad in 1 decor" breekt op Bunzlau-kaarten over twee regels en loopt tot de kaartrand. Niet aangepast.
