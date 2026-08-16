# ORBIS — Manus-Schreibtest 0.1

*Phase 8: Kann jedes Wort des Grundwortschatzes nach §26 vollständig in Orbis Manus zerlegt werden? Regelbasierte Zerlegung mit `orbis_validator.py --manus`; pro Silbe werden Kernkonsonant/Vokalträger, optionaler zweiter Anfangskonsonant, Vokal/Diphthong, Coda 1 und Coda 2 bestimmt. Die Grammatik 0.9.3 wurde nicht verändert.*

## 1. Methode

Jede Grundform wird per Rückverfolgungssuche in alle §5-konformen Silbenfolgen zerlegt (Notation je Silbe: `[Onset;Nukleus;Coda]`; leerer Onset = Vokalträger nach §26.2). Zwei Regelmengen: **strikt** = wörtliche §5.1-Liste; **erweitert** = zusätzlich VK/VKK/KKVKK (nötig wegen K-01 — sonst wären u. a. aul, eird, granz gar nicht schreibbar). Ein Wort gilt als eindeutig manus-schreibbar, wenn genau EINE Zerlegung existiert; bei mehreren: **[MANUS-AMBIGUITÄT]**.

## 2. Gesamtergebnis

| Kategorie | Anzahl |
|---|---|
| Grundformen geprüft | 281 |
| eindeutig zerlegbar | 203 |
| [MANUS-AMBIGUITÄT] mehrdeutig | 77 |
| nicht zerlegbar (bloße Wurzel suvr-, §14-Stütz-e) | 1 |

**77 von 281 Grundformen (27 %) haben mehr als eine regelkonforme Manus-Schreibung.** Ursache ist nicht die Schrift, sondern Befund **L-09**: §5/§26 legen keine Silbifizierungs-Präferenz fest (z. B. Onset-Maximierung, Diphthong-Vorrang). Für flektierte Formen steigt der Anteil weiter (jede V-K-V-Folge ist zweideutig).

## 3. Die Tastatur-Beispiele aus dem Prüfauftrag

| Wort | Zerlegungen | Verdikt |
|---|---|---|
| kra | kra  ([kr;a;]) | eindeutig |
| mel | mel  ([m;e;l]) | eindeutig |
| mela | me·la  ([m;e;] [l;a;]) **oder** mel·a  ([m;e;l] [;a;]) | [MANUS-AMBIGUITÄT] (2) |
| milk | milk  ([m;i;lk]) | eindeutig |
| breun | breun  ([br;eu;n]) | eindeutig |
| kaun | kaun  ([k;au;n]) | eindeutig |
| virn | virn  ([v;i;rn]) | eindeutig |
| moks | moks  ([m;o;ks]) | eindeutig |

**Kernproblem für eine spätere Tastatur:** Nach einem Vokal kann der nächste Konsonant dreierlei sein — Coda der laufenden Silbe, Kern der nächsten Silbe oder (nach weiterem Konsonanten) zweiter Anfangskonsonant. *mela* = `[m;e;l] + [Träger;a]` **oder** `[m;e] + [l;a]`; *kaun* = `[k;au;n]` **oder** `[k;a] + [Träger;u;n]`(erweitert); *breun* ist nur dank des einzigen eu-Belegs eindeutig. §26.8 beschreibt die Eingabe („Ein neuer Kernkonsonant schließt den vorherigen Block ab“) — das löst die **Eingabereihenfolge**, aber nicht die **Rückübertragung** aus der Lateinschreibung: dieselbe Buchstabenkette bleibt mehrdeutig. KEINE neue Tastaturregel wird hier festgelegt; dokumentiert als L-09.

## 4. Dokumentations- und Regelbefunde zu §26

