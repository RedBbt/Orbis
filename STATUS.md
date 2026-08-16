# ORBIS — STATUS

**Stand:** 2026-08-16
**Aktuelle Phase:** Phase A — Infrastruktur und Migration
**Referenz:** `Orbis-Grammatik-0.9.3.md` (READ ONLY, eingefroren, während der Migration nicht änderbar)
**Gesamturteil Testbericht 0.1:** NOT READY für einen direkten Sprung auf 1.0 — kein P0, sechs P1-Probleme, alle additiv lösbar

Diese Datei fasst den Projektzustand auf einen Blick zusammen. Alle Zahlen sind
unverändert aus `Orbis-Testbericht-0_1.md`, `Orbis-Validator-Bericht-0_1.md` und
`Orbis-Manus-Schreibtest-0_1.md` übernommen. Bei Abweichung gelten die Quelldokumente.

---

## 1. Kanonische Versionen

| Komponente | Version | Zustand |
|---|---|---|
| Orbis Grammar | 0.9.3 | eingefroren (READ ONLY) |
| Orbis Lexicon | 0.1 | in Migration nach `language/lexicon/` |
| Orbis Manus | 0.x | Schriftsystem, noch ohne Freigabeversion |
| Orbis Keyboard | 0.x | noch ohne Freigabeversion |
| Orbis Corpus | 0.1 | `Orbis-Testkorpus-0_1.md`, 150 Tests |
| Orbis Tools | 0.2 | `orbis_validator.py` + `orbis_baseline.json` |

Die vier bzw. sechs Stränge werden getrennt versioniert und dürfen nicht zusammengelegt werden.

---

## 2. Stabile Bereiche (mit Beleg)

Gemeinsame maschinelle Grundlage: Validator-Lauf D — **130 von 130 bildbaren Orbis-Sätzen
ohne automatischen Befund**; kein Satz enthält eine unbekannte Wortform, einen
Phonotaktikverstoß jenseits K-01, eine Geminate, einen Präpositionskasus-Fehler oder
eine NP-Inkongruenz.

| Bereich | Beleg |
|---|---|
| 45 Nomenendungen, volle Kasus-/Numerus-Matrix | 360 Formen (45 Endungen × 8) maschinell erzeugt und §5-geprüft, alle konform — Testkorpus Anhang 1, Validator-Bericht §5, `--tables` |
| Vier Kasus (Nominativ, Akkusativ, Dativ, Genitiv) | Korpusblöcke A (001–020), B (021–035), C (036–045); 0 automatische Befunde |
| Artikel (bestimmt/unbestimmt, Genus, Numerus, Kasus) | Validator-Prüfung 7 (§11) über den gesamten Formenbestand: 0 Treffer |
| Adjektivkongruenz | Korpusblock D (046–060) plus NP-Kongruenzheuristik: 0 Treffer; der einzige je gefundene Kongruenzfehler stammt aus dem archivierten Chat-Entwurf (Satz 48) und ist in der Prüffassung korrigiert |
| Reguläre Verben, 6 Personen × 3 Zeiten | Testkorpus Anhang 2 (Verbparadigmen), Validator-Prüfung 9: Wurzel + Tempusvokal + Personendung durchgängig konform |
| Die 8 unregelmäßigen Verben | Korpusblöcke J (116–125, Vergangenheit) und K (126–135, Zukunft), Stresstest J; Validator-Prüfung 10 gegen die belegten Tabellen: 0 Treffer |
| Kernwortdeklination (15 Kernwörter, Sonderklasse -e-/-ei) | Validator-Prüfung 6: 0 Treffer |
| V2-Stellung | Korpusblock A (001–020), manuell geprüft: 0 Beanstandungen |
| Verbklammer im Hauptsatz | Korpusblock I (106–115, Modalverben), manuell geprüft: 0 Beanstandungen |
| Negation | Korpusblock G (081–090): 0 Beanstandungen |
| Passivbildung ohne Agens | Korpusblock L (136–140), Stresstest E; nur das Agens selbst ist offen (L-05) |
| mai-Konditional | Korpusblock M (141–145): 0 Beanstandungen |
| Präpositionskasus | Validator-Prüfung 11 (§19), teilautomatisch über Folge-Artikel/-Pronomen: kein Kasusfehler in den 130 bildbaren Sätzen |

