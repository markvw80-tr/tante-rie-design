# Designreview tanterie.nl, 28-10-2026

Opdracht van Mark: in hoofdlijnen laten zoals het is, met verbeteringen die de beleving net prettiger maken, met nadruk op mobiel. Alleen gelezen en gemeten; er is niets gewijzigd. Gemeten op live thema 204204900616 met een lege browser (390 px mobiel, 1440 px desktop). Screenshots lokaal in `screenshots/2026-10-28-review/`.

## Waarom mobiel voorop

Uit de Search Console-export van SEO (21-10): 74 procent van de organische klikken in 90 dagen is mobiel (964 van 1.308), 72 procent in de nulmeting. Dat zijn zoekklikken, geen sessies; GA4 staat niet in `data/ga4/`. Aan SEO gevraagd naar sessies en conversie per apparaat (mailbox, 28-10). Lab-metingen van SEO op 21-10, mobiel: prestatiescore 61 (home), 68 (Bunzlau) en 60 (Earl Grey), LCP 6,9 s, 5,1 s en 11,3 s. Toegankelijkheid scoort 96 tot 97.

## Wat goed is en blijft

Merkgevoel, kleur, Playfair-koppen, hero met winkel in Borne, zwarte usp-balk, productkaarten met ronde foto's, "Het verhaal" en de zetadvies-tegels op de productpagina, bruine hero's per collectie. Geen horizontale scroll op mobiel, elke pagina één H1, alle afbeeldingen hebben alt-tekst.

## Verbeterpunten, op volgorde van impact

**1. Winkelwagenknop op de productpagina is op mobiel onleesbaar (fout, hoge impact).** In `assets/tr-base.css` maakt de regel `[data-tr-atc]` binnen `max-width: 767px` van elke toevoegen-knop een cirkel van 40 px met `font-size: 0`. Die regel is bedoeld voor kleine kaartknoppen, maar raakt ook de hoofdknop "Aan winkelwagen toevoegen" (nu een klein bolletje met tasje onder de prijs) en de vaste balk onder in beeld "In winkelwagen" (een lange zwarte ellips met alleen een tasje, zonder tekst). Dit is de belangrijkste actie van de shop. Oplossing: de regel alleen laten gelden voor kaartknoppen (bijvoorbeeld `.tr-card-btn[data-tr-atc]`), hoofdknop weer volle breedte met tekst. Eén bestand, klein.

**2. Twee winkelwagenknoppen over elkaar op productpagina en collectie (middel).** De zwevende ronde winkelwagenknop rechtsonder (56 px, `position: fixed`) ligt op mobiel boven het uiteinde van de vaste toevoegen-balk en over productfoto's, terwijl de header al een winkelwagen heeft. Voorstel: op productpagina's weghalen of boven de balk plaatsen; elders alleen tonen na scrollen. Dit is een keuze voor Mark of het gedrag bewust is.

**3. Collectiepagina mobiel: één kolom en een zware vaste bovenbalk (hoge impact).** Onder 400 px breedte toont het raster één kolom (kaarten van 359 px breed). Zwarte thee wordt daardoor 28.845 px lang voor 43 producten (iPhone 390 px valt hieronder; veel Android-telefoons ook). Daarnaast blijven usp-balk (drie regels) en filterknoppen vast onder de header staan: ongeveer 245 van 844 px, rond 30 procent van het scherm, blijft bedekt tijdens het scrollen. Voorstel: twee kolommen vanaf 340 px met compactere kaart (kleinere foto-opvulling, korte beschrijving afkappen op twee regels), usp-balk niet sticky of een regel hoog op mobiel, alleen filters sticky. Raakt alle `tr-collection-*` secties; de secties zijn vrijwel kopieën, dus eerst in één sectie bouwen en de rest volgt met dezelfde wijziging.

**4. Productpagina mobiel: titel en prijs komen laat in beeld (middel).** Boven de vouw staan foto, miniaturen en vijf tag-chips (Bergamot, Earl-grey, Klassiek, Zwarte-thee, 90 g) voordat de titel verschijnt; prijs en toevoegen-knop staan pas na zetadvies en verhaal. Voorstel: chips kleiner of onder de titel, titel en prijs direct onder de foto, hoofdknop vóór "Het verhaal". Merkbeleving blijft: verhaal en zetadvies gewoon eronder.

**5. Aanraakdoelen te klein (middel).** Meting op mobiel: broodkruimels 16 px hoog, tekstlinks op home 17 tot 24 px, "Bekijk beoordelingen" 22 px, filterpillen 35 px, kaartknop "Toevoegen" 32 px hoog met 12 px tekst, labels van 10 en 11 px (`trh-prod-type`, `trzt-card-type`, `trzt-tag` 9,5 px). Richtlijn 44 px voor links en knoppen, minimaal 12 px voor tekst. Opvulling vergroten zonder het uiterlijk te veranderen.

**6. Snelheid op mobiel (hoog, deels buiten de theme-code).** LCP 5 tot 11 s in de lab. Controleren in de eerste ronde: heroafbeelding en eerste productfoto met `fetchpriority="high"` en niet lazy (de meting vond lazy-geladen afbeeldingen binnen het eerste scherm op home, collectie en product), kleinere afbeeldingsbreedtes via `srcset`, en ongeveer 105 scripts per pagina; reviewscript en andere apps beoordelen. Dit is werk voor de Performance & Accessibility Reviewer en een nieuwe meting, niet voor gokken.

**7. Hero homepage mobiel (laag).** De knop "Ons verhaal" is nauwelijks zichtbaar (transparante rand op lichte foto), en de wazige foto achter de tekst oogt op mobiel vlak. Rand en tekstkleur sterker, of foto licht donkerder onder de knoppen.

**8. Kleine punten (laag).** Productpagina: de prijs staat dubbel zichtbaar (in beeld en in de vaste balk). Home: de tekstlinks onder de tegels (Theewinkel in Borne, Bunzlau servies, Serviezen) zijn klein en staan los; maak er duidelijke knoppen of tegels van. Footer en cart-drawer niet beoordeeld.

## Niet beoordeeld

Winkelwagenpagina, cart-drawer en checkout (zouden een wagen vullen; na akkoord van Mark op een dev-thema te doen), header op tablet, blog, accountpagina's. Desktop is globaal bekeken en vertoont dezelfde patronen (kleine labels, 133 kleine aanraakdoelen op de collectiepagina), zonder grote fouten.

## Buiten Design (doorzetten)

Productpagina Earl Grey: in het verhaal ontbreekt een spatie na "melk." (tekst staat in PIM-data). Tags worden zichtbaar als "EARL-GREY" en "ZWARTE-THEE" met koppelteken: dat is tagnotatie van PIM; Design kan weergave aanpassen (koppelteken naar spatie tonen) maar wijzigt de tags niet. Doorgeven aan PIM via de mailbox na akkoord van Mark.

## Raakt de open punten van de stijlgids

Punt 5, 6 en 7 sluiten niet; de voorstellen gebruiken bestaande waarden. Een nieuwe knopstijl op de productpagina (punt 1) volgt de bestaande `tr-btn-primary` van de sectie (zwart, pil), tot Mark open punt 2 beslist.

## Voorstel voor de volgorde

Ronde 1 (klein, direct waarde): punten 1 en 2, daarna 5 voor knoppen en breadcrumb. Ronde 2: punt 3 en 4. Ronde 3: punt 6 met meting vooraf en achteraf. Elke ronde op een ontwikkelthema met screenshots voor en na, Reviewer ingezet voor ronde 3. Mark publiceert zelf.
