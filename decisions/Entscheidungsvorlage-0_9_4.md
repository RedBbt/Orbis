# ORBIS 0.9.4 — Entscheidungsvorlage

*Vorlage für die Sprachdesigner. Dieses Dokument legt NICHTS fest — es bereitet die sechs P1-Entscheidungen (plus zwei Sonderfälle) so auf, dass jede Option mit konkreten Sätzen sichtbar wird. Alle Orbis-Beispiele in den Optionskästen sind **hypothetisch und nicht kanonisch**; kanonisch wird erst, was in 0.9.4 steht. Grundlage: `Orbis-Testbericht-0_1.md`, `Orbis-Audit-0_1.md`, Simulationsdaten aus `orbis_validator.py --sim-l09`.*

**Empfohlene Reihenfolge der Entscheidungen:** E1 (Relativsatz) und E2 (Modal im Nebensatz) zuerst — beide betreffen das Endfeld des Nebensatzes und sollten zueinander passen. Danach E3–E6 (unabhängig voneinander). E7 (L-09) ist für die Grammatik P2, für die Tastatur aber blockierend. E8 (velkran) ist der einzige Punkt, der den Wortschatz-Freeze berühren würde.

---

## E1 · L-02 — Relativsatz (Tests 100–102, 149)

**Problem:** §13.4 nennt *fai* als Relativpronomen, aber es existiert keine einzige Regel zur Konstruktion; zusätzlich ist *fai* homonym mit *fai* „dass" (§20).