Zusätzlich maschinell bestätigt: kein reguläres Nomen trägt eine falsche Endung, und
kein Geschlecht widerspricht seiner Endung (0 Treffer über alle 281 Grundformen,
inklusive der §24.6-Abstrakta).

---

## 3. Offene Bereiche nach Priorität

Prioritätsschema: P0 = verhindert grundlegende Kommunikation · P1 = wichtige Konstruktion
fehlt · P2 = seltene/fortgeschrittene Konstruktion unklar · P3 = Dokumentations-/
Formulierungsproblem · P4 = rein stilistisch.

**Es gibt keinen P0-Befund.** Grundlegende Kommunikation — Aussage, Frage, Negation,
drei Zeiten, Modalität im Hauptsatz, Passiv ohne Agens, Konditional — funktioniert durchgängig.

### 3.1 P1 — wichtige grammatische Konstruktionen (6)

| ID | Kurzname | Befund | Betroffene §§ | Tests |
|---|---|---|---|---|
| L-01 | Genitivstellung | Die Stellung des Genitivattributs ist nicht geregelt, und die Stapelung von Genitiv und Possessiv bleibt offen. | §8, §13.3, §17 | 036, 039 |
| L-02 | Relativsatz | Der Relativsatzbau fehlt vollständig; fai trägt weder Kasus noch Kongruenz noch eine festgelegte Verbstellung und ist homonym mit fai „dass". | §13.4, §17.2, §20 | 100, 101, 102, 149 |
| L-03 | Fragewortkasus | kem und kelt existieren nur in der Grundform, sodass „wen/wem/wessen" nicht bildbar ist. | §18.2 | 074, 075, 076 |
| L-04 | Reflexivpronomen | Das Reflexivum se hat keine Kasusformen, und sein Personenbereich ist unklar. | §13.4 | 033, 035 |
| L-05 | Passiv-Agens | Das Agens im Passiv ist nicht ausdrückbar. | §16.3, §19 | 137, 138 |
| K-05 | Modalverb im Nebensatz | §16.1 (Infinitiv am Satzende) und §17.2 (finites Verb am Ende) beanspruchen dieselbe Position; bei Negation ist zusätzlich die Stellung von xa offen. | §16.1 ↔ §17.2, §18.3 | 103, 105 |

Alle sechs sind additiv lösbar: je eine klar umrissene Designentscheidung, keine kollidiert
mit bestehenden Regeln, keine erfordert neue Wörter außer gegebenenfalls L-05 und W-01.

### 3.2 P2 — fortgeschrittene Konstruktionen (9)

