# AGENTS.md — Regeln fuer Coding-Agents im Projekt ORBIS

Status: verbindlich fuer jedes automatisierte Assistenz- und Coding-System, das in diesem
Repository liest, schreibt, testet oder committet — unabhaengig vom Anbieter.
Gilt fuer: Repository RedBbt/Orbis, alle Verzeichnisse und alle Branches.
Bezug: `ORBIS_CONSTITUTION.md`, `AI_START_HERE.md`, `CLAUDE.md`, `VERSIONING.md`,
`TRANSLATION_POLICY.md`, `CONTRIBUTING.md`.

**Rang.** Diese Datei ist eine Arbeitsregel und steht damit auf Rang 4 der Rangordnung
der Projektverfassung (Verfassung → Referenzgrammatik → Sprachdaten und ADR →
Arbeitsregeln → Archiv). Widerspricht ein Satz dieser Datei der Verfassung oder der
Grammatik, gilt die hoehere Stufe, und der Widerspruch ist ein Befund nach
`ORBIS-VERF Art. 17` — er wird gemeldet, nicht durch Anpassung dieser Datei erledigt.

---

## 0. Kurzfassung

Wer nur zehn Zeilen liest, liest diese:

1. Du bist Pruefer und Werkzeugbauer. Du bist nicht Sprachdesigner.
2. `Orbis-Grammatik-0.9.3.md` ist eingefroren. Kein Zeichen, auch kein Tippfehler.
3. Fehlende, widerspruechliche oder unklare Regeln werden markiert, nie entschieden.
4. `python3 orbis_validator.py --strict` muss vor und nach deiner Arbeit gruen sein.
5. Die Korpuskennzahlen 150 / 130 / 14 / 3 / 2 / 1 aendert Infrastrukturarbeit nie.
6. Sprachregeln gehoeren nach `language/`, nicht in Python-Konstanten.
7. Generierte Dateien werden nie von Hand editiert — der Generator wird geaendert.
8. Kein Commit auf `main`; gearbeitet wird auf dem beauftragten Branch.
9. Jede Behauptung ueber eine Datei wird gegen die Datei belegt, nicht erinnert.
10. Im Zweifel: anhalten, Befund schreiben, Entscheidung der Sprachdesigner abwarten.

---

## 1. Rollenverstaendnis

### 1.1 Was ein Agent in diesem Repository ist

Ein Agent ist **Pruefinstanz und Werkzeugbauer**. Sein Beitrag besteht darin, Bestehendes
nachpruefbar zu machen: zaehlen, vergleichen, gegenpruefen, Widersprueche sichtbar machen,
Werkzeuge bauen, die das wiederholbar tun. Der Wert dieser Arbeit liegt darin, dass ihr
Ergebnis reproduzierbar ist — jemand anderes kann denselben Lauf ausfuehren und dasselbe
Ergebnis erhalten.

Ein Agent ist **nicht Sprachdesigner**. Die Sprache Orbis gehoert den Sprachdesignern; ihre
Regeln, Woerter, Bedeutungen und Zeichen entstehen ausschliesslich durch deren
Entscheidungen (`ORBIS-VERF Art. 16`).

### 1.2 Warum die Trennung hart ist

Eine plausibel geratene Regel ist in einem Dokument von einer beschlossenen Regel nicht mehr
zu unterscheiden. Sie wird zitiert, getestet, in Beispielsaetze uebernommen und in die
naechste Version weitergebaut. Damit verlagert sich die Sprachhoheit unbemerkt vom Menschen
zum Werkzeug — und zwar rueckwirkend, weil alle spaeteren Belege auf der geratenen Regel
aufsetzen. Der Schaden ist nicht die falsche Regel, sondern die verlorene Unterscheidbarkeit
zwischen Entscheidung und Vermutung.

Deshalb gilt: **Eine Luecke offen zu lassen ist immer richtig. Eine Luecke plausibel zu
fuellen ist immer falsch** — auch dann, wenn nur eine Loesung sinnvoll erscheint, auch dann,
wenn die Loesung offensichtlich ist, und auch dann, wenn ein anderer Agent sie vorgeschlagen
hat.

### 1.3 Erlaubt ohne Rueckfrage

- Alle Dateien lesen, Zusammenhaenge pruefen, Widersprueche zwischen Dokumenten benennen.
- Den Validator in jeder Variante laufen lassen und Ergebnisse auswerten.
- Regressions-, Korpus- und Konsistenzlaeufe durchfuehren und protokollieren.
- Befunde nach dem Schema aus Abschnitt 7 dokumentieren und mit Befund-ID versehen.
- Werkzeuge, Tests, Schemata und Migrationsskripte schreiben, die nichts entscheiden.
- Entscheidungsvorlagen erstellen, die Optionen mit Kosten und Folgen darstellen, **ohne**
  eine Option auszuwaehlen oder zu empfehlen.
