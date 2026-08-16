# ROADMAP — Orbis, Phasen A bis K

Diese Roadmap ordnet die Arbeit am Projekt ORBIS in elf Phasen. Sie beschreibt, was in
welcher Reihenfolge entsteht, woran der Abschluss einer Phase erkennbar ist und wer
zuständig ist.

Die Roadmap ist ein Planungsdokument, keine Sprachquelle. Sie legt keine Sprachregel
fest, ändert keine Grammatikversion und ersetzt keine Entscheidung. Maßgeblich bleiben
`Orbis-Grammatik-0.9.3.md` (READ ONLY), `ORBIS_CONSTITUTION.md`, `VERSIONING.md` und die
Entscheidungen (ADR) unter `docs/decisions/`.

Die Roadmap nennt bewusst keine Termine. Phasen sind über Abschlusskriterien und
Abhängigkeiten geordnet, nicht über Datumsangaben.

---

## Rollen und Notation

| Kürzel | Rolle | Befugnis |
|---|---|---|
| **SD** | Sprachdesigner | Entscheiden über Sprache, Schrift, Bedeutung, Wortschatzaufnahme, Versionssprünge und Freigaben. Einzige Instanz, die Regellücken und Regelkonflikte schließt. |
| **PW** | Prüfstand / Werkzeug | Migration, Datenmodell, Validator, Tests, CI, Berichte, Generierung. Markiert Befunde, liefert Optionen und Messwerte, entscheidet nichts. Claude Code dient dem Projekt in dieser Rolle als Prüfwerkzeug. |

Ist eine Aufgabe mit **SD+PW** ausgezeichnet, liefert der Prüfstand die Grundlage und die
Sprachdesigner entscheiden bzw. geben frei.

### Statuswerte

| Status | Bedeutung |
|---|---|
| LAUFEND | Arbeit hat begonnen, Abschlusskriterien noch nicht erfüllt |
| GEPLANT | Vorbereitet, Start hängt an den genannten Abhängigkeiten |
| BLOCKIERT | Start setzt eine noch offene Entscheidung voraus |
| LANGFRISTIG | Beginnt ausdrücklich erst nach Grammar 1.0 |

---

## Übersicht

| Phase | Thema | Status | Hauptabhängigkeit | Zuständig |
|---|---|---|---|---|
| A | Infrastruktur (Datenmodell, Governance, Migration, CI) | LAUFEND | — | PW, Freigaben SD |
| B | Grammatik 0.9.4 — Entscheidungen | GEPLANT | A | SD |
| C | Regression gegen 0.9.4 | GEPLANT | B | PW |
| D | Grammar 1.0 RC | GEPLANT | C | SD+PW |
| E | Lexikon-Ausbau (gestuft) | LAUFEND (Stufe E-1) | A; ab E-2 auch B/C | SD+PW |
| F | Manus 1.0 | BLOCKIERT (L-09, L-10) | A | SD+PW |
| G | Keyboard | BLOCKIERT (Manus-Fassung) | F | PW, Belegung SD |
| H | Learning (Lernstufen, Lernkorpus) | GEPLANT | D, E-2 | SD+PW |
| I | Audio (Aussprache, IPA) | GEPLANT | D | SD+PW |
| J | Scholar/AI (Analyse, Wortgraph) | GEPLANT | A | PW |
| K | Dialekte und Kultur | LANGFRISTIG | D, E, F | SD |

Ausgangsstand (Stabilitätstest 0.1): 150 Tests gegen Grammatik 0.9.3 — 130 OK,
14 REGELLÜCKE, 3 REGELKONFLIKT, 2 REGELUNKLARHEIT, 1 TESTPROBLEM, Stabilitätsquote
86,7 %. Kein P0-Befund, 6 P1-Befunde, alle additiv lösbar. Urteil: NOT READY für einen
direkten 1.0-Sprung.

---

## Phase A — Infrastruktur

**Status: LAUFEND**

### Ziel

Ein gewachsenes Dokumentenrepository wird in eine strukturierte, maschinenlesbare
Datenbasis mit verbindlicher Governance überführt. Phase A ändert die Sprache nicht:
alles, was hier entsteht, ist Abbild bestehender Regeln.

### Arbeitspakete

- Zielverzeichnisse anlegen und befüllen: `language/` (metadata, phonology, morphology,
  syntax, lexicon, proto, corpus, findings), `script/` (manus, magna, traces), `tools/`
  (validator, lexicon, corpus, documentation, migration), `tests/`, `docs/de`, `docs/en`,
  `docs/decisions`, `reports/`, `archive/`, `keyboard/`.
- Bestehende Regeln aus der Grammatik 0.9.3 nach `language/*.json` extrahieren
  (Phonologie, Morphologie, Syntax, Proto) — Abbild, keine neue Regel.
- Lexikonbestand nach `language/lexicon/entries/*.json` überführen, mit `index.json`,
  `word_families.json` und Konzeptdatei.