- **L-06** — Deklination der Demonstrativa (kilra…) und Indefinita (kelsu, xakaun…) fehlt (§13.4).
- **L-07** — Plural der 10-Prozent-Gruppe (velkran, soralm, prilm) nicht bildbar (§10.1, §9).
- **L-08** — Syntax der Kardinalzahlen: Kongruenz, Numerus, Artikel ungeregelt (§24.8, §9; Test 070).
- **L-09** — Keine Silbifizierungs-Präferenzregel; erzeugt die Manus-/Tastatur-Mehrdeutigkeit (§5, §26).
- **U-02** — Attributives Partizip („das gefundene Buch") ungeregelt (§12, §14, §16.3; Test 051).
- **U-03** — Modalverb ohne Infinitiv („Ich mag das Wort") ungeregelt (§16.1; Test 111).
- **U-04** — Pro-Drop: Subjektpronomen fehlen in §18-Fragen, nie in Aussagesätzen; Regel fehlt (§18, §13.1).
- **U-08** — Deklinationsklasse von Komposita mit Kernwort-Kopf (taivbreun) offen (§21.3, §10).
- **W-01** — Wortschatzlücken für Grundkommunikation: „sagen", „zeigen", „suchen", Existenzkonstruktion „es gibt" (§24; Test 104).

### 3.3 P3 — Dokumentation und Formulierung (15)

- **K-01** — §5.1-Silbenformenliste ohne VK/VKK/KKVKK, obwohl eingefrorener Wortschatz und grammatikeigene Beispiele diese Formen brauchen (aul, eird, est, granz, trelm, vresn, skirm, prilm …).
- **K-02** — killa/dolla/kella(n) verletzen die Fugenregel §21.4 (l+l unverschmolzen).
- **K-03** — telnxelmmern trägt m+m gegen §21.4 (§24.8).
- **K-04** — §25.1 nutzt tolm adverbial statt tolmun (§12.4; Test 060).
- **U-01** — §15.2-Formel deckt es- (suppletiv) und die Kontraktionspräsentia nu-/vur- nicht.
- **U-05** — Objektreihenfolge Dativ vor Akkusativ ist nur Beispielpraxis, keine Regel (§17).
- **U-06** — Kasus nach kon/zil ungeregelt; die Beispiele zeigen Nominativ (§12.3).
- **U-07** — „Konjunktionen systematisch aus Präpositionen + -i" stimmt nur für 4 von 7 (§20).
- **U-09** — „Echovokal" ist nur über Tabellen definiert, nicht ausformuliert (§9).
- **U-10** — §26.8 spricht von „20 Konsonantentasten"; korrekt sind 19 Konsonanten + 1 Vokalträger.
- **U-11** — Temporaler Dativ ohne Präposition (Vraş zaldreş) ungeregelt (§25.2 ↔ §8, §19).
- **U-12** — Imperativ-Stütz-e prüft nur §5.3; Dremn!/Prens!/Vlent! hätten KKVKK-Form (hängt an K-01).
- **U-13** — Prädikativ steht in allen Beispielen vor dem Verb (Lo loşn est = V3); Verhältnis zur V2-Regel ungesagt (§12.2 ↔ §17.1).
- **U-14** — §18.3-Beispiel „Vim xa num vna breun" lässt das Objekt unmarkiert; regelkonform wäre vnan breunen (aus der P3/P4-Restliste des Testberichts).
- **L-10** — Strichstärke für f s ş x v z j ç undefiniert; 9 von 19 Konsonantenklassen nicht erfasst (§26.9).

---

## 4. Komponentenstatus

| Komponente | Status | Anmerkung |
|---|---|---|
| Grammatik | stabil | 0.9.3 eingefroren; regulärer Morphologiekern widerspruchsfrei; 6 P1-Entscheidungen stehen aus |
| Lexikon | im Aufbau | 281 Grundformen belegt; Migration nach `language/lexicon/` mit ID-System ORB-LEX-…; W-01 offen |
| Korpus | stabil | 150 Tests, reproduzierbar über `--corpus Orbis-Testkorpus-0_1.md`; Migration nach `language/corpus/` läuft |
| Validator | stabil | `orbis_validator.py` mit 12 Prüfungen, Baseline 39 bekannte Befunde, Selbstvalidierung gegen Positiv- und Negativproben bestanden |
| Manus | blockiert | blockiert durch L-09 (fehlende Silbifizierungs-Präferenz): 77 von 281 Grundformen mehrdeutig zerlegbar; zusätzlich L-10 und U-10 offen |
| Keyboard | geplant | setzt eine Entscheidung zu L-09 voraus; keine eigene Regelbasis vor Manus-Freigabe |
| Doku | im Aufbau | Migration in `docs/de/`, `docs/en/`, `docs/decisions/`, `reports/`; Deutsch ist Primärsprache und semantische Autorität, Englisch abgeleitete Zweitsprache |
| CI | aktiv | `.github/workflows/orbis-ci.yml`; Regressionslauf `--strict` gegen `orbis_baseline.json`, Exit-Code 1 bei neuen Befunden |

---

## 5. Kennzahlen-Baseline

| Kennzahl | Wert | Quelle |
|---|---|---|
| Tests insgesamt | 150 | Testbericht 0.1, Phase 5 |
| [OK] | 130 | Testbericht 0.1, Phase 5 |
| [REGELLÜCKE] | 14 | Tests 033, 035, 036, 039, 070, 074, 075, 076, 100, 101, 102, 137, 138, 149 |
| [REGELKONFLIKT] | 3 | Tests 060, 103, 105 |
| [REGELUNKLARHEIT] | 2 | Tests 051, 111 |
| [TESTPROBLEM] | 1 | Test 104 |
| Stabilitätsquote | 86,7 % | 130 / 150 |
| Grundformen im Wortschatz | 281 | Manus-Schreibtest 0.1, Abschnitt 2 |
| Manus-Ambiguitäten | 77 | 77 von 281 mehrdeutig zerlegbar (27 %); 203 eindeutig, 1 nicht zerlegbar (bloße Wurzel suvr-) |
| Bekannte Validator-Befunde in der Baseline | 39 | `orbis_baseline.json` |

Ergänzende Kennzahlen aus denselben Quellen: Die 20 Nicht-OK-Tests gehen auf nur
11 unterschiedliche Probleme zurück (L-01, L-02, L-03, L-04, L-05, L-08, K-04, K-05,
U-02, U-03, W-01). Hinzu kommen 19 nicht korpuswirksame Befunde; Gesamtinventar
30 Befunde plus die Phase-7-Wortschatzliste. Von den 71 Beispielsätzen der Grammatik
sind 54 ohne Befund; die 17 Treffer gehen ausnahmslos auf K-01, K-02 und K-03 zurück.
360 [TESTFORM]-Deklinationsformen wurden maschinell erzeugt und sind sämtlich §5-konform.

---

## 6. Was auf wen blockiert ist

Alle folgenden Punkte sind **Designerentscheidungen**. Claude Code dient in diesem Repo
ausschließlich als Prüf- und Werkzeug-Assistent und trifft keine Sprachentscheidungen;
Befunde werden markiert, nicht per Interpretation repariert.

| Blockierter Punkt | Wartet auf | Wirkung der Entscheidung |
|---|---|---|
| Grammar 0.9.4 | Entscheidung der Sprachdesigner zu den 6 P1-Befunden (L-01, L-02, L-03, L-04, L-05, K-05) | Ohne sie bleibt das Urteil NOT READY; mit ihnen werden die 20 offenen Tests bearbeitbar |
| Manus-Freigabe | Entscheidung zu L-09 (Silbifizierungs-Präferenz, z. B. Onset-Maximierung + Diphthong-Vorrang) | Löst die 77 mehrdeutigen Grundformen und entblockt die Rückübertragung aus der Lateinschreibung |
| Manus-Strichstärken | Entscheidung zu L-10 (Strichstärke für die 8 Reibelaute und die Affrikate) | Vervollständigt §26.9 |
| Keyboard 0.x | Manus-Freigabe (L-09, L-10) | Erst danach ist ein belastbares Tastaturlayout definierbar |
| Redaktionelle 0.9.4-Fixes | Entscheidung zu K-01, K-03, K-04, U-01, U-10 | Reine Dokumentationskorrekturen, kein Wort und keine Form ändert sich |
| Wortschatzerweiterung | Entscheidung zu W-01 („sagen", „zeigen", „suchen", „es gibt") und ggf. L-05 | Einzige Punkte, die neue Wörter erfordern könnten; ohne Auftrag werden keine Wörter erfunden |
| Baseline-Aktualisierung | Ausdrücklicher Auftrag | `--update-baseline` wird nur nach Rücksprache ausgeführt |

Vorlage für die anstehenden Entscheidungen: `decisions/Entscheidungsvorlage-0_9_4.md`.

Empfohlener Weg laut Testbericht 0.1: die 6 P1-Entscheidungen treffen, als 0.9.4 nachtragen
(zusammen mit den redaktionellen P3-Fixes), Regressionslauf dieses Testkorpus; bei
mindestens 95 % ohne neue Befunde ist ein 1.0-RC realistisch. Die P2-Befunde können
nach 1.0 als dokumentierte offene Punkte weiterlaufen.

---

*Reproduktion der Kennzahlen: `python3 orbis_validator.py --all`, `--corpus Orbis-Testkorpus-0_1.md`,
`--manus`, `--tables`, `--strict`. Claude Code dient in diesem Repo als Prüfwerkzeug.*