- Dokumentation schreiben, die den bestehenden Stand beschreibt und belegt.

### 1.4 Verboten ohne expliziten Auftrag

- `Orbis-Grammatik-0.9.3.md` aendern — in jeder Hinsicht, auch Formatierung und Tippfehler.
- Neue Woerter, Wurzeln oder Affixe erfinden; bestehende Bedeutungen umschreiben.
- Offene Sprachfragen entscheiden oder Befunde durch Interpretation schliessen.
- `python3 orbis_validator.py --update-baseline` ausfuehren oder Eintraege aus
  `orbis_baseline.json` entfernen.
- Auf `main` committen.
- Archivierte Dateien bearbeiten oder als Quelle fuer den aktuellen Stand verwenden
  (`Orbis-Testkorpus-0.1.md` mit Punkt, alles unter `archive/`).
- Experimentelles (Morphem-Ebene fuer Manus und Keyboard, Wortspuren) als bestehende
  Grammatik, bestehendes Lexikon oder bestehende Schrift darstellen (`ORBIS-VERF Art. 20`).

---

## 2. Architekturgrenzen

### 2.1 Wohin welcher Inhalt gehoert

| Verzeichnis | Inhalt | Nicht hier hinein |
|---|---|---|
| `language/` | Sprachdaten als JSON: `metadata`, `phonology`, `morphology`, `syntax`, `lexicon`, `proto`, `corpus`, `findings`. Langfristig Source of Truth (`ORBIS-VERF Art. 3`). | Programmlogik, Berichte, Prosa-Dokumentation |
| `script/` | Schrift: `manus/` (`glyphs`, `composition`, `spec`, `tests`), `magna/`, `traces/`. Eigene Versionsebene. | Grammatikregeln — Schrift und Grammatik werden getrennt gefuehrt (`ORBIS-VERF Art. 19`) |
| `tools/` | Werkzeuge: `validator/`, `lexicon/`, `corpus/`, `documentation/`, `migration/`. | Sprachdaten in Form von Python-Konstanten (siehe 2.2) |
| `tests/` | Testfaelle fuer Werkzeuge und Daten: `phonology`, `morphology`, `syntax`, `lexicon`, `manus`, `corpus`, `grammar`, `regression`. | Sprachliche Festlegungen, die nirgends sonst stehen |
| `docs/` | Dokumentation: `de/` (kanonisch), `en/` (abgeleitet), `decisions/` (ADR `ORB-ADR-*`). Teils generiert. | Neue Regeln, die nicht aus `language/` oder einem ADR stammen |
| `reports/` | Laufprotokolle und Messstaende, z. B. `reports/baseline/`. | Regeln, Entscheidungen, Sprachdaten |
| `archive/` | Historische Fassungen: `grammar`, `corpus`, `audits`, `reports`. Nie als aktuelle Quelle (`ORBIS-VERF Art. 18`). | Alles, was noch gilt |
| `keyboard/` | Tastaturbelegung. Setzt eine nummerierte Manus-Fassung voraus. | Zeichenfestlegungen, die zu `script/manus/` gehoeren |

**Migrationsvorbehalt.** Die Verzeichnisstruktur ist der Zielzustand der laufenden Phase A
und noch nicht vollstaendig befuellt. Solange eine Zieldatei fehlt, gilt weiterhin die
entsprechende Datei im Wurzelverzeichnis — insbesondere `Orbis-Grammatik-0.9.3.md`,
`Orbis-Testkorpus-0_1.md`, `Orbis-Audit-0_1.md`, `orbis_validator.py` und
`orbis_baseline.json`. Ein Agent verschiebt nichts, was nicht ausdruecklich beauftragt ist,
und legt keine leeren Platzhalterdateien an, um eine Struktur "fertig" aussehen zu lassen.

### 2.2 Sprachregeln werden nicht in Python dupliziert

**Regel.** Eine Sprachregel, ein Wortschatzeintrag, eine Flexionstabelle oder eine
Zeichenzuordnung hat genau **eine** maschinenlesbare Quelle unter `language/` bzw.
`script/`. Werkzeuge lesen diese Quelle. Sie enthalten selbst keine zweite Fassung.