- Testkorpus 0.1 und die Grammatikbeispiele nach `language/corpus/` überführen.
- Befunde K-01…K-05, L-01…L-10, U-01…U-14, W-01 nach `language/findings/findings.json`
  mit Schema überführen; Befund-IDs unverändert lassen.
- ID-System einführen: `ORB-LEX-`, `ORB-CON-`, `ORB-SENT-`, `ORB-GRAM-PHON/MOR/SYN-`,
  `ORB-MANUS-`, `ORB-ADR-`, `ORB-FIND-`.
- Governance schreiben und in Kraft setzen: `ORBIS_CONSTITUTION.md`, `VERSIONING.md`,
  `TRANSLATION_POLICY.md`, `AGENTS.md`, `CONTRIBUTING.md`, `CLAUDE.md`,
  `AI_START_HERE.md`, `ROADMAP.md`, Statusübersicht.
- Sprachpolitik verankern: Deutsch als PRIMARY LANGUAGE und semantische Autorität,
  Englisch als SECONDARY OFFICIAL DOCUMENTATION LANGUAGE mit Übersetzungsstatus
  (`missing`, `draft`, `derived`, `reviewed`).
- Messstand vor der Migration sichern: `reports/baseline/` mit Validator-Läufen und
  Prüfsummen; nachträglich nicht anpassen.
- Validator modularisieren (`tools/validator/`); die bekannte Migrationsschuld
  (Sprachdaten als Python-Konstanten) benennen und nicht vermehren.
- CI erweitern: `--strict` gegen `orbis_baseline.json`, Korpuslauf, Schemaprüfung der
  JSON-Dateien unter `language/`.
- Bestand und Archiv trennen: historische Fassungen nach `archive/` (grammar, corpus,
  audits, reports), Archiv nie als aktuelle Quelle.

### Abschlusskriterien

- Alle in `AGENTS.md` Abschnitt 2.1 genannten Verzeichnisse existieren und enthalten
  echte Inhalte; keine leeren Platzhalterdateien.
- Jede Regel, jedes Lexem, jeder Testfall und jeder Befund aus den Wurzeldokumenten hat
  genau eine maschinenlesbare Entsprechung mit ID.
- `python3 orbis_validator.py --strict` endet mit Exit-Code 0 gegen die 39 bekannten
  Befunde; `--corpus Orbis-Testkorpus-0_1.md` reproduziert 130 OK und 86,7 %.
- `Orbis-Grammatik-0.9.3.md` ist byte-identisch zum Stand vor der Migration
  (Prüfsummenvergleich gegen `reports/baseline/`).
- Die verbliebene Migrationsschuld ist als Liste dokumentiert (welche Sprachdaten noch
  im Werkzeugcode liegen und wohin sie gehören).
- README, `AI_START_HERE.md`, `CLAUDE.md` und `AGENTS.md` verweisen auf die neue
  Struktur; kein toter Verweis.

### Abhängigkeiten

Keine. Phase A ist Voraussetzung für alle folgenden Phasen, weil Datenmodell, IDs,
Baseline und CI die Grundlage jeder späteren Regressionsaussage sind.

### Zuständig

PW für Migration, Werkzeuge, Schemata und CI. SD für die Freigabe der
Governance-Dokumente, der Sprachpolitik, der ID-Konventionen und für die ausdrückliche
Erklärung, wann `language/*.json` Source of Truth wird.

---

## Phase B — Grammatik 0.9.4: Entscheidungen

**Status: GEPLANT — Zuständigkeit Sprachdesigner**

### Ziel

Die sechs P1-Befunde des Stabilitätstests werden entschieden und zusammen mit den
Redaktionskorrekturen in eine neue Grammatikversion 0.9.4 überführt. Die 0.9.3 bleibt
unverändert bestehen.

### Arbeitspakete

- Entscheidung zu **L-02** (Relativsatz): `fai` indeklinabel, `fai` dekliniert oder
  eigenes Relativwort; Folgen für §13.4 und §17.
- Entscheidung zu **K-05** (Modalverb im Nebensatz): Infinitiv vor Finitum oder Finitum
  vor Infinitiv — einschließlich der Position von `xa` im Endfeld (§17.2, §18.3), sonst
  bleibt der zugehörige Testfall offen.
- Entscheidung zu **L-01** (Stellung des Genitivattributs): Nachstellung normieren oder
  beide Stellungen zulassen; Stapelung von Genitiv und Possessiv mitentscheiden.
- Entscheidung zu **L-03** (Deklination der Fragewörter): Kernwortmuster, pronominales
  Muster oder indeklinabel. Mitzuentscheiden ist, ob die adjektivische Kongruenz von `kel-`,
  die §18.2 bisher nur an einem Beispiel zeigt, als Regel ausgesprochen wird.
- Entscheidung zu **L-04** (Reflexivpronomen `se`): indeklinabel, voll dekliniert oder
  für alle Personen.
