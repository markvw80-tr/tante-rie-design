# 2026-10-28, collectiepagina Zwarte Thee: H2 boven het productraster (TEST van de opzet)

**Wat:** In `sections/tr-collection-zwarte-thee.liquid` is boven het productraster een H2 toegevoegd: "Alle losse zwarte thee van Tante Rie" (Playfair Display 400, clamp(1.5rem,2.5vw,2rem), zelfde stijl als de bestaande H2 "Bestellen, verzenden & afhalen"). Verder niets; itemprop, JSON-LD, koppen en links ongemoeid.
**Eis van SEO:** bericht `2026-10-28-190148-seo-test-re-heading-eis-collectiepagina-zwarte-thee.md` (gesimuleerd door Claude als test; geen echte SEO-beslissing, dus de tekst moet door het SEO-team worden bevestigd voordat dit ooit live gaat).
**Kopvolgorde na wijziging:** H1 Zwarte Thee, H2 Alle losse zwarte thee van Tante Rie, H2 Van theeplantage tot jouw kopje, H2 Bestellen verzenden en afhalen (met H3's), H2 Waar komt losse zwarte thee vandaan, H2 Meer dan 40 losse zwarte theesoorten. Geen sprongen.
**Ontwikkelthema:** `design-zwarte-thee-h2-2026-10-28`, id 204337217800 (unpublished). Preview: https://0qkm31-r6.myshopify.com/collections/zwarte-thee?preview_theme_id=204337217800
**Live thema:** 204204900616 "Bunzlau voorraad + TikTok 2026-10-26", ongewijzigd (gecontroleerd na de push; live pagina bevat de nieuwe kop niet).
**Screenshots:** `screenshots/2026-10-28-zwarte-thee-h2/` voor en na, desktop 1440 en mobiel 390 (lokaal, gitignored). De scrollpositie kwam niet op het raster maar op de bovenkant; de nieuwe kop staat op beide formaten in beeld.
**Akkoord Mark:** nee, niet gevraagd; test op ontwikkelthema. Publiceren doet Mark zelf.

## Rollback
Niets live gewijzigd, dus terugdraaien is: het ontwikkelthema 204337217800 verwijderen of negeren. Mocht het ooit gepubliceerd worden en teruggedraaid moeten worden: zet het vorige live thema 204204900616 terug als live, of herstel `sections/tr-collection-zwarte-thee.liquid` met de backup `changelog/2026-10-28-zwarte-thee-h2.backup-tr-collection-zwarte-thee.liquid` (één regel, de `<h2 class="trzt-grid-heading">`, verwijderen).

## Review
Reviewer niet ingezet (team start met Design Lead en Theme Developer). Basischecks door de Design Lead: `shopify theme check` geeft in dit bestand geen nieuwe overtreding (de bestaande VariableName-melding staat al op het live thema; 689 meldingen in het hele thema zijn vooraf aanwezig); kopniveaus zonder sprongen; contrast: donkerbruin #1c1c14 op #faf8f2; geen nieuwe scripts of afbeeldingen, dus geen invloed op laadtijd.