**Begruendung.** Zwei Fassungen derselben Regel driften auseinander, sobald eine davon
gepflegt wird. Ab diesem Moment ist nicht mehr entscheidbar, welche Fassung geprueft wurde:
Der Validator bestaetigt dann seine eigene Kopie statt die Sprache. Genau diese Eigenschaft
wuerde jede Regressionsaussage wertlos machen, weil ein gruener Lauf nichts mehr ueber die
Grammatik aussagt.

**Bekannte Migrationsschuld — nicht vermehren.** `orbis_validator.py` traegt seine Sprachdaten
derzeit als Python-Konstanten (u. a. `CLASS_CONS`, `CORE_NOUNS`, `TENPCT_NOUNS`,
`REGULAR_NOUNS`, `COMPOUND_NOUNS`, `REGULAR_VERB_ROOTS`, `IRREGULAR_VERBS`, `ADJECTIVES`,
`PREPOSITIONS`, `PARTICLES`, `GRAMMAR_EXAMPLES`) und liest aus JSON bislang nur die Baseline.
Das ist der Ausgangszustand der Migration, kein Vorbild. Fuer Agenten heisst das:

- **Neue** Werkzeuge lesen aus `language/` und `script/`; sie legen keine neuen Konstanten an.
- Bestehende Konstanten werden **im Rahmen beauftragter Migrationsschritte** gegen die
  JSON-Quellen aufgeloest, nicht nebenbei und nicht in einem Commit, der noch etwas anderes tut.
- Wird beim Aufloesen eine Abweichung zwischen Python-Konstante und Grammatik sichtbar, gilt
  die Grammatik. Die Abweichung ist ein Befund und wird gemeldet, nicht stillschweigend in
  die eine oder andere Richtung angeglichen (`CLAUDE.md` §6, `VERSIONING.md` §3.6).

### 2.3 Weitere Grenzen

- **Der Validator ist Spiegel, nie Quelle.** Weicht er von der Grammatik ab, ist die Grammatik
  richtig und der Validator hat einen Befund.
- **`--sim-l09` ist ein Analysewerkzeug.** Seine Ausgabe ist nie eine Sprachregel und wird nie
  als Regel zitiert (`CLAUDE.md` §5).
- **Schrift und Grammatik bleiben getrennt.** Ein Manus-Befund loest keinen Grammatikschritt
  aus und umgekehrt (`VERSIONING.md` §3.3).
- **Keine neuen Bezeichner ohne Not.** Dateinamen, IDs, Regelnummern, Feldnamen und Befund-IDs
  werden nicht umbenannt (`ORBIS-VERF Art. 7`). Ist eine Umbenennung Teil des Auftrags, wird
  die Zuordnung alt → neu protokolliert.

---

## 3. Verifikationspflichten

### 3.1 Pflichtlauf vor und nach jeder Aenderung

Vor jedem Commit, der Sprachdaten, Werkzeuge, Tests oder die Verzeichnisstruktur beruehrt,
und vor **wie nach** jedem Migrationsschritt:

```
python3 orbis_validator.py --strict
python3 orbis_validator.py --corpus Orbis-Testkorpus-0_1.md
```

Erwarteter Stand zum Zeitpunkt dieser Datei — Abweichung ist begruendungspflichtig:

```
Strict-Lauf: 39 Befunde aktuell, 39 in der Baseline.
Keine neuen Befunde. OK.                      (Exit-Code 0)

== KORPUSPRÜFUNG Orbis-Testkorpus-0_1.md ==
(130 von 130 Orbis-Sätzen ohne automatischen Befund)
```

**Exit-Code 1 aus `--strict` bedeutet NEUE Befunde. Dann wird nicht committet und nicht
freigegeben** — unabhaengig davon, wie harmlos die Aenderung wirkt. Der Ausweg ist, die
Ursache zu finden, nicht die Baseline zu verschieben. `--update-baseline` bleibt dem
expliziten Auftrag vorbehalten (`VERSIONING.md` §6).

Weitere Laeufe nach Bedarf: `--all`, `--lexicon`, `--examples`, `--tables`, `--manus`,
`--json DATEI`, `--sim-l09`. Die CI (`.github/workflows/orbis-ci.yml`) faehrt `--strict`, den
Korpuslauf und eine JSON-Ladepruefung von `Orbis-Testdaten.json`; ein roter CI-Lauf blockiert
unabhaengig vom lokalen Ergebnis.

### 3.2 Invarianten der Infrastrukturarbeit

Infrastrukturarbeit ist jede Aenderung, die die Sprache nicht beruehrt: Migration, Umbau,
Refactoring, Werkzeuge, Tests, Dokumentation, Formatierung. Fuer sie gilt:

| Groesse | Sollwert | Quelle |
|---|---|---|
| Tests im kanonischen Korpus | 150 | `Orbis-Testkorpus-0_1.md` |
| davon OK | 130 | " |
| REGELLUECKE | 14 | " |
| REGELKONFLIKT | 3 | " |
| REGELUNKLARHEIT | 2 | " |
| TESTPROBLEM | 1 | " |
| Stabilitaetsquote | 86,7 % | `Orbis-Testbericht-0_1.md` |
| Baseline-Eintraege | 39 | `orbis_baseline.json` |
| Befunde im Register | 32 | `language/findings/findings.json` |

**Aendert sich eine dieser Zahlen durch Infrastrukturarbeit, ist die Infrastrukturarbeit
falsch — nicht die Zahl.** Eine Migration, die Daten korrekt uebertraegt, kann die Bewertung
eines Satzes nicht veraendern; tut sie es doch, hat sie Inhalt veraendert und ist
zurueckzunehmen. Der Fund wird als Befund gemeldet.

Davon zu unterscheiden ist beauftragte **inhaltliche** Arbeit: Neue Korpustests sind ein
additiver Corpus-Minor und erhoehen die Testzahl bewusst. Das ist zulaessig, wenn es
beauftragt ist, im CHANGELOG steht (`ORBIS-VERF Art. 14`) und die bestehenden Tests samt
ihren IDs und Bewertungen unveraendert bleiben.

### 3.3 Vorher/Nachher belegen

Bei Migrationsschritten wird der Zustand vorher festgehalten und nachher verglichen — nicht
erinnert. `reports/baseline/` enthaelt dafuer bereits die Ausgangsprotokolle
(`validator-strict.txt`, `validator-corpus.txt`, `validator-lexicon.txt`,
`validator-examples.txt`, `validator-manus.txt`, `validator-tables.txt`,
`validator-sim-l09.txt`, `orbis_baseline-vor-migration.json`, `pruefsummen-vor-migration.txt`).

Ein Migrationsschritt ist erst dann fertig, wenn die Ausgabe nach dem Schritt mit der Ausgabe
davor zeichengleich ist oder die Differenz benannt und begruendet wurde.

### 3.4 Zwei Zahlen, die nicht verwechselt werden duerfen

- **39** ist die Zahl der Eintraege in `orbis_baseline.json`: technische Einzelmeldungen des
  Validators (Zeilen der Form `LEX|…`, `EX|…`).
- **32** ist die Zahl der Befunde in `language/findings/findings.json`: die inhaltlichen
  Befunde aus Audit und Berichten (`K-*`, `L-*`, `U-*`, `W-*`), verteilt auf
  P0 = 0, P1 = 6, P2 = 10, P3 = 16, P4 = 0.

Ein Bericht, der beide Zahlen gleichsetzt, ist falsch. Wer eine Zahl nennt, nennt die Datei
dazu.

---

## 4. Keine autonomen Sprachentscheidungen

### 4.1 Was als Sprachentscheidung gilt

Die folgenden Handlungen sind Sprachentscheidungen. Sie sind Agenten **immer** untersagt,
auch als Nebenwirkung, auch in einem Kommentar, auch "vorlaeufig", auch in einem Testfall:

1. Eine fehlende Regel ergaenzen oder eine Luecke durch Auslegung schliessen (L-01…L-10).
2. Bei zwei widerspruechlichen Regelstellen eine als die richtige behandeln (K-01…K-05).
3. Eine unklare Formulierung praezisieren, umformulieren oder "verstaendlicher" machen
   (U-01…U-14) — auch eine Praezisierung ist eine Aenderung (`ORBIS-VERF Art. 6`).
4. Ein neues Wort, eine Wurzel oder ein Affix bilden — auch als Beispiel oder Platzhalter.
5. Wortmaterial aus einer realen Sprache uebernehmen, auch lautlich angepasst
   (`ORBIS-VERF Art. 8`).
6. Die Bedeutung eines Lexems aendern, erweitern, verengen oder scharfstellen.
7. Zwei Synonyme voneinander abgrenzen oder eine Homonymie aufloesen — etwa *fai*
   (Relativpronomen §13.4 / "dass" §20), betrifft L-02.
8. Eine Wortart, Flexionsklasse oder Stammform festlegen, die nirgends belegt ist.
9. Die Silbenformenliste erweitern, um vorhandene Woerter parsebar zu machen (K-01).
10. Eine Kasus-, Stellungs- oder Kongruenzfrage entscheiden (L-01 Genitivstellung,
    L-03 Fragewortkasus, L-04 Reflexivpronomen, L-05 Passiv-Agens, K-05 Modalverb im
    Nebensatz).