1. **[U-10] §26.8 „20 Konsonantentasten“ ist terminologisch falsch.** Orbis hat 19 Konsonanten; die 20. Kernform ist der Vokalträger (§26.2), kein Konsonant. Korrekt: „19 Konsonantentasten + 1 Vokalträgertaste“ (an der Summe von 31 Tasten ändert sich nichts). Dokumentationsfehler, kein Systemfehler.
2. **[L-10] Strichstärkenregel unvollständig.** §26.9 definiert: dünn = Vokalzeichen, mittel = Fließlaute und Nasale (l r m n ñ), dick = Verschlusslaute (p t k b d g). **Für die 8 Reibelaute f s ş x v z j und die Affrikate ç ist keine Strichstärke definiert** — 9 der 19 Konsonantenklassen sind nicht erfasst.
3. **[L-09] Silbifizierungs-Präferenzregel fehlt** (siehe oben; Details Audit §2.4). Betrifft §5 und §26 gemeinsam.
4. Kein Befund: Silbenformel §26.1, Vokalpunktsystem §26.4, Coda-Platzierung §26.5–26.6 und die 6 Abschlusszeichen §26.7 sind in sich vollständig und decken alle im strikten wie erweiterten Modus zerlegbaren Silben ab (max. 2 Anfangskonsonanten, max. 2 Codas — deckungsgleich mit §5).

## 5. Vollständige Zerlegungstabelle des Grundwortschatzes

Notation: `Silbe·Silbe`, je Silbe `[Onset;Nukleus;Coda]`; leerer Onset = Vokalträger. Bei Mehrdeutigkeit alle Zerlegungen (max. 4 gezeigt). „(erw.)“ = nur mit den §5.1 fehlenden Formen VK/VKK/KKVKK zerlegbar (K-01).