- Entscheidung zu **L-05** (Agens im Passiv): eine bestehende Präposition mit einer
  Zweitfunktion betrauen (der Testbericht nennt `ven` + Dativ als Beispiel, nicht als Vorgabe),
  eine eigene Agens-Präposition schaffen oder auf ein Passiv-Agens verzichten.
- Redaktionskorrekturen entscheiden: K-01, K-03, K-04, U-01 sowie U-10 (§26.8 nennt
  fälschlich „20 Konsonantentasten"; korrekt sind 19 Konsonanten und 1 Vokalträger).
- Grenzfälle K-02 und U-14 entscheiden, deren Korrekturform von den Entscheidungen oben
  abhängt.
- Für jede Entscheidung einen ADR `ORB-ADR-xxxx` unter `docs/decisions/` anlegen:
  Frage, Optionen, Entscheidung, Begründung, betroffene Paragraphen, Folgeänderungen.
- `Orbis-Grammatik-0.9.4.md` als **neue Datei** schreiben; 0.9.3 nie überschreiben.
- CHANGELOG-Eintrag und Vorbereitung der Kompatibilitätsmatrix nach `VERSIONING.md` §7.
- Prüfstand: Entscheidungsvorlage `decisions/Entscheidungsvorlage-0_9_4.md` aktuell
  halten, Formenkandidaten phonotaktisch prüfen, Folgen für `language/*.json` und den
  Validator abschätzen — ohne vorzugreifen.

### Abschlusskriterien

- Für alle sechs P1-Befunde (L-01, L-02, L-03, L-04, L-05, K-05) existiert je ein
  entschiedener ADR mit benannten Folgeparagraphen.
- Die Redaktionskorrekturen samt K-02 und U-14 sind entschieden oder ausdrücklich mit
  Begründung vertagt.
- `Orbis-Grammatik-0.9.4.md` existiert; die Prüfsumme von `Orbis-Grammatik-0.9.3.md` ist
  unverändert.
- Kein Befund wurde per Interpretation geschlossen; was offen bleibt, bleibt als Befund
  markiert.
- Neu eingeführte Funktionswörter (etwa ein Relativwort oder eine Agens-Präposition)
  erfüllen Phonologie und Phonotaktik und haben vollständige Lexikoneinträge.

### Abhängigkeiten

Phase A (ADR-Ablage, Befund-IDs, maschinenlesbare Befundliste). **L-09 und L-10 gehören
nicht in diese Phase** — sie betreffen die Schrift und werden in Phase F entschieden.

### Zuständig

SD entscheidet. PW liefert Optionen, Kosten-Nutzen-Gegenüberstellungen, phonotaktische
Prüfung möglicher Formen und Auswirkungslisten; PW entscheidet nichts und formuliert
keine Empfehlung als Festlegung.

---

## Phase C — Regression gegen 0.9.4

**Status: GEPLANT**

### Ziel

Maschinell nachweisen, dass die 0.9.4 die entschiedenen Befunde tatsächlich schließt und
keine neuen erzeugt. Ohne bestandenen Regressionslauf gilt kein Versionswechsel.

### Arbeitspakete

- `language/*.json` und Validator auf 0.9.4 nachziehen — ausschließlich entlang
  entschiedener ADRs, ohne eigene Auslegung.
- Testkorpus 0.1 unverändert gegen 0.9.4 fahren und die Bewertung jedes betroffenen
  Tests neu setzen.
- Testkorpus um Fälle zu den sechs Entscheidungen erweitern (Korpus 0.2), einschließlich
  der bisher nicht ausdrückbaren Sätze (etwa Relativsatz im Dativ, Passiv mit Agens).
- Die Deklinationsmatrix erneut erzeugen und prüfen: 45 Endungen × 8 Formen = 360
  Formen über alle Kasus und Numeri, §5-Konformität.
- Vollläufe `--all`, `--lexicon`, `--examples`, `--tables`, `--manus`, `--corpus`.
- Baseline neu schneiden (`--update-baseline`) nur nach ausdrücklichem Auftrag; die alte
  Baseline nach `reports/baseline/` archivieren.
- Validator-Bericht und Testbericht in neuer Fassung schreiben, Stabilitätsquote
  gegenüberstellen (Ausgangswert 86,7 %).
- Kompatibilitätsmatrix `VERSIONING.md` §7 fortschreiben.

### Abschlusskriterien

- Alle Tests des Korpus sind gegen 0.9.4 neu bewertet; jeder zu L-01…L-05 und K-05
  gehörende Fall steht auf OK oder hat eine benannte, begründete Restlücke.
- Die Stabilitätsquote ist dokumentiert und liegt über 86,7 %; keine neue Befundklasse
  ist entstanden.
- `--strict` endet mit Exit-Code 0 gegen die neu geschnittene Baseline; die CI ist grün.
- Alle 360 erzeugten Deklinationsformen sind §5-konform.
- Die Zeilen für Lexicon, Corpus und Tools zu Grammar 0.9.4 stehen in der
  Kompatibilitätsmatrix auf „geprueft", nicht auf „erwartet kompatibel".

### Abhängigkeiten

Phase B vollständig abgeschlossen. Ein Regressionslauf gegen eine halb entschiedene
Grammatik ist wertlos.

### Zuständig

PW führt aus und berichtet. SD bewertet verbliebene Restlücken und gibt einen
Baseline-Neuschnitt frei.

---

## Phase D — Grammar 1.0 RC

**Status: GEPLANT**

### Ziel

Aus einer stabilen 0.9.4 wird ein Release-Kandidat 1.0 geschnitten. Erst damit gilt die
Grammatik als Ganzes stabilisiert und wird zur Bezugsgröße für Lexikon, Schrift und
Lernmaterial.

### Arbeitspakete

- Restbestand der Unklarheiten U-01…U-14 durchgehen: entscheiden, vertagen oder
  ausdrücklich als bewusst offen dokumentieren.
- Vollständigkeitsprüfung: jede Paragraphenreferenz ist auflösbar, jedes Beispiel der
  Grammatik ist maschinell nachvollziehbar.
- Festlegen, ob und wann `language/*.json` Source of Truth wird und Markdown daraus
  generiert oder dagegen geprüft wird; der Übergang gilt nur nach ausdrücklicher
  Erklärung der SD.
- Freeze-Kriterien für 1.0 festlegen: was künftig einen Major-Sprung auslöst und was
  additiv bleibt.
- RC-Fenster: Einfrieren, Regressionslauf, ausschließlich Fehlerkorrekturen.
- Deutsche Fassung nach `docs/de/`, englische Fassung nach `docs/en/` ableiten;
  Übersetzungsstatus je Kapitel setzen.
- CHANGELOG, Versionsstände und Kompatibilitätsmatrix fortschreiben.

### Abschlusskriterien

- Kein P0- und kein P1-Befund ist offen; jede verbliebene Unklarheit trägt einen Status
  (entschieden, bewusst offen, vertagt mit Begründung).
- Zwei aufeinanderfolgende vollständige Regressionsläufe ohne neue Befunde.
- Alle Beispielsätze der Grammatik sind maschinell prüfbar und geprüft.
- Die 1.0-RC-Fassung liegt als neue Datei vor; 0.9.3 und 0.9.4 sind archiviert, nicht
  gelöscht oder verändert.
- Die englische Fassung ist mindestens als `derived` gekennzeichnet, inhaltlich aus der
  deutschen Fassung abgeleitet und ohne Bedeutungsverschiebung.

### Abhängigkeiten

Phase C. Phase D ist Voraussetzung für H, I und K.

### Zuständig

SD für Freigabe, Freeze-Kriterien und die Source-of-Truth-Erklärung. PW für Prüfläufe,
Vollständigkeitsprüfung, Generierung und Berichte.

---

## Phase E — Lexikon-Ausbau

**Status: LAUFEND (Stufe E-1)**

### Ziel

Der Wortschatz wächst gestuft und qualitätsgesichert. Jedes kanonische Wort hat einen
vollständigen Eintrag; Menge ist nie das Kriterium.

### Stufen

| Stufe | Umfang | Voraussetzung |
|---|---|---|
| E-1 | Bestehenden Wortschatz migrieren und vervollständigen | Phase A |
| E-2 | Kernlexikon: 500–1000 Lexeme | E-1, Phase B/C (stabile Flexionsregeln) |
| E-3 | Ausbau auf 3000+ Lexeme, domänenweise | E-2 |
| E-4 | Weiterer Ausbau, Fachwortschatz nach Bedarf | E-3, Grammar 1.0 |

### Arbeitspakete

- **E-1**: vorhandene Einträge auf Pflichtfelder prüfen und ergänzen (ORB-LEX-ID,
  Wortart, Flexionsklasse, deutsche kanonische Bedeutung, abgeleitete englische
  Bedeutung, Beispiel, Quelle); Konzepte (`ORB-CON`) und Wortfamilien pflegen; die
  Wortschatzlücke W-01 als Arbeitsvorrat führen.
- **E-2**: zuerst die Konzeptliste festlegen (welche Begriffe fehlen), dann Lexeme dazu
  entscheiden — nicht umgekehrt. Alltagsdomänen zuerst.
- **E-3**: Domäne für Domäne, je Domäne ein eigener Freigabeschritt und ein eigener
  Prüflauf.
- Querschnitt: Werkzeuge unter `tools/lexicon/` für Phonotaktikprüfung,
  Dublettenerkennung, Homonymie- und Minimalpaarreport, Wortfamilienkonsistenz.
- Querschnitt: Aufnahmeverfahren festlegen — Vorschlag, maschinelle Prüfung, Freigabe
  durch SD, Statuswechsel auf `canonical`.
- Querschnitt: Übersetzungsstatus je Eintrag pflegen; englische Bedeutung wird aus der
  deutschen abgeleitet und verändert sie nicht.
- Querschnitt: Lexicon-Versionssprünge nach `VERSIONING.md` §3.2 setzen.

### Abschlusskriterien (je Stufe)

- Jeder kanonische Eintrag hat vollständige Pflichtfelder, eine ORB-LEX-ID, mindestens
  ein zugeordnetes Konzept und eine geprüfte Phonotaktik.
- Keine unbeabsichtigte Dublette, keine unmarkierte Homonymie, keine Übernahme aus einer
  realen Sprache.
- Jeder Eintrag ist mit Proto-Orbis vereinbar oder als Ausnahme begründet; Synonyme sind
  semantisch gegeneinander abgegrenzt.
- `--lexicon` läuft ohne neue Befunde; die Zielmenge der Stufe ist erreicht oder die
  erreichte Teilmenge ist ausdrücklich als Stufenstand freigegeben.
- Die Freigabe je Domäne ist protokolliert.

### Abhängigkeiten

Phase A für das Datenmodell. Ab E-2 zusätzlich B und C, weil sonst jeder Eintrag nach
einer Grammatikentscheidung nachgezogen werden muss. Qualität hat Vorrang vor
Stufenerreichung: eine Stufe wird lieber unvollständig abgeschlossen als mit
ungeprüften Einträgen gefüllt.

### Zuständig

SD gibt jedes Konzept, jedes Lexem und jede Domäne frei. PW prüft, meldet und pflegt
Datensätze nach Freigabe; PW erzeugt keinen Wortschatz aus eigenem Antrieb.

---

## Phase F — Manus 1.0

**Status: BLOCKIERT — setzt die Entscheidung zu L-09 voraus**

### Ziel

Orbis Manus wird vom Konzept zu einer nummerierten, vollständig spezifizierten
Schriftfassung. Schrift und Grammatik bleiben dabei getrennte Ebenen.

### Arbeitspakete

- **L-09 entscheiden** (Silbifizierung). Die Simulation (`--sim-l09`) liefert Zahlen zu vier
  Kandidatenstrategien — Onset-Maximierung ohne Diphthong-Vorrang (280/281), Minimal-Onset mit
  Diphthong-Vorrang (279/281), Onset-Maximierung mit Diphthong-Vorrang (280/281), lexikalisch
  gespeicherte Grenzen (0/281, da §5 keine festlegt). Der Testbericht nennt zusätzlich die
  Möglichkeit, **freie Varianz zu erklären** und die Schrift mehrdeutig zu lassen.
  Die Auswahl ist offen und trifft ausschließlich der Sprachdesigner; die Sonderfälle `suvr-`
  und die Kompositionsfuge in `taivbreun` sind mitzuentscheiden.
- **L-10 entscheiden**: Strichstärke für `f`, `s`, `ş`, `x`, `v`, `z`, `j`, `ç`.
- **U-10 nachziehen**: §26.8 nennt 20 Konsonantentasten; korrekt sind 19 Konsonanten und
  1 Vokalträger. Die Korrektur erscheint in der jeweils gültigen Grammatikversion, nicht
  durch Änderung der 0.9.3.
- Glyphensatz unter `script/manus/glyphs/`: Zeichenliste mit `ORB-MANUS-`IDs,
  Formvarianten, Schreibrichtung, Referenzformen.
- Kompositionsregeln unter `script/manus/composition/`: Silbenblockbau, Diakritika,
  Interpunktion, Zahlzeichen.
- Spezifikation unter `script/manus/spec/`, Dokumentation in `docs/de/` und abgeleitet
  in `docs/en/`.
- Tests unter `script/manus/tests/`: Zerlegung des gesamten Grundformenbestands,
  Mehrdeutigkeitsreport, Regressionslauf.
- Die experimentelle Morphem-Ebene (sichtbare Kasus- und Tempuszeichen) bleibt
  ausdrücklich als EXPERIMENTAL gekennzeichnet und wird nirgends als bestehende
  Orbis-Grammatik dargestellt.

### Abschlusskriterien

- L-09 und L-10 sind als ADR entschieden; die §26.8-Korrektur ist nachgezogen.
- Die getroffene L-09-Entscheidung ist umgesetzt und ihre Folgen für den Grundformenbestand sind dokumentiert (bei einer Präferenzregel: eindeutige Zerlegung; bei erklärter freier Varianz: dokumentierte Mehrdeutigkeit); die 77 mehrdeutigen Fälle sind
  aufgelöst, verbleibende Ausnahmen sind einzeln benannt und begründet.
- Jedes Zeichen hat ID, Strichstärke, Schreibrichtung und Referenzform; kein Zeichen ist
  nur in Prosa beschrieben.
- Der Zerlegungstest läuft in der CI und ist grün.
- Manus liegt als nummerierte Fassung 1.0 vor; die Kompatibilitätsmatrix ist
  fortgeschrieben.

### Abhängigkeiten

Phase A. Fachlich unabhängig von B, C und D — ein Manus-Befund löst keinen
Grammatikschritt aus und umgekehrt. Der Lexikonstand aus Phase E bestimmt die Testmenge.
Phase F blockiert Phase G.

### Zuständig

SD entscheidet Silbifizierung, Strichstärke und Zeichenformen. PW liefert Simulationen
(`--sim-l09` ist ein Analysewerkzeug und nie eine Sprachregel), Zerlegungsreports und
Testautomatisierung.

---

## Phase G — Keyboard

**Status: BLOCKIERT — setzt eine nummerierte Manus-Fassung voraus**

### Ziel

Eine erste benutzbare Eingabemethode für Orbis Manus (MVP): tippen, silbisch setzen,
korrekt darstellen.

### Arbeitspakete

- Belegung unter `keyboard/` festlegen: 19 Konsonanten und 1 Vokalträger, Vokale und
  Diphthonge, Modifikatoren, Interpunktion, Zahlen.
- Verarbeitungskette umsetzen: **MorphologyEngine → Syllabifier → ManusComposer**. Jede
  Stufe liest ausschließlich aus `language/` bzw. `script/`; keine Regelkopie im Code.
- Referenzimplementierung mit Testsuite, insbesondere Rundlauftest: Eingabe → Manus →
  Rückzerlegung → Ausgangsform.
- Plattformfrage klären und für den MVP eingrenzen (Desktop-Belegung zuerst, mobile
  Eingabemethode später).
- Fehlerverhalten festlegen: was passiert bei phonotaktisch unzulässigen Eingaben.
- Die experimentelle Morphem-Ebene, falls sie überhaupt sichtbar wird, ausschließlich
  als abschaltbarer, klar markierter EXPERIMENTAL-Modus.

### Abschlusskriterien

- Jede Grundform des freigegebenen Lexikons ist tippbar und ergibt genau eine
  Manus-Darstellung.
- Der Rundlauftest läuft über den gesamten Lexikonbestand ohne Fehlschlag und ist Teil
  der CI.
- Die Keyboard-Fassung ist nummeriert und ausdrücklich gegen eine nummerierte
  Manus-Version freigegeben; die Kompatibilitätsmatrix nennt beide Stände.
- Eine Prüfung nach `AGENTS.md` 2.2 zeigt keine zweite Fassung einer Sprach- oder
  Zeichenregel im Werkzeugcode.

### Abhängigkeiten

Phase F (nummerierte Manus-Fassung, entschiedene Silbifizierung) und Phase A. Der
Lexikonstand aus Phase E bestimmt die Testmenge.

### Zuständig

PW baut, testet und dokumentiert. SD entscheidet Belegung, Zeichenzuordnung und ob
experimentelle Ebenen überhaupt sichtbar werden.

---

## Phase H — Learning

**Status: GEPLANT**

### Ziel

Orbis wird lernbar: gestufte Lernmaterialien und ein Lernkorpus, geordnet nach einer
Orbis-eigenen Stufenklassifikation A0 bis C2.

### Arbeitspakete

- Stufenmodell A0–C2 als **eigene Orbis-Klassifikation** definieren: Wortschatzumfang,
  Grammatikpensum, Textsorten und Kannbeschreibungen je Stufe. Die Bezeichnungen A0–C2
  sind projektintern belegt und werden nicht als Übernahme eines fremden
  Referenzrahmens dargestellt.
- Jedes Lexem und jede Grammatikregel einer Stufe zuordnen (Feld im Datenmodell).
- Lernkorpus aufbauen: Sätze und Texte je Stufe mit `ORB-SENT-`IDs, deutscher
  kanonischer Übersetzung und abgeleiteter englischer Fassung.
- Materialien generieren: Glossare, Flexionstabellen, Übungsformate je Stufe über
  `tools/documentation/`.
- Prüfwerkzeug: ein Lerntext darf nur Wortschatz und Regeln der eigenen und der
  darunterliegenden Stufen verwenden.

### Abschlusskriterien

- Das Stufenmodell ist als ADR verabschiedet und dokumentiert.
- Jede Stufe hat einen abgeschlossenen Wortschatz- und Regelumfang sowie ein
  Mindestkorpus an geprüften Texten.
- Die automatische Stufenprüfung läuft ohne Verstoß; kein Text verwendet Material über
  seiner Stufe.
- Deutsche Materialien sind vollständig, englische abgeleitet und im Status gekennzeichnet.

### Abhängigkeiten

Phase D (stabile Grammatik) und Stufe E-2 (Kernlexikon). Ohne stabile Regeln müsste
jedes Lernmaterial nach jeder Grammatikentscheidung neu geschrieben werden.

### Zuständig

SD definiert Stufen und gibt Texte frei. PW prüft Stufenkonformität, generiert Tabellen
und Glossare.

---

## Phase I — Audio

**Status: GEPLANT**

### Ziel

Die Aussprache wird verbindlich beschrieben und hörbar belegt.

### Arbeitspakete

- Aussprachenorm je Phonem, Diphthong und Cluster festlegen; offene Punkte der
  Phonologie ausdrücklich benennen statt zu füllen.
- IPA-Notation ergänzen, **sobald sie verbindlich entschieden ist** — vorher wird keine
  IPA-Angabe als Regel geführt.
- Betonungsregeln prüfen und in `language/phonology/stress.json` abbilden.
- Referenzaufnahmen erstellen: vollständiges Phoneminventar, Minimalpaare,
  Beispielsätze, später Lernstufentexte.
- Aussprachehinweis je Lexikoneintrag aus den Phonologiedaten generieren, nicht von Hand
  pflegen.

### Abschlusskriterien

- Jedes Phonem hat eine entschiedene Aussprachebeschreibung; das IPA-Feld ist gefüllt
  oder ausdrücklich als offen markiert.
- Referenzaufnahmen decken das vollständige Inventar und die Minimalpaare ab.
- Kein Aussprachedatum steht ohne Ableitung aus der entschiedenen Phonologie.
- Die Generierung der Aussprachehinweise läuft reproduzierbar aus `language/`.

### Abhängigkeiten

Phase D für die stabile Phonologie, Phase E für Wortbeispiele. Unabhängig von F und G.

### Zuständig

SD entscheidet Aussprache und IPA-Festlegungen. PW dokumentiert, generiert und prüft auf
Konsistenz.

---

## Phase J — Scholar / AI

**Status: GEPLANT**

### Ziel

Analysewerkzeuge für die Sprachpflege: Wortgraph, Abfragen und Konsistenzberichte, deren
Ausgaben jederzeit belegbar sind. Diese Phase liefert Erkenntnis, nie Entscheidung.

### Arbeitspakete

- Wortgraph aufbauen: Lexeme, Konzepte, Wortfamilien, Ableitungen und
  Proto-Verbindungen als navigierbare Struktur, vollständig aus `language/` erzeugt.
- Abfrageschicht über die Sprachdaten: Suche nach Flexionsklasse, Domäne, Lernstufe,
  Status, Befundbezug.
- Erklärbarkeit: jede Ausgabe nennt ihre Quelle (Paragraph, Regel-ID, Lexem-ID,
  Befund-ID). Keine Aussage ohne Beleg.
- Konsistenzberichte: Homonymien, Lücken im Konzeptnetz, ungenutzte Regeln, tote
  Verweise, widersprüchliche Felder.
- Abdeckungsbericht: welche Grammatikparagraphen das Korpus tatsächlich prüft und wo
  eine Prüflücke besteht.
- Exportschnittstelle für externe Analyse, ohne dass Analyseergebnisse jemals
  Regelstatus erhalten.

### Abschlusskriterien

- Der Wortgraph wird vollständig aus `language/` erzeugt und ohne Handpflege aktuell
  gehalten.
- Eine Stichprobe bestätigt, dass jede Werkzeugausgabe eine auflösbare Quellenangabe
  trägt.
- Der Abdeckungsbericht weist für jeden Grammatikparagraphen mindestens einen Testfall
  oder eine begründete Lücke aus.
- Kein Werkzeug schreibt Sprachdaten außerhalb eines beauftragten Migrations- oder
  Freigabeschritts.

### Abhängigkeiten

Phase A für das Datenmodell. Der Nutzen steigt mit D und E, der Start hängt nicht daran.

### Zuständig

PW. SD nur dort, wo eine Auswertung eine Sprachaussage berühren würde — dann wird der
Fall als Befund gemeldet, nicht im Werkzeug entschieden.

---

## Phase K — Dialekte und Kultur

**Status: LANGFRISTIG — beginnt ausdrücklich erst nach Grammar 1.0**

### Ziel

Varietäten, Register und kulturelle Einbettung. Diese Phase erweitert Orbis um Vielfalt,
nachdem die Standardsprache stabil ist — nicht vorher.

### Arbeitspakete

- Voraussetzungen prüfen: Grammar 1.0 freigegeben, Lexikon tragfähig, Manus 1.0 vorhanden.
- Varietätenmodell entscheiden: was gilt als Dialekt, was als Register, was als
  Idiolekt; wie wird eine Varietät versioniert und vom Standard abgegrenzt.
- Proto-Orbis weiterführen: Lautwandelgesetze, historische Schichten, Ableitung von
  Varietäten aus dem Proto-Stand.
- Register ausarbeiten: formell, informell, Fachsprache, gebundene Sprache.
- Eigennamen, Zahl- und Kalendersystem, Höflichkeitsformen — je als eigener
  Entscheidungsschritt.
- Kulturelle Texte und Namenskorpus aufbauen.
- Die experimentellen Wortspuren (Möglichkeit, Erinnerung, gehört/berichtet, selbst
  erlebt) bleiben EXPERIMENTAL, bis die SD sie ausdrücklich entscheiden; bis dahin
  erscheinen sie nirgends als bestehende Orbis-Grammatik.

### Abschlusskriterien

- Das Varietätenmodell ist als ADR entschieden, bevor die erste Varietät beschrieben wird.
- Jede Varietät ist getrennt vom Standard versioniert; der Standard bleibt durch die
  Varietätenarbeit unverändert.
- Kein experimentelles System ist ohne ausdrückliche Entscheidung kanonisch geworden.
- Regressionsläufe der Standardsprache bleiben unbeeinflusst von Varietätendaten.

### Abhängigkeiten

Phasen D, E und F. Vor Grammar 1.0 wird in dieser Phase nichts begonnen.

### Zuständig

SD. PW liefert Datenmodell, Trennung der Datenbestände und Prüfläufe.

---

## Abhängigkeiten im Überblick

```
A ──┬──> B ──> C ──> D ──┬──> H
    │                    ├──> I
    │                    └──> K
    ├──> E (E-1) ──> E-2 ──> E-3 ──> E-4
    │                 │              ↑
    │                 └──> H         D
    ├──> F ──> G
    └──> J
```

- A ist Voraussetzung für alles.
- B → C → D ist der kritische Pfad zur Grammatikstabilität.
- E-1, F und J können parallel zu B/C laufen; E-2 wartet auf C.
- G wartet auf F. H, I und K warten auf D.

---

## Nicht-Ziele

Was in diesem Projekt ausdrücklich **nicht** passiert — unabhängig von Phase, Auftrag
oder Zeitdruck:

1. **Keine Massengenerierung von Wortschatz.** Lexeme entstehen einzeln, mit Konzept,
   Begründung, vollständigem Eintrag und Freigabe. Eine Zielzahl rechtfertigt niemals
   automatisch erzeugte Wortlisten. Qualität geht vor Menge, auch wenn eine Stufe dadurch
   länger offen bleibt.
2. **Keine autonomen Sprachentscheidungen.** Werkzeuge, Berichte und KI-Systeme schließen
   keine Regellücke, lösen keinen Regelkonflikt und beseitigen keine Unklarheit durch
   Interpretation. Sie markieren `[REGELLUECKE]`, `[REGELKONFLIKT]` oder
   `[REGELUNKLARHEIT]` mit Befund-ID. Entscheidungen treffen ausschließlich die
   Sprachdesigner.
3. **Keine Vermischung von Manus und Grammatik.** Schriftregeln (§26, `script/`) und
   Grammatikregeln (`language/`) bleiben getrennte Ebenen mit getrennter Versionierung.
   Ein Schriftbefund löst keinen Grammatikschritt aus und umgekehrt. Silbifizierungs-
   Simulationen sind Analysewerkzeuge und werden nie als Sprachregel zitiert.
4. **Kein Überschreiben eingefrorener Fassungen.** `Orbis-Grammatik-0.9.3.md` und alle
   archivierten Dateien bleiben unverändert, auch bei Tippfehlern. Neue Versionen
   entstehen als neue Datei.
5. **Keine Sammelversion.** Grammar, Lexicon, Manus, Keyboard, Corpus und Tools werden
   getrennt versioniert und nicht zu einer gemeinsamen Projektversion zusammengelegt.
6. **Keine stillen Bedeutungsänderungen über die englische Fassung.** Deutsch ist
   semantische Autorität; englische Bedeutungen werden abgeleitet und dürfen die deutsche
   nicht erweitern, verengen oder verschieben. Bei Widerspruch wird die englische Fassung
   korrigiert.
7. **Keine lexikalischen Übernahmen aus realen Sprachen.** Reale Sprachen dürfen
   strukturell, phonologisch oder rhythmisch inspirieren, liefern aber keine Wörter.
8. **Kein Regelduplikat im Werkzeugcode.** Jede Regel, Tabelle und Zeichenzuordnung hat
   genau eine maschinenlesbare Quelle. Werkzeuge lesen sie; sie enthalten keine zweite
   Fassung. Bestehende Konstanten werden nur in beauftragten Migrationsschritten
   aufgelöst.
9. **Keine experimentellen Systeme als geltende Sprache.** Die Morphem-Ebene für
   Manus/Keyboard und die Wortspuren (Möglichkeit, Erinnerung, gehört/berichtet, selbst
   erlebt) sind EXPERIMENTAL und werden nirgends als bestehende Orbis-Grammatik
   dargestellt.
10. **Kein Versionswechsel ohne bestandenen Regressionslauf.** Eine erwartete
    Kompatibilität ersetzt keinen Lauf, und ein grüner Lauf gegen eine halb entschiedene
    Grammatik zählt nicht.

---

## Pflege dieser Datei

Diese Roadmap wird fortgeschrieben, wenn eine Phase abgeschlossen wird, eine
Abhängigkeit sich ändert oder ein Arbeitspaket entfällt. Änderungen an Phasenzielen und
Zuständigkeiten sind eine Entscheidung der Sprachdesigner und erscheinen im
`CHANGELOG.md`. Der Prüfstand darf Status, Messwerte und erledigte Arbeitspakete
nachtragen; er verschiebt keine Zuständigkeit und legt keine neuen Ziele fest.