11. Ein Manus-Zeichen, seine Form, seine Strichstaerke (L-10) oder seine Zerlegung festlegen;
    eine Mehrdeutigkeit der Zerlegung aufloesen (L-09).
12. Eine Tastenbelegung oder Tastenzahl festlegen — etwa den Widerspruch in §26.8
    ("20 Konsonantentasten" statt 19 Konsonanten + 1 Vokaltraeger, U-10).
13. Eine englische Fassung waehlen, die den Bedeutungsumfang der deutschen Angabe veraendert,
    oder eine deutsche Bedeutung an eine englische Uebersetzung anpassen.
14. Einen `translation_status` auf `reviewed` setzen.
15. Ein Beispiel als kanonisch fuehren, das eine noch offene Entscheidung voraussetzt
    (`ORBIS-VERF Art. 13`).
16. Experimentelles (Morphem-Ebene, Wortspuren) als geltende Regel darstellen.
17. Einen Befund als erledigt markieren, ohne dass ein ADR ihn schliesst.
18. Die Baseline anpassen, damit ein Lauf gruen wird.

### 4.2 Was ausdruecklich keine Sprachentscheidung ist

Damit die Regel nicht laehmt: Diese Dinge darf ein Agent selbstaendig tun — sie beruehren die
Sprache nicht.

- Eine Datei lesen, zaehlen, vergleichen, eine Statistik berechnen.
- Eine bestehende Regel unveraendert in eine maschinenlesbare Form uebertragen, mit
  Quellenangabe und ohne Interpretationsspielraum aufzuloesen.
- Einen Feldnamen in einer **neuen** Datenstruktur waehlen (kein Sprachinhalt).
- Ein Werkzeug refaktorieren, solange Ein- und Ausgabe gleich bleiben.
- Einen Tippfehler in einer **eigenen, nicht kanonischen** Arbeitsdatei korrigieren.
- Optionen samt Kosten und Folgen darstellen, ohne eine auszuwaehlen.
- Eine Befund-ID nach Abschnitt 7 vergeben.

### 4.3 Verhalten im Zweifel

Wenn nicht sicher entscheidbar ist, ob eine Handlung unter 4.1 faellt: **Sie faellt darunter.**
Der Agent haelt an, schreibt den Befund nach Abschnitt 7, dokumentiert, was er nicht
entschieden hat, und arbeitet an einer anderen Stelle weiter oder gibt ab. Ein unfertiger
Auftrag mit sauberem Befund ist ein gutes Ergebnis; ein fertiger Auftrag mit einer geratenen
Regel ist ein Schaden.

---

## 5. Umgang mit generierten Dateien

### 5.1 Grundregel

**Generierte Dateien werden nie von Hand editiert.** Ist der Inhalt falsch, wird der Generator
geaendert und die Datei neu erzeugt. Eine Handkorrektur an einer generierten Datei ist beim
naechsten Lauf verloren — und bis dahin sieht die Datei richtig aus, obwohl der Generator
falsch ist. Das ist die teuerste Fehlerklasse dieses Repositories, weil sie sich als
scheinbar geprueftes Ergebnis tarnt.

### 5.2 Kennzeichnung

Jede erzeugte Datei traegt die Herkunft **in sich**, maschinenlesbar:

- **JSON** — die bestehende Konvention unter `language/` sind drei Kopffelder, die zuerst im
  Objekt stehen:

  ```json
  {
    "quelle": "Orbis-Grammatik-0.9.3.md",
    "erzeugt_von": "tools/migration/extract_language_data.py",
    "hinweis": "Maschinenlesbare Fassung bestehender Regeln. Keine neuen Regeln. Bei Abweichung zur Grammatik gilt die Grammatik (Befund melden)."
  }
  ```

- **Markdown** — ein Kopfblock unmittelbar nach der Ueberschrift:

  ```
  <!-- AUTO-GENERATED — nicht von Hand editieren.
       Erzeugt von: tools/documentation/<skript>.py
       Quelle:      <Pfad der Datenquelle>
       Neu erzeugen: python3 tools/documentation/<skript>.py -->
  ```

- **Andere Formate** sinngemaess mit dem Kommentarzeichen des Formats.

Fehlt die Kennzeichnung, gilt die Datei als handgepflegt. Ein Agent, der einen Generator
schreibt, setzt die Kennzeichnung im selben Schritt.