| Wort | Kategorie | Zerlegung(en) | Verdikt |
|---|---|---|---|
| kaun | Kernwort-M | kaun | eindeutig |
| veiş | Kernwort-F | veiş | eindeutig |
| draun | Kernwort-M | draun | eindeutig |
| şirn | Kernwort-N | şirn | eindeutig |
| aul | Kernwort-N | a·ul · aul | [MANUS-AMBIGUITÄT] 2 Zerlegungen (erw.) |
| xerp | Kernwort-M | xerp | eindeutig |
| luiv | Kernwort-F | luiv | eindeutig |
| grein | Kernwort-F | grein | eindeutig |
| nauş | Kernwort-F | nauş | eindeutig |
| virn | Kernwort-N | virn | eindeutig |
| moks | Kernwort-M | moks | eindeutig |
| eird | Kernwort-F | e·ird · eird | [MANUS-AMBIGUITÄT] 2 Zerlegungen (erw.) |
| şaul | Kernwort-M | şaul | eindeutig |
| taiv | Kernwort-F | taiv | eindeutig |
| breun | Kernwort-N | breun | eindeutig |
| velkran | Nomen10%-N | vel·kran · velk·ran | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| soralm | Nomen10%-F | so·ralm | eindeutig |
| prilm | Nomen10%-F | prilm | eindeutig (erw.) |
| valru | Nomen-M-A | val·ru · valr·u | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| velkra | Nomen-M-A | vel·kra · velk·ra | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| zaldre | Nomen-M-A | zal·dre · zald·re | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| melru | Nomen-M-A | mel·ru · melr·u | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| talru | Nomen-M-A | tal·ru · talr·u | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| narku | Nomen-M-B | nar·ku · nark·u | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| larki | Nomen-M-B | lar·ki · lark·i | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| vlaiko | Nomen-M-B | vla·i·ko · vlai·ko · vlaik·o | [MANUS-AMBIGUITÄT] 3 Zerlegungen |
| vlenko | Nomen-M-B | vlen·ko | eindeutig |
| vrondo | Nomen-M-C | vron·do | eindeutig |
| luvandi | Nomen-M-C | lu·van·di · lu·vand·i | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| navildo | Nomen-M-C | na·vil·do · na·vild·o | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| morda | Nomen-M-C | mor·da · mord·a | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| sarla | Nomen-F-A | sar·la · sarl·a | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| prila | Nomen-F-A | pri·la · pril·a | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| kavla | Nomen-F-A | ka·vla · kav·la | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| zenlo | Nomen-F-A | zen·lo · zenl·o | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| mela | Nomen-F-A | me·la · mel·a | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| tala | Nomen-F-A | ta·la · tal·a | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| kirva | Nomen-F-B | kir·va · kirv·a | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| melva | Nomen-F-B | mel·va · melv·a | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| gluvi | Nomen-F-B | glu·vi · gluv·i | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| drovi | Nomen-F-B | dro·vi · drov·i | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| şonma | Nomen-F-C | şon·ma · şonm·a | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| soruma | Nomen-F-C | so·ru·ma · so·rum·a · sor·u·ma | [MANUS-AMBIGUITÄT] 3 Zerlegungen |
| klerma | Nomen-F-C | kler·ma | eindeutig |
| taluma | Nomen-F-C | ta·lu·ma · ta·lum·a · tal·u·ma | [MANUS-AMBIGUITÄT] 3 Zerlegungen |
| meluma | Nomen-F-C | me·lu·ma · me·lum·a · mel·u·ma | [MANUS-AMBIGUITÄT] 3 Zerlegungen |
| milne | Nomen-N-A | mil·ne · miln·e | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| verno | Nomen-N-A | ver·no · vern·o | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| melna | Nomen-N-A | mel·na · meln·a | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| drovna | Nomen-N-A | dro·vna · drov·na | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| skelnu | Nomen-N-A | skel·nu | eindeutig |
| talna | Nomen-N-A | tal·na · taln·a | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| taisa | Nomen-N-B | ta·i·sa · tai·sa · tais·a | [MANUS-AMBIGUITÄT] 3 Zerlegungen |
| pliso | Nomen-N-B | pli·so · plis·o | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| brasi | Nomen-N-B | bra·si · bras·i | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| vresto | Nomen-N-C | vre·sto · vres·to | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| melisto | Nomen-N-C | me·li·sto · me·lis·to · me·list·o · mel·i·sto | [MANUS-AMBIGUITÄT] 4 Zerlegungen |
| talisto | Nomen-N-C | ta·li·sto · ta·lis·to · ta·list·o · tal·i·sto | [MANUS-AMBIGUITÄT] 4 Zerlegungen |
| veltu | Nomen-N-C | vel·tu · velt·u | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| klaunuma | Nomen-F-C | kla·u·nu·ma · kla·u·num·a · klau·nu·ma · klau·num·a … | [MANUS-AMBIGUITÄT] 5 Zerlegungen |
| nestuma | Nomen-F-C | ne·stu·ma · ne·stum·a · nes·tu·ma · nes·tum·a … | [MANUS-AMBIGUITÄT] 5 Zerlegungen |
| salvuma | Nomen-F-C | sal·vu·ma · sal·vum·a · salv·u·ma | [MANUS-AMBIGUITÄT] 3 Zerlegungen |
| vaşnuma | Nomen-F-C | vaş·nu·ma · vaş·num·a · vaşn·u·ma | [MANUS-AMBIGUITÄT] 3 Zerlegungen |
| mirnuma | Nomen-F-C | mir·nu·ma · mir·num·a · mirn·u·ma | [MANUS-AMBIGUITÄT] 3 Zerlegungen |
| şauluma | Nomen-F-C | şa·u·lu·ma · şa·u·lum·a · şau·lu·ma · şau·lum·a … | [MANUS-AMBIGUITÄT] 5 Zerlegungen |
| tarnuma | Nomen-F-C | tar·nu·ma · tar·num·a · tarn·u·ma | [MANUS-AMBIGUITÄT] 3 Zerlegungen |
| saivuma | Nomen-F-C | sa·i·vu·ma · sa·i·vum·a · sai·vu·ma · sai·vum·a … | [MANUS-AMBIGUITÄT] 5 Zerlegungen |
| virnuma | Nomen-F-C | vir·nu·ma · vir·num·a · virn·u·ma | [MANUS-AMBIGUITÄT] 3 Zerlegungen |
| taivbreun | Nomen-Komp-N | taiv·breun | eindeutig |
| aulmelna | Nomen-Komp-N | a·ul·mel·na · a·ul·meln·a · a·ulm·el·na · a·ulm·eln·a … | [MANUS-AMBIGUITÄT] 8 Zerlegungen (erw.) |
| luivresto | Nomen-Komp-N | lu·i·vre·sto · lu·i·vres·to · lui·vre·sto · lui·vres·to … | [MANUS-AMBIGUITÄT] 7 Zerlegungen |
| milk | Verbwurzel | milk | eindeutig |
| zaub | Verbwurzel | zaub | eindeutig |
| tal | Verbwurzel | tal | eindeutig |
| nast | Verbwurzel | nast | eindeutig |
| prev | Verbwurzel | prev | eindeutig |
| soñ | Verbwurzel | soñ | eindeutig |
| dremn | Verbwurzel | dremn | eindeutig (erw.) |
| prens | Verbwurzel | prens | eindeutig (erw.) |
| saiv | Verbwurzel | saiv | eindeutig |
| vlent | Verbwurzel | vlent | eindeutig (erw.) |
| rusk | Verbwurzel | rusk | eindeutig |
| leşn | Verbwurzel | leşn | eindeutig |
| traiv | Verbwurzel | traiv | eindeutig |
| mald | Verbwurzel | mald | eindeutig |
| stan | Verbwurzel | stan | eindeutig |
| sor | Verbwurzel | sor | eindeutig |
| salv | Verbwurzel | salv | eindeutig |
| vaşn | Verbwurzel | vaşn | eindeutig |
| mirn | Verbwurzel | mirn | eindeutig |
| tarn | Verbwurzel | tarn | eindeutig |
| valn | Modalwurzel | valn | eindeutig |
| dolm | Modalwurzel | dolm | eindeutig |
| vlek | Modalwurzel | vlek | eindeutig |
| tirn | Modalwurzel | tirn | eindeutig |
| nest | Modalwurzel | nest | eindeutig |
| suvr | Modalwurzel | — | NICHT ZERLEGBAR |
| es | Verbwurzel-irr | es | eindeutig (erw.) |
| nuv | Verbwurzel-irr | nuv | eindeutig |
| vurn | Verbwurzel-irr | vurn | eindeutig |
| mel | Verbwurzel-irr | mel | eindeutig |
| vand | Verbwurzel-irr | vand | eindeutig |
| narg | Verbwurzel-irr | narg | eindeutig |
| zav | Verbwurzel-irr | zav | eindeutig |
| dalv | Verbwurzel-irr | dalv | eindeutig |
| vlaid | Adjektiv | vlaid | eindeutig |
| nirm | Adjektiv | nirm | eindeutig |
| selv | Adjektiv | selv | eindeutig |
| morn | Adjektiv | morn | eindeutig |
| loşn | Adjektiv | loşn | eindeutig |
| granz | Adjektiv | granz | eindeutig (erw.) |
| zirv | Adjektiv | zirv | eindeutig |
| trelm | Adjektiv | trelm | eindeutig (erw.) |
| misn | Adjektiv | misn | eindeutig |
| velm | Adjektiv | velm | eindeutig |
| girn | Adjektiv | girn | eindeutig |
| luid | Adjektiv | luid | eindeutig |
| şaln | Adjektiv | şaln | eindeutig |
| xarn | Adjektiv | xarn | eindeutig |
| vresn | Adjektiv | vresn | eindeutig (erw.) |
| zilv | Adjektiv | zilv | eindeutig |
| tolm | Adjektiv | tolm | eindeutig |
| klaun | Adjektiv | klaun | eindeutig |
| norv | Adjektiv | norv | eindeutig |
| xan | Adjektiv | xan | eindeutig |
| kem | Fragewort | kem | eindeutig |
| kelt | Fragewort | kelt | eindeutig |
| kur | Fragewort | kur | eindeutig |
| kan | Fragewort | kan | eindeutig |
| grais | Fragewort | grais | eindeutig |
| kolm | Fragewort | kolm | eindeutig |
| kelra | Fragewort-adj | kel·ra · kelr·a | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| kella | Fragewort-adj | kel·la · kell·a | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| kelna | Fragewort-adj | kel·na · keln·a | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| kilra | Demonstrativ | kil·ra · kilr·a | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| killa | Demonstrativ | kil·la · kill·a | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| kilna | Demonstrativ | kil·na · kiln·a | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| dolra | Demonstrativ | dol·ra · dolr·a | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| dolla | Demonstrativ | dol·la · doll·a | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| dolna | Demonstrativ | dol·na · doln·a | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| kaun | Indefinit | kaun | eindeutig |
| kelsu | Indefinit | kel·su · kels·u | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| xakaun | Indefinit | xa·kaun | eindeutig |
| kelte | Indefinit | kel·te · kelt·e | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| xakelte | Indefinit | xa·kel·te · xa·kelt·e | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| se | Reflexiv | se | eindeutig |
| fai | Relativ | fa·i · fai | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| zva | Präposition | zva | eindeutig |
| xun | Präposition | xun | eindeutig |
| prai | Präposition | pra·i · prai | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| dral | Präposition | dral | eindeutig |
| dun | Präposition | dun | eindeutig |
| ven | Präposition | ven | eindeutig |
| nul | Präposition | nul | eindeutig |
| gral | Präposition | gral | eindeutig |
| şlan | Präposition | şlan | eindeutig |
| tel | Präposition | tel | eindeutig |
| kru | Präposition | kru | eindeutig |
| span | Präposition | span | eindeutig |
| drel | Präposition | drel | eindeutig |
| glem | Präposition | glem | eindeutig |
| traus | Präposition | traus | eindeutig |
| şlim | Präposition | şlim | eindeutig |
| ze | Konj-koord | ze | eindeutig |
| vu | Konj-koord | vu | eindeutig |
| klas | Konj-koord | klas | eindeutig |
| xer | Konj-koord | xer | eindeutig |
| fai | Konj-sub | fa·i · fai | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| grali | Konj-sub | gra·li · gral·i | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| tund | Konj-sub | tund | eindeutig |
| şlani | Konj-sub | şla·ni · şlan·i | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| dremi | Konj-sub | dre·mi · drem·i | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| glemi | Konj-sub | gle·mi · glem·i | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| trausi | Konj-sub | tra·u·si · trau·si · traus·i | [MANUS-AMBIGUITÄT] 3 Zerlegungen |
| nel | Zahl | nel | eindeutig |
| dram | Zahl | dram | eindeutig |
| teln | Zahl | teln | eindeutig |
| kalm | Zahl | kalm | eindeutig |
| mern | Zahl | mern | eindeutig |
| vesn | Zahl | vesn | eindeutig |
| zerm | Zahl | zerm | eindeutig |
| glon | Zahl | glon | eindeutig |
| pirn | Zahl | pirn | eindeutig |
| xelm | Zahl | xelm | eindeutig |
| munar | Zahl | mu·nar | eindeutig |
| kraven | Zahl | kra·ven | eindeutig |
| xelmnel | Zahl-Komp | xelm·nel | eindeutig |
| dramxelm | Zahl-Komp | dram·xelm | eindeutig |
| telnxelmmern | Zahl-Komp | teln·xelm·mern | eindeutig |
| nunda | Partikel/Adverb | nun·da · nund·a | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| zirna | Partikel/Adverb | zir·na · zirn·a | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| granza | Partikel/Adverb | gran·za | eindeutig |
| nun | Partikel/Adverb | nun | eindeutig |
| dalvur | Partikel/Adverb | dal·vur | eindeutig |
| xanur | Partikel/Adverb | xa·nur | eindeutig |
| kilur | Partikel/Adverb | ki·lur | eindeutig |
| dolur | Partikel/Adverb | do·lur | eindeutig |
| vran | Partikel/Adverb | vran | eindeutig |
| skirm | Partikel/Adverb | skirm | eindeutig (erw.) |
| ain | Partikel/Adverb | a·in · ain | [MANUS-AMBIGUITÄT] 2 Zerlegungen (erw.) |
| xaus | Partikel/Adverb | xaus | eindeutig |
| xa | Partikel/Adverb | xa | eindeutig |
| mai | Partikel/Adverb | ma·i · mai | [MANUS-AMBIGUITÄT] 2 Zerlegungen |
| kon | Partikel/Adverb | kon | eindeutig |
| zil | Partikel/Adverb | zil | eindeutig |
| selvai | Partikel/Adverb | sel·va·i · sel·vai · selv·a·i · selv·ai | [MANUS-AMBIGUITÄT] 4 Zerlegungen |
| melai | Partikel/Adverb | me·la·i · me·lai · mel·a·i · mel·ai | [MANUS-AMBIGUITÄT] 4 Zerlegungen |
| selves | Partikel/Adverb | sel·ves | eindeutig |
| praum | Partikel/Adverb | praum | eindeutig |
| vim | Pronomenform | vim | eindeutig |
| vin | Pronomenform | vin | eindeutig |
| viş | Pronomenform | viş | eindeutig |
| vis | Pronomenform | vis | eindeutig |
| şet | Pronomenform | şet | eindeutig |
| şen | Pronomenform | şen | eindeutig |
| şeş | Pronomenform | şeş | eindeutig |
| şes | Pronomenform | şes | eindeutig |
| şevar | Pronomenform | şe·var | eindeutig |
| şevan | Pronomenform | şe·van | eindeutig |
| şevaş | Pronomenform | şe·vaş | eindeutig |
| şevas | Pronomenform | şe·vas | eindeutig |
| ro | Pronomenform | ro | eindeutig |
| ron | Pronomenform | ron | eindeutig |
| roş | Pronomenform | roş | eindeutig |
| ros | Pronomenform | ros | eindeutig |
| lo | Pronomenform | lo | eindeutig |
| lon | Pronomenform | lon | eindeutig |
| loş | Pronomenform | loş | eindeutig |
| los | Pronomenform | los | eindeutig |
| no | Pronomenform | no | eindeutig |
| non | Pronomenform | non | eindeutig |
| noş | Pronomenform | noş | eindeutig |
| nos | Pronomenform | nos | eindeutig |
| viñ | Pronomenform | viñ | eindeutig |
| viñan | Pronomenform | vi·ñan | eindeutig |
| viñaş | Pronomenform | vi·ñaş | eindeutig |
| viñas | Pronomenform | vi·ñas | eindeutig |
| şeñ | Pronomenform | şeñ | eindeutig |
| şeñan | Pronomenform | şe·ñan | eindeutig |
| şeñaş | Pronomenform | şe·ñaş | eindeutig |
| şeñas | Pronomenform | şe·ñas | eindeutig |
| oñ | Pronomenform | oñ | eindeutig (erw.) |
| oñan | Pronomenform | o·ñan | eindeutig |
| oñaş | Pronomenform | o·ñaş | eindeutig |
| oñas | Pronomenform | o·ñas | eindeutig |
| xra | Artikelform | xra | eindeutig |
| xran | Artikelform | xran | eindeutig |
| xraş | Artikelform | xraş | eindeutig |
| xras | Artikelform | xras | eindeutig |
| xrañ | Artikelform | xrañ | eindeutig |
| xrañan | Artikelform | xra·ñan | eindeutig |
| xrañaş | Artikelform | xra·ñaş | eindeutig |
| xrañas | Artikelform | xra·ñas | eindeutig |
| xla | Artikelform | xla | eindeutig |
| xlan | Artikelform | xlan | eindeutig |
| xlaş | Artikelform | xlaş | eindeutig |
| xlas | Artikelform | xlas | eindeutig |
| xlañ | Artikelform | xlañ | eindeutig |
| xlañan | Artikelform | xla·ñan | eindeutig |
| xlañaş | Artikelform | xla·ñaş | eindeutig |
| xlañas | Artikelform | xla·ñas | eindeutig |
| xna | Artikelform | xna | eindeutig |
| xnan | Artikelform | xnan | eindeutig |
| xnaş | Artikelform | xnaş | eindeutig |
| xnas | Artikelform | xnas | eindeutig |
| xnañ | Artikelform | xnañ | eindeutig |
| xnañan | Artikelform | xna·ñan | eindeutig |
| xnañaş | Artikelform | xna·ñaş | eindeutig |
| xnañas | Artikelform | xna·ñas | eindeutig |
| vra | Artikelform | vra | eindeutig |
| vran | Artikelform | vran | eindeutig |
| vraş | Artikelform | vraş | eindeutig |
| vras | Artikelform | vras | eindeutig |
| vla | Artikelform | vla | eindeutig |
| vlan | Artikelform | vlan | eindeutig |
| vlaş | Artikelform | vlaş | eindeutig |
| vlas | Artikelform | vlas | eindeutig |
| vna | Artikelform | vna | eindeutig |
| vnan | Artikelform | vnan | eindeutig |
| vnaş | Artikelform | vnaş | eindeutig |
| vnas | Artikelform | vnas | eindeutig |

*Reproduktion: `python3 orbis_validator.py --manus`.*
