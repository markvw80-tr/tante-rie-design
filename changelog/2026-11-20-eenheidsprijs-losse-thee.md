# Eenheidsprijs losse thee (V134 optie B), 20-11-2026

## Wat
Eenheidsprijs (bijvoorbeeld "€10,63 / 100 g") klein onder de prijs in het eigen tr-price-blok en in de vaste prijsbalk op mobiel. Alleen bij varianten met een ingevulde eenheidsprijs; de regel wisselt mee met de variantkeuze. Het Product-JSON-LD krijgt in het bestaande Offer een `priceSpecification` van het type UnitPriceSpecification volgens de eisen van SEO (bericht 2026-11-20-230602): price = variantprijs, referenceQuantity = inhoud (GRM/KGM/MLT/LTR), valueReference = basiseenheid. Alleen als de variant een eenheidsprijs heeft en de Offer-prijs gelijk is aan die variant.

Bijkomend: de begin-prijs in tr-price en de sticky balk komt nu van de geselecteerde variant (selected_or_first_available_variant) in plaats van product.price, zodat prijs en eenheidsprijs altijd bij dezelfde variant horen.

## Bestanden
- `sections/tr-product-redesign.liquid` (CSS .tr-unit-price, variant-JSON `unitPrice`, regel onder tr-price, regel in sticky balk, updateUI)
- `snippets/tr-unit-price-text.liquid` (nieuw)
- `snippets/tr-product-schema.liquid` (priceSpecification in Offer)

## Thema
- Ontwikkelthema: 205914898696 `design-eenheidsprijs-2026-11-20`
- Preview: https://0qkm31-r6.myshopify.com/products/kamille?preview_theme_id=205914898696
- Basis: verse pull van live 205262029064 op 20-11-2026 (`.theme-werkkopie/eenheidsprijs`)
- `shopify theme check`: geen nieuwe meldingen (bestaande ImgWidthAndHeight regel 256 blijft).

## Waarom
Besluit Mark V134 optie B (20-11-2026), eisen schema van SEO (20-11-2026).

## Stand
Code staat op het ontwikkelthema, maar de regel en het schemablok blijven nog leeg: Shopify geeft voor kamille en gemberwortel geen unit_price of unit_price_measurement door aan de winkel (`/products/kamille.js` toont beide als null), terwijl PIM het variantveld op 18-11 gevuld zag. Gevraagd aan PIM om na te gaan waarom (mogelijk de instelling om de eenheidsprijs te tonen bij de variant). Screenshots voor en na volgen zodra de eenheidsprijs zichtbaar is: `screenshots/2026-11-20-eenheidsprijs/`.

## Akkoord Mark
Akkoord op bouwen (V134 B). Live zetten pas na akkoord Mark op de preview. Nog niet gepubliceerd.

## Rollback
Live thema 205262029064 is ongewijzigd. Mocht dit later live gaan: terugzetten door 205262029064 (of de dan vorige live) opnieuw te publiceren, of de twee gewijzigde bestanden terugzetten vanuit de backups `changelog/2026-11-20-eenheidsprijs.backup-tr-product-redesign.liquid` en `changelog/2026-11-20-eenheidsprijs.backup-tr-product-schema.liquid` (live versie van 20-11); `snippets/tr-unit-price-text.liquid` kan dan weg.