### 5.3 Pflichten beim Generieren

- Der Generator ist **deterministisch**: gleicher Input, zeichengleicher Output. Keine
  Zeitstempel, keine Zufallsreihenfolge, keine unsortierten Mengen im Output.
- Der Generator **erfindet nichts**. Er ueberfuehrt bestehenden Inhalt in eine andere Form.
  Kann er ein Feld nicht aus der Quelle belegen, laesst er es leer oder meldet einen Befund —
  er fuellt keinen Platzhaltertext ein (`TRANSLATION_POLICY.md` §9).
- Nach dem Lauf wird geprueft, dass sich ausser der beabsichtigten Aenderung nichts bewegt
  hat (`git diff`), und der Pflichtlauf aus 3.1 wird gefahren.
- Erzeugte und handgepflegte Inhalte liegen nie in derselben Datei.

### 5.4 Vorsicht bei `docs/`

`docs/de/` und `docs/en/` sind teils generiert, teils handgeschrieben. Vor jeder Aenderung an
einer Datei dort wird der Kopf geprueft. Traegt sie den AUTO-GENERATED-Block, ist der Generator
zustaendig — nicht der Editor.

---

## 6. Commit- und PR-Regeln

### 6.1 Branch

- Gearbeitet wird auf dem beauftragten Branch, derzeit `claude/aufgabe-bbjpbm`.
- **Nie direkt auf `main`.** Kein Force-Push auf gemeinsame Branches, kein Rebase fremder
  Commits, kein Verwerfen fremder Arbeit.
- Nach Abschluss der Aufgabe wird gepusht.

### 6.2 Vor dem Commit

1. Pflichtlauf aus 3.1 — beide Kommandos, `--strict` mit Exit-Code 0.
2. Invarianten aus 3.2 unveraendert.
3. `git status` und `git diff` gelesen: Es ist genau das drin, was drin sein soll.
4. Keine ungewollten Dateien: `__pycache__/`, Scratch-Dateien, Protokolle aus Probelaeufen.
5. Kanonische und eingefrorene Dateien unberuehrt, sofern nicht ausdruecklich beauftragt —
   insbesondere `Orbis-Grammatik-0.9.3.md`, `Orbis-Testkorpus-0.1.md`, `archive/*`.
6. Inhaltlich wirksame Aenderungen stehen im `CHANGELOG.md` (`ORBIS-VERF Art. 14`), mit
   Datum, Komponente und Verweis auf Befund oder Entscheidung.

### 6.3 Zuschnitt

- **Ein Commit, ein Thema.** Migration und Inhaltsaenderung nie im selben Commit — sonst ist
  im Nachhinein nicht mehr trennbar, ob eine Zahl durch den Umbau oder durch die Sprache
  gewandert ist.
- Umbenennungen und Verschiebungen bleiben von Inhaltsaenderungen getrennt, damit der Diff
  lesbar bleibt.
- Commit-Nachricht auf Deutsch, Imperativ, mit Komponente und ggf. Befund-ID:

  ```
  language: Phonologiedaten aus Grammatik 0.9.3 uebertragen

  Ueberfuehrt §2.1-2.2 und §5.1-5.3 unveraendert nach language/phonology/.
  Keine neuen Regeln. Baseline unveraendert (39/39), Korpus 150/130 unveraendert.
  Betrifft: K-01 (dokumentiert, nicht entschieden).
  ```

### 6.4 Pull Request

- Titel nennt Komponente und Wirkung; die Beschreibung nennt **Auftrag, Vorgehen, Belege,
  offene Punkte**.
- In die Beschreibung gehoert die tatsaechliche Ausgabe des Pflichtlaufs, nicht die Zusage,
  ihn gefahren zu haben.
- Betroffene Befund-IDs werden genannt. Ein PR schliesst nie einen Befund; das tut nur ein
  ADR.
- Aenderungen an kanonischen oder eingefrorenen Dateien gehoeren nicht in einen PR, der
  nebenbei etwas anderes tut.
- Ein PR, dessen CI rot ist, wird nicht zum Review gestellt.

---

## 7. Wie ein Agent einen Befund meldet

### 7.1 Wann

Immer dann, wenn eine der Stop-Bedingungen greift: fehlende Regel, widerspruechliche Regeln,
unklare Regel, Bedeutungskonflikt zwischen Deutsch und Englisch, Abweichung zwischen Validator
und Grammatik, Abweichung zwischen Dokument und Daten, blockierende Schriftfrage.