| | Option A: fai indeklinabel | Option B: fai dekliniert | Option C: neues Relativwort |
|---|---|---|---|
| Prinzip | fai leitet ein, Verbendstellung wie jeder Nebensatz; die Rolle des Bezugsworts bleibt unbezeichnet oder wird durch ein Pronomen im Satz wiederaufgenommen | fai flektiert wie ein Pronomen: fai / fain / faiş / fais | fai bleibt nur „dass"; Relativ übernimmt z. B. ein dekliniertes kel- oder ein Neuwort |
| „der Mann, der kommt" | *xra valru, fai vandat* | *xra valru, fai vandat* | *xra valru, kelra vandat* (hypothetisch) |
| „die Frau, die ich sehe" | *xla sarla, fai vim milkam* (Rolle nur aus Kontext) | *xla sarla, fain vim milkam* | *xla sarla, kellan vim milkam* |
| „der Mann, dem ich das Buch gebe" | ⚠ nicht ausdrückbar oder nur mit Stützpronomen (*fai vim roş xnan vreston dalvam* — „dass ich ihm…") | *xra valru, faiş vim xnan vreston dalvam* | *xra valru, kelraş vim xnan vreston dalvam* |
| Kosten/Nutzen | billigste Regel; Dativ-/Genitivfälle bleiben schwach; fai-Homonymie bleibt | volle Ausdruckskraft; 3 neue Formen (fain/faiş/fais sind phonotaktisch sauber: ✓ geprüft); Homonymie im Nominativ bleibt | löst auch die Homonymie; kel- ist aber schon Fragewort („welcher") — neue Doppelrolle; Neuwort bräche den Freeze nicht (Funktionswort), wäre aber die größte Änderung |
| Folgeänderungen | §13.4 + neuer §17-Absatz | §13.4 (Formentabelle) + §17-Absatz | §13.4, §18.2, §20 |

*Hinweis aus dem Test: Die Verbstellung im Relativsatz sollte in jedem Fall ausdrücklich festgelegt werden (Endstellung liegt nahe, da §17.2 für alle Nebensätze gilt — aber sagen muss es 0.9.4).*

---

## E2 · K-05 — Modalverb im Nebensatz (Tests 103, 105)

**Problem:** §16.1 („Vollverb im Infinitiv am Satzende") und §17.2 („im Nebensatz steht das finite Verb am Ende") beanspruchen dieselbe Position.

| | Option A: Infinitiv vor Finitum („deutsches Muster") | Option B: Finitum vor Infinitiv |
|---|---|---|
| „…, dass der Mann gehen muss" | *…, fai xra valru melex dolmat* | *…, fai xra valru dolmat melex* |
| mit Negation (Test 105) | *…, fai lo xnan vreston xa leşnex valnat*? oder *… leşnex xa valnat*? — xa-Position MUSS mitentschieden werden (§18.3 sagt „vor dem finiten Verb": dann *… leşnex xa valnat*) | *…, fai lo xnan vreston xa valnat leşnex* (xa direkt vor Finitum, Infinitiv dahinter) |
| Konsistenz | folgt §1 („Satzbau folgt eng dem Deutschen"); Endstellung des FINITEN Verbs (§17.2) bleibt wörtlich wahr | §17.2 müsste umformuliert werden („Verbkomplex am Ende, Finitum zuerst"); klingt weniger deutsch, ist aber die einfachere Serialisierung |
| Empfehlung des Prüfstands | — keine; beide sind logisch sauber. Wichtig ist nur: **die xa-Position im Endfeld in derselben Entscheidung festlegen** (sonst bleibt Test 105 offen) | |

---

## E3 · L-01 — Stellung des Genitivattributs (Tests 036, 039)

**Problem:** Morphologie vollständig, Stellung nirgends geregelt. Faktenlage: ALLE Beispiele der Grammatik stellen nach; §13.3 schreibt für Possessive „nachgestellt" vor.

| | Option A: nachgestellt normieren | Option B: beide Stellungen zulassen |
|---|---|---|
| „das Haus des Mannes" | *xna breun xras valrus* | zusätzlich *xras valrus xna breun* (z. B. als markiert/poetisch) |
| Kosten/Nutzen | ein Satz in §17; deckt alle 71 Beispiele; Testkorpus 037–045, 148 werden ohne Änderung normkonform | Flexibilität, aber Parsing-Ambiguität wächst (wo endet die NP?); für NZE-Dichtung ohnehin über §17.5-NZE lösbar |
| Stapelung (Test 039) | zusätzlich festlegen: „das Buch meines Freundes" = *xna vresto xras velkras vis* (Possessiv klebt am Genitivkopf) — oder Umschreibung erzwingen | gleiche Zusatzfrage |

---

## E4 · L-03 — Deklination der Fragewörter (Tests 074–076)

**Problem:** *kem* „wer" und *kelt* „was" existieren nur als Grundformen.

| | Option A: Kernwortmuster (-e- + Marker) | Option B: pronominales Muster (wie vim/vin/viş/vis) | Option C: indeklinabel |
|---|---|---|---|
| wer / wen / wem / wessen | kem / *kemen / kemeş / kemes* | kem / *kemn?* — Problem: \*kemn verletzt §5.3 nicht (mn ✓), aber die m/n-Folge kollidiert mit dem Pluralmarker-Klang; realistisch wäre kem/kemen wie A | „wen siehst du" wäre nur über Stellung lesbar — bricht das sonst konsequente Kasussystem |
| was / Akk | kelt / *kelten* oder unverändert kelt (wie dt. „was") | — | — |
| Kosten/Nutzen | konsistent mit §10.3 (kem klingt wie ein Kernwort); 6–8 neue Formen, alle phonotaktisch sauber (maschinell geprüft) | kaum Unterschied zu A in der Praxis | billig, aber systemfremd |
| Zusatz | *kelra/kella/kelna* deklinieren laut §18.2-Beispiel bereits adjektivisch — das sollte 0.9.4 als Regel aussprechen (heute nur Beispielpraxis; Test 080) | | |

---

## E5 · L-04 — Reflexivpronomen se (Tests 033, 035; 022/032/034 berührt)

**Problem:** *se* ist gelistet, hat aber weder Kasusformen noch einen definierten Personenbereich.

| | Option A: se indeklinabel, nur 3. Person | Option B: se voll dekliniert | Option C: se für alle Personen |
|---|---|---|---|
| „Er sieht sich" | *Ro milkat se* | *Ro milkat sen* | wie A/B |
| „Sie spricht über sich" | *Lo talat span se* (Kasus unsichtbar — nach span wäre Dat/Akk-Unterschied verloren) | *Lo talat span seş* | wie B |
| „Ich sehe mich" | *Vim milkam vin* (wie heute, Test 032 — 1./2. Person über Personalpronomen, deutsches Modell) | ebenso | *Vim milkam se(n)* — bricht mit dem deutschen Modell, spart aber Formen |
| Kosten/Nutzen | minimal; verliert Ort/Richtung-Unterschied nach Wechselpräpositionen | 3 neue Formen (sen/seş/ses — phonotaktisch sauber ✓); konsistent mit dem restlichen Pronominalsystem | größte Systemänderung, wenig Gewinn |

---

## E6 · L-05 — Agens im Passiv (Tests 137–138)

**Problem:** „vom Mann gebaut" ist nicht ausdrückbar.

| | Option A: ven + Dativ widmen | Option B: neue Agens-Präposition | Option C: kein Passiv-Agens |
|---|---|---|---|
| „Das Haus wird vom Mann gebaut" | *Xna breun şunargat ven xraş valruş* | *Xna breun şunargat PREP xraş valruş* (Neuwort) | nur aktiv: *Xra valru nargat xnan breunen* |
| Kosten/Nutzen | null neue Wörter; ven „mit (Mittel/Begleitung)" bekommt eine zweite Funktion — Mehrdeutigkeit „mit dem Mann/durch den Mann" entsteht | sauberste Semantik; einziges echtes Neuwort dieser Runde (Funktionswort — der Freeze erlaubt Ergänzungen bei „grammatischer Inkonsistenz", das hier ist eine) | ehrlich, aber ungewöhnlich einschränkend; Übersetzungstests scheitern weiter |

---

## E7 · L-09 — Silbifizierungsregel (für die Tastatur: Keyboard-P1)

**Problem:** 77/281 Grundformen mehrdeutig zerlegbar; ohne Präferenzregel kein deterministischer Manus-Composer.

**Simulationsergebnis (`--sim-l09`, alle 281 Grundformen):**

| Kandidat | löst eindeutig | Fehlschläge |
|---|---|---|
| **Variante A** — Diphthong-Vorrang + Onset-Maximierung (§5.2-Cluster bevorzugt) | **280/281, davon alle 77 mehrdeutigen** | nur *suvr-* (gebundene Wurzel; als Wortform existiert ohnehin nur *Suvre!*) |
| **Variante B** — Diphthong-Vorrang + Minimal-Onset (1 Konsonant, Rest Coda) | 279/281 | *suvr-* und ⚠ *taivbreun* (Restcoda „vb" unzulässig — B bräuchte eine Kompositionsfugen-Ausnahme) |

**Die 10 Formen, in denen A und B verschieden entscheiden** (nur hier ist die Wahl hörbar/schreibbar):

| Wort | A (Onset-Max) | B (Minimal-Onset) |
|---|---|---|
| velkra / velkran | vel·kra | velk·ra |
| zaldre | zal·dre | zald·re |
| kavla | ka·vla | kav·la |
| drovna | dro·vna | drov·na |
| vresto | vre·sto | vres·to |
| melisto / talisto | me·li·sto | me·lis·to |
| nestuma | ne·stu·ma | nes·tu·ma |
| luivresto | lui·vre·sto | luiv·res·to |
| taivbreun | taiv·breun | — (scheitert) |

**Bewertungshilfe ohne Festlegung:** A ist technisch vollständig und entspricht der sprachwissenschaftlichen Standardannahme (Onset-Maximierung); B respektiert Morphemgrenzen optisch besser (kav-la, drov-na), scheitert aber an Komposita und bräuchte Zusatzregeln. Ein Mittelweg wäre A mit einer Ausnahme „Kompositionsfuge bricht die Silbe" (taiv·breun statt tai·vbreun — A macht das ohnehin schon richtig, weil vb kein zulässiger Onset ist). Wichtig: Die Entscheidung gehört in §5 (Sprache), §26 (Manus) referenziert sie dann nur.

---

## E8 · Sonderfall velkran (Phase 7) — einziger Kandidat für eine Wortschatzänderung

**Problem:** *velkran* „Freundschaft" (Nominativ) ist formgleich mit *velkran* = Akkusativ von *velkra* „Freund". Exakte Kollision im selben semantischen Feld; der Freeze erlaubt Änderungen ausdrücklich bei „Kollision".

| | Option A: belassen + Artikelpflicht | Option B: Freundschaft umbilden | Option C: 10-%-Wort regularisieren |
|---|---|---|---|
| Mechanik | Kollision nur artikellos; Regel: Abstrakta der 10-%-Gruppe stehen nie artikellos im Objekt | z. B. über das reguläre Abstraktum *velkuma*? — ⚠ Achtung: §21.1-Suffix -uma existiert bereits produktiv; *velkrauma/velkuma* wären Neubildungen (Freeze-Bruch, Designer-Sache) | *velkran* → reguläres Nomen (z. B. *velkrana*?) — ebenfalls Freeze-Bruch |
| Kosten | null Wortänderung, eine Stilregel | historische 10-%-Klasse verliert ihr Paradebeispiel (§10.1 nennt velkran als Beispiel!) | wie B |
| Prüfstand-Hinweis | Die Kollision ist real, aber durch Artikel praktisch immer auflösbar; sie ist der einzige Fall dieser Schärfe im gesamten Lexikon | | |

---

## Redaktionskorrekturen (keine Designentscheidungen — können in 0.9.4 einfach durchgeführt werden)

| ID | Korrektur | Aufwand |
|---|---|---|
| K-01 | §5.1-Liste um VK, VKK, KKVKK ergänzen (kein Wort ändert sich; legalisiert aul, eird, est, ain, oñ, granz, trelm, vresn, skirm, prilm, prens-, dremn-, vlent-) | 1 Zeile + Beispielabsatz |
| K-03 | telnxelmmern → telnxelmern ODER Zahlenkomposita von §21.4 ausnehmen | 1 Wortform bzw. 1 Satz |
| K-04 | §25.1-Satz auf *tolmun* korrigieren ODER Ausnahme formulieren | 1 Wort |
| U-01 | §15.2-Beschreibung an die (korrekten) Tabellen anpassen (es- suppletiv; nu-/vur-Präsens) | 1 Absatz |
| U-10 | §26.8: „19 Konsonantentasten + 1 Vokalträgertaste" | 1 Halbsatz |
| U-14 | §18.3-Beispiel: *vna breun* → *vnan breunen* (oder Regel benennen) | 1 Beispiel |
| K-02 | killa/dolla/kella: als Ausnahme markieren ODER zu kila/dola/kela regularisieren — GRENZFALL: eigentlich Designentscheidung, da Formänderung | Designer entscheiden |

**Nach den Entscheidungen:** 0.9.4 schreiben (Designer) → `orbis_validator.py` nachziehen (Prüfstand) → Regressionslauf: 150 Tests + 360er-Matrix + `--strict` mit aktualisierter Baseline → die 20 offenen Tests müssen [OK] werden → dann 1.0-RC.

*Erstellt vom Prüfstand als Entscheidungsgrundlage; alle hypothetischen Formen sind maschinell auf Phonotaktik geprüft, aber NICHT kanonisch.*