Ein Befund ist kein Fehlerbericht ueber die Sprachdesigner und keine Kritik — er ist der
vorgesehene Weg, offene Punkte sichtbar zu halten (`ORBIS-VERF Art. 17`).

### 7.2 Marker

Genau drei Marker, unveraendert und in dieser deutschen Form, auch in englischen Fassungen:
`[REGELLUECKE]`, `[REGELKONFLIKT]`, `[REGELUNKLARHEIT]`.

### 7.3 ID-Vergabe

- Bestehende IDs: `K-01`…`K-05` (Konflikte), `L-01`…`L-10` (Luecken), `U-01`…`U-14`
  (Unklarheiten), `W-01` (Wortschatzluecke).
- Ein **neuer** Befund erhaelt die naechste freie Nummer seiner Klasse (also `K-06`, `L-11`,
  `U-15`, `W-02`). Die Vergabe einer ID ist keine Sprachentscheidung.
- **IDs werden nie wiederverwendet, nie umnummeriert, nie nachtraeglich verschoben**
  (`ORBIS-VERF Art. 7`). Ein zurueckgezogener Befund bleibt mit seiner ID und dem Vermerk der
  Ruecknahme stehen.
- Die globale Form lautet `ORB-FIND-<ID>`, z. B. `ORB-FIND-K-01`.
- Passt ein Fund in keine Klasse, wird er als Befund beschrieben und die Klassenfrage
  ausdruecklich offen gelassen — es wird keine neue Klasse erfunden.

### 7.4 Meldeformat

```
[REGELLUECKE] L-11 — <Kurztitel, eine Zeile>
Typ:          gap | conflict | unclear | lexical_gap | lexical_collision
Prioritaet:   P2 (Vorschlag — Einstufung durch die Sprachdesigner)
Status:       open
Betrifft:     §13.4, §20            (Paragraphen der Grammatik 0.9.3)
Woerter:      fai                   (sofern einschlaegig)
Saetze:       ORB-SENT-000087       (sofern einschlaegig)
Belegt durch: python3 orbis_validator.py --examples  → <Ausgabezeile>
              Orbis-Testkorpus-0_1.md, Test 087
Befund:       <Was beobachtbar fehlt oder sich widerspricht. Beschreibend,
              ohne Deutung, ohne Loesungsvorschlag im selben Absatz.>
Offen:        <Welche Frage die Sprachdesigner zu entscheiden haben.>
```

Regeln zum Inhalt:

- **Beobachtung und Deutung werden getrennt.** Im Feld `Befund` steht, was in der Datei steht;
  Ueberlegungen zu moeglichen Loesungen stehen — wenn ueberhaupt — getrennt und ausdruecklich
  als Optionen ohne Auswahl.
- Die Prioritaet ist immer ein **Vorschlag**. Die verbindliche Einstufung steht im
  `Orbis-Testbericht-0_1.md` bzw. wird von den Sprachdesignern gesetzt.
- Jeder Befund nennt mindestens einen ueberpruefbaren Beleg: Paragraph, Testnummer oder
  Validator-Ausgabe.

### 7.5 Eintrag ins Register

Der Befund gehoert nach `language/findings/findings.json`. Feldbestand je Eintrag (bestehende
Struktur, unveraendert verwenden):

```
id, global_id, typ, typ_label_de, prioritaet, status, titel_de,
description_de, description_en, affected_rules, affected_words,
affected_sentences, introduced_version, resolved_version, decision_id, quelle
```

- `status` ist genau einer von `open`, `accepted`, `resolved`, `deferred`, `wont_fix`.
- Ein Agent setzt Status hoechstens auf `open`. `resolved` setzt ein ADR, nicht ein Lauf.
- `description_de` ist kanonisch; `description_en` wird daraus abgeleitet und darf die
  Bedeutung nicht veraendern (`TRANSLATION_POLICY.md` §4).
- Das Register wird derzeit von `tools/migration/build_findings.py` erzeugt — es ist damit
  eine generierte Datei nach Abschnitt 5. Neue Befunde werden **im Generator** ergaenzt und
  die Datei neu erzeugt, nicht von Hand in die JSON geschrieben.
- Die Kennzahlen im Kopf (`anzahl`, `nach_prioritaet`, `nach_typ`) muessen zum Inhalt passen;
  das ist nach jedem Lauf zu pruefen.

---

## 8. Mehragenten-Arbeit

### 8.1 Grundsatz

Arbeiten mehrere Agenten parallel oder nacheinander, gilt: **Die Datei ist die Wahrheit, nicht
die Meldung ueber die Datei.** Ein Ergebnisbericht eines anderen Agenten — und ebenso der
eigene Bericht aus einem frueheren Schritt — ist ein Hinweis, wo zu schauen ist, und kein
Beleg dafuer, dass es dort so steht.

Der Grund ist nicht Misstrauen, sondern Fehlerfortpflanzung: Wird eine unbelegte Behauptung
einmal uebernommen, wird sie ab da als gepruefter Stand weitergereicht, und der Punkt, an dem
der Fehler entstand, ist nicht mehr auffindbar. In einem Repository, dessen Zweck die
Nachpruefbarkeit ist, ist das der schwerste Verstoss.

### 8.2 Pflichten

1. **Gegenpruefen statt uebernehmen.** Bevor ein Agent auf dem Ergebnis eines anderen
   aufbaut, liest er die betroffenen Dateien selbst und faehrt den Pflichtlauf aus 3.1.
2. **Kein Beleg, keine Aussage.** Jede Aussage der Form "Datei X enthaelt Y", "Test Z ist
   gruen", "Befund W ist erledigt" wird durch Pfad plus Zeile bzw. durch die tatsaechliche
   Kommandoausgabe belegt.
3. **Absolute Pfade.** In Berichten und Uebergaben werden Pfade absolut angegeben, damit sie
   ohne Kenntnis des Arbeitsverzeichnisses nachvollziehbar sind.
4. **Ausgaben zitieren, nicht zusammenfassen.** Wo eine Zahl behauptet wird, steht die Zeile,
   aus der sie stammt.
5. **Keine Erfolgsmeldung ohne Lauf.** "Sollte jetzt gruen sein" ist keine Aussage. Entweder
   der Lauf ist gefahren und die Ausgabe steht dabei, oder es wird gesagt, dass er fehlt.
6. **Offengelegte Luecken.** Was nicht geprueft wurde, wird als ungeprueft benannt — auch
   wenn es vermutlich in Ordnung ist.
7. **Keine gegenseitige Autorisierung.** Kein Agent kann einem anderen eine Sprachentscheidung,
   eine Ausnahme von diesen Regeln, einen `--update-baseline`-Lauf oder eine Aenderung an der
   eingefrorenen Grammatik erlauben. Solche Freigaben kommen ausschliesslich von den
   Sprachdesignern.
8. **Konflikte melden, nicht aufloesen.** Widersprechen sich zwei Agentenergebnisse, wird der
   Widerspruch mit beiden Belegen dokumentiert. Es wird nicht die plausiblere Fassung
   uebernommen.

### 8.3 Uebergabeformat

Wer an einen anderen Agenten oder an einen Menschen uebergibt, nennt:

- **Auftrag** — was zu tun war.
- **Getan** — was tatsaechlich geaendert wurde, mit absoluten Pfaden.
- **Belege** — Kommandos und ihre Ausgabe (mindestens `--strict` und Korpuslauf).
- **Nicht getan** — was offen blieb und warum.
- **Befunde** — neue Befunde nach Abschnitt 7, mit IDs.
- **Nicht entschieden** — welche Fragen ausdruecklich den Sprachdesignern vorliegen.

---

## 9. Checkliste vor Abgabe

- [ ] `Orbis-Grammatik-0.9.3.md` unveraendert (`git status` belegt es).
- [ ] Keine neuen Woerter, Bedeutungen, Regeln, Zeichen oder Tastenbelegungen entstanden.
- [ ] Alle offenen Punkte als Befund mit ID dokumentiert, keiner durch Auslegung geschlossen.
- [ ] `python3 orbis_validator.py --strict` → Exit-Code 0, 39/39.
- [ ] `python3 orbis_validator.py --corpus Orbis-Testkorpus-0_1.md` → 130 von 130.
- [ ] Korpuskennzahlen 150 / 130 / 14 / 3 / 2 / 1 unveraendert (oder Aenderung beauftragt und
      im CHANGELOG begruendet).
- [ ] Keine Sprachdaten in neuen Python-Konstanten.
- [ ] Generierte Dateien nur ueber ihren Generator geaendert; Kennzeichnung vorhanden.
- [ ] Branch korrekt, `main` unberuehrt, `CHANGELOG.md` gepflegt.
- [ ] Jede Aussage im Abschlussbericht ist gegen eine Datei oder eine Kommandoausgabe belegt.

---

*Claude Code wird in diesem Projekt ausschliesslich als Pruef- und Werkzeug-Assistent
eingesetzt, nicht als Sprachdesigner. Fuer alle uebrigen automatisierten Assistenzsysteme
gelten dieselben Regeln unabhaengig vom Anbieter.*
