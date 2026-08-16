# CONTRIBUTING — Mitwirken am Projekt ORBIS

Status: verbindlich fuer alle menschlichen Mitwirkenden.
Gilt fuer: Repository RedBbt/Orbis.
Bezug: `ORBIS_CONSTITUTION.md`, `README.md`, `VERSIONING.md`, `TRANSLATION_POLICY.md`,
`AGENTS.md` (Regeln fuer automatisierte Assistenzsysteme), `CLAUDE.md`.

Willkommen. Dieses Dokument erklaert, wie man in diesem Repository mitarbeitet: was ein
nuetzlicher Beitrag ist, was ohne Entscheidung der Sprachdesigner nicht geht, welche Pruefungen
vor einem Pull Request laufen muessen und wohin welche Datei gehoert.

---

## 1. Worum es geht

Orbis ist eine konstruierte Sprache mit eigener Schrift (Orbis Manus). Das Projekt verbindet
Sprachdesign mit maschineller Pruefung: Eine eingefrorene Referenzgrammatik wird gegen ein
Testkorpus und einen Validator geprueft, Befunde werden dokumentiert und fliessen als
Designentscheidungen in die naechste Version ein.

Der Kerngedanke, an dem sich alles andere ausrichtet: **Offene Punkte werden sichtbar
gehalten, nicht geschlossen.** Ein Projekt, das jede Luecke sofort plausibel fuellt, verliert
die Unterscheidung zwischen dem, was entschieden wurde, und dem, was jemand einmal fuer
naheliegend hielt. Deshalb ist ein gut dokumentierter Befund hier ein vollwertiger Beitrag —
oft der wertvollere gegenueber einer schnellen Loesung.

### 1.1 Wer entscheidet was

| Rolle | Zustaendigkeit |
|---|---|
| **Sprachdesigner** | Alle Sprach- und Designentscheidungen: Regeln, Woerter, Bedeutungen, Zeichen, Prioritaeten, Freigaben. |
| **Mitwirkende** | Pruefen, belegen, Befunde melden, Testfaelle beitragen, Werkzeuge und Dokumentation bauen, Optionen aufbereiten. |
| **Werkzeuge und Assistenzsysteme** | Pruefen und melden. Sie entscheiden nichts (`ORBIS-VERF Art. 16`, `AGENTS.md`). |

---

## 2. Einstieg

### 2.1 Voraussetzungen

Python 3 (CI faehrt 3.12), Git. **Keine externen Abhaengigkeiten** — der Validator laeuft mit
der Standardbibliothek. Es gibt nichts zu installieren.

```
git clone https://github.com/RedBbt/Orbis.git
cd Orbis
python3 orbis_validator.py --strict
```

Der letzte Befehl sollte ohne neue Befunde durchlaufen (Exit-Code 0). Tut er das nicht, liegt
es an der Arbeitskopie, nicht am Beitrag — bitte zuerst klaeren.

### 2.2 Lesereihenfolge

1. `ORBIS_CONSTITUTION.md` — die Projektverfassung; sie steht ueber allen anderen Regeln.
2. `README.md` — Ueberblick, Status, Validatoraufrufe.
3. Dieses Dokument.
4. `Orbis-Grammatik-0.9.3.md` — die kanonische Referenzgrammatik. Jede Regelfrage wird hier
   und nur hier beantwortet.
5. `Orbis-Audit-0_1.md` — Regelbasis und alle Befund-IDs.
6. `Orbis-Testbericht-0_1.md` — Lagebeurteilung, Prioritaeten, Begruendung des Urteils.
7. `VERSIONING.md` und `TRANSLATION_POLICY.md` — Versions- und Sprachregeln.

Wer Werkzeuge baut oder mit einem Assistenzsystem arbeitet, liest zusaetzlich `AGENTS.md`.

### 2.3 Stand in Zahlen

| Groesse | Wert |
|---|---|
| Grammatik | 0.9.3, eingefroren (READ ONLY) |
| Testkorpus | 150 Tests: 130 OK, 14 REGELLUECKE, 3 REGELKONFLIKT, 2 REGELUNKLARHEIT, 1 TESTPROBLEM |
| Stabilitaetsquote | 86,7 % |
| Urteil | NOT READY fuer einen direkten 1.0-Sprung; kein P0, 6 P1-Probleme, alle additiv loesbar |
| Baseline | `orbis_baseline.json`, 39 bekannte Validatormeldungen |
| Befundregister | `language/findings/findings.json`, 32 Befunde |

Diese Zahlen sind Bezugspunkte. Wenn ein Beitrag sie veraendert, muss das gewollt, begruendet
und im `CHANGELOG.md` vermerkt sein.

### 2.4 Umbau im Gange

Das Repository wird derzeit auf eine neue Struktur umgestellt (`language/`, `script/`,
`tools/`, `tests/`, `docs/`, `reports/`, `archive/`). Die Umstellung ist nicht abgeschlossen:
Solange eine Zieldatei fehlt, gilt weiterhin die entsprechende Datei im Wurzelverzeichnis.
Bitte keine Dateien auf eigene Faust verschieben — Verschiebungen sind eigene, beauftragte
Schritte mit Protokoll (`ORBIS-VERF Art. 7`).

---

## 3. Branch-Konvention

- Es wird **nie direkt auf `main`** gearbeitet oder committet.
- Arbeitsbranches folgen dem Muster `<bereich>/<kurzbeschreibung>`:

  | Praefix | Verwendung |
  |---|---|
  | `befund/` | Neue oder praezisierte Befunde, z. B. `befund/l-11-kongruenz-distanz` |
  | `korpus/` | Neue Testsaetze, z. B. `korpus/tests-fragesaetze` |
  | `tools/` | Validator, Migration, Werkzeuge, z. B. `tools/lexikon-schema-pruefung` |
  | `docs/` | Dokumentation und Uebersetzungen, z. B. `docs/en-glossar` |
  | `chore/` | Aufraeumen, CI, Formatierung ohne Inhaltswirkung |

- Branches, die im Auftrag der Sprachdesigner laufen, behalten ihren beauftragten Namen
  (derzeit `claude/aufgabe-bbjpbm`).
- Ein Branch, ein Thema. Migration und Inhaltsaenderung werden nicht vermischt — sonst ist
  hinterher nicht mehr trennbar, ob eine Kennzahl durch den Umbau oder durch die Sprache
  gewandert ist.
- Kein Force-Push auf gemeinsame Branches.

---

## 4. Was ein guter Beitrag ist

### 4.1 Befunde

Der wichtigste Beitrag. Ein Befund haelt eine fehlende, widerspruechliche oder unklare Regel
fest, ohne sie zu entscheiden.

Ein guter Befund:

- nennt **einen** Fall, nicht fuenf,
- belegt ihn mit Paragraph, Testnummer oder Validator-Ausgabe,
- trennt Beobachtung von Deutung,
- sagt ausdruecklich, welche Frage offen bleibt,
- schlaegt keine Loesung als Loesung vor. Optionen sind willkommen — als Optionen mit Kosten
  und Folgen, ohne Auswahl.

Format, Marker (`[REGELLUECKE]`, `[REGELKONFLIKT]`, `[REGELUNKLARHEIT]`), ID-Vergabe und
Registereintrag sind in `AGENTS.md` Abschnitt 7 beschrieben; die Regeln gelten fuer Menschen
und Werkzeuge gleichermassen. Kurz:

- Neue Befunde erhalten die naechste freie Nummer ihrer Klasse (`K-06`, `L-11`, `U-15`, `W-02`).
- IDs werden nie wiederverwendet und nie umnummeriert.
- Die Prioritaet (P0…P4) ist im Beitrag immer ein **Vorschlag**; die Einstufung nehmen die
  Sprachdesigner vor.

### 4.2 Testsaetze

Neue Korpustests machen die Sprache pruefbar. Ein guter Testbeitrag:

- prueft **ein** Phaenomen und benennt es,
- verwendet ausschliesslich vorhandenen Wortschatz — kein Test erfindet ein Wort,
- nennt die Paragraphen, gegen die geprueft wird,
- fuehrt die deutsche Bedeutung als kanonische Angabe und die englische als abgeleitete
  (`TRANSLATION_POLICY.md`),
- markiert Saetze, deren korrekte Form von einer offenen Entscheidung abhaengt, als `open` mit
  Verweis auf den Befund — statt eine Form zu waehlen.

Wichtig: Neue Tests **erhoehen** die Testzahl bewusst (additiver Corpus-Minor). Bestehende
Tests, ihre IDs und ihre Bewertungen bleiben dabei unveraendert. Ein zurueckgezogener Test
wird als zurueckgezogen markiert, nicht geloescht (`VERSIONING.md` §3.5).

### 4.3 Uebersetzungen

Englische Fassungen sind offizieller Bestandteil der Dokumentation — aber abgeleitet.

- Uebersetzt wird **aus der deutschen kanonischen Bedeutung**, nie aus dem Orbis-Wort, seinem
  Klang oder seiner Etymologie.
- Der Bedeutungsumfang bleibt erhalten: kein engerer, kein weiterer, kein praeziserer Begriff.
- Traegt kein englisches Wort den Umfang, wird umschrieben und der Rest im `usage_note`
  (deutsch) dokumentiert — die Nuance wird nicht weggeglaettet.
- Faellt beim Uebersetzen eine Unschaerfe der deutschen Fassung auf, ist das ein **Befund**,
  keine Gelegenheit zur Korrektur in der Uebersetzung.
- `translation_status` setzt der Beitrag hoechstens auf `derived`; `reviewed` vergeben
  ausschliesslich die Sprachdesigner.

Vollstaendige Regeln: `TRANSLATION_POLICY.md`.

### 4.4 Werkzeuge

Werkzeuge sind willkommen, solange sie pruefen und nicht entscheiden.

- Ein Werkzeug liest Sprachdaten aus `language/` bzw. `script/`. **Sprachregeln werden nicht
  als Python-Konstanten dupliziert** — zwei Fassungen derselben Regel driften auseinander, und
  ab dann bestaetigt der Validator seine eigene Kopie statt die Sprache.
- Ein Werkzeug ist deterministisch: gleicher Input, zeichengleicher Output.
- Ein Werkzeug erfindet nichts. Fehlt eine Angabe, meldet es einen Befund und setzt keinen
  Platzhalter.
- Weicht ein Werkzeug von der Grammatik ab, gilt die Grammatik. Die Abweichung ist ein Befund
  und wird gemeldet, nicht "weggefixt".
- Python 3, Standardbibliothek, keine neuen Abhaengigkeiten ohne Ruecksprache.

### 4.5 Dokumentation

Beschreibende Dokumentation, Beispiele mit Quellenangabe, Aufbereitung von
Entscheidungsvorlagen, Glossare, Korrekturen an nicht kanonischen Dateien.

**Vorsicht bei generierten Dateien:** Traegt eine Datei einen `AUTO-GENERATED`-Kopf oder die
JSON-Kopffelder `quelle` / `erzeugt_von` / `hinweis`, wird sie nicht von Hand editiert. Statt
dessen wird der genannte Generator geaendert und die Datei neu erzeugt. Eine Handkorrektur
ist beim naechsten Lauf verloren — und sieht bis dahin richtig aus.

---

## 5. Was nicht ohne Entscheidung der Sprachdesigner geht

Die folgenden Aenderungen werden in einem Pull Request **nicht** angenommen, auch nicht in
guter Absicht und auch nicht als Nebenwirkung:

1. **Aenderungen an `Orbis-Grammatik-0.9.3.md`.** Die Datei ist eingefroren — auch Tippfehler,
   Nummerierung und Formatierung bleiben stehen. Korrekturen erscheinen in einer kuenftigen
   0.9.4, nie durch Ueberschreiben (`ORBIS-VERF Art. 4`).
2. **Neue Woerter, Wurzeln oder Affixe** — auch als Beispiel, Platzhalter oder Testmaterial.
3. **Uebernahmen aus realen Sprachen**, auch lautlich angepasst und auch bei
   "naheliegenden" Internationalismen (`ORBIS-VERF Art. 8`).
4. **Geaenderte Bedeutungen** bestehender Lexeme — auch Praezisierungen sind Aenderungen
   (`ORBIS-VERF Art. 6`).
5. **Geschlossene Regelluecken**: L-01 (Genitivstellung), L-02 (Relativsatz), L-03
   (Fragewortkasus), L-04 (Reflexivpronomen), L-05 (Passiv-Agens), K-05 (Modalverb im
   Nebensatz) und alle weiteren offenen Befunde bleiben offen, bis ein ADR sie schliesst.
6. **Aufgeloeste Widersprueche** — etwa die Homonymie von *fai* oder die Silbenformenliste in
   §5.1, die den eigenen Wortschatz nicht deckt (K-01).
7. **Manus-Festlegungen**: Zeichenform, Strichstaerke (L-10), Zerlegung und deren
   Mehrdeutigkeit (L-09), Tastenzahl in §26.8 (U-10).
8. **Experimentelles als kanonisch**: Die Morphem-Ebene fuer Manus und Keyboard sowie die
   Wortspuren (Moeglichkeit, Erinnerung, gehoert/berichtet, selbst erlebt) sind
   **EXPERIMENTELL und NICHT KANONISCH** und duerfen nirgends als bestehende Orbis-Grammatik
   dargestellt werden (`ORBIS-VERF Art. 20`).
9. **Baselineanpassungen**: `--update-baseline` laeuft nur auf ausdruecklichen Auftrag. Eine
   Baseline zu verschieben, damit ein Lauf gruen wird, ist unzulaessig.
10. **Umbenennungen** von Dateien, IDs, Regelnummern oder Feldnamen ohne dokumentierte
    Entscheidung (`ORBIS-VERF Art. 7`).
11. **Bearbeitung von Archivdateien**: `archive/corpus/Orbis-Testkorpus-0.1.md` (mit Punkt) und alles unter
    `archive/`.

Wer eine solche Aenderung fuer noetig haelt, macht daraus einen **Befund** oder eine
**Entscheidungsvorlage** — beides ist ein willkommener Beitrag. Vorbild:
`decisions/Entscheidungsvorlage-0_9_4.md`, die Optionen mit Kosten und Folgeaenderungen
darstellt, ohne eine auszuwaehlen.

---

## 6. Pflichtchecks vor einem Pull Request

### 6.1 Die zwei Pflichtlaeufe

```
python3 orbis_validator.py --strict
python3 orbis_validator.py --corpus Orbis-Testkorpus-0_1.md
```

Erwartete Ausgabe im aktuellen Stand:

```
Strict-Lauf: 39 Befunde aktuell, 39 in der Baseline.
Keine neuen Befunde. OK.                      (Exit-Code 0)

== KORPUSPRÜFUNG Orbis-Testkorpus-0_1.md ==
(130 von 130 Orbis-Sätzen ohne automatischen Befund)
```

**Exit-Code 1 aus `--strict` bedeutet NEUE Befunde. Dann wird nicht committet.** Der richtige
Weg ist, die Ursache zu finden — nicht, die Baseline anzupassen.

Weitere Laeufe je nach Beitrag:

```
python3 orbis_validator.py --all         # Lexikon, Beispiele und Manus in einem Lauf
python3 orbis_validator.py --lexicon     # Phonotaktik, Dubletten
python3 orbis_validator.py --examples    # Beispielsaetze der Grammatik
python3 orbis_validator.py --tables      # Deklinations- und Konjugationstabellen
python3 orbis_validator.py --manus       # Silbenzerlegung des Grundwortschatzes
python3 orbis_validator.py --json DATEI  # maschinenlesbare Ausgabe
python3 orbis_validator.py --sim-l09     # Simulation zu L-09 — Analysewerkzeug, KEINE Sprachregel
```

### 6.2 Checkliste

- [ ] Beide Pflichtlaeufe gefahren, `--strict` mit Exit-Code 0.
- [ ] Korpuskennzahlen 150 / 130 / 14 / 3 / 2 / 1 unveraendert — oder die Aenderung ist
      gewollt, beauftragt und im `CHANGELOG.md` begruendet.
- [ ] `Orbis-Grammatik-0.9.3.md` unveraendert (`git status` zeigt es nicht an).
- [ ] Keine neuen Woerter, Bedeutungen, Regeln oder Zeichen entstanden.
- [ ] Offene Punkte als Befund mit ID dokumentiert, keiner durch Auslegung geschlossen.
- [ ] Generierte Dateien nur ueber ihren Generator geaendert.
- [ ] Deutsche Fassung vorhanden und kanonisch; englische Fassung abgeleitet.
- [ ] Dateien UTF-8 ohne BOM, Unix-Zeilenenden.
- [ ] `git diff` gelesen: Es ist genau das drin, was drin sein soll — kein `__pycache__/`,
      keine Probelauf-Protokolle, keine Scratch-Dateien.
- [ ] `CHANGELOG.md` gepflegt, wenn die Aenderung inhaltlich wirksam ist
      (`ORBIS-VERF Art. 14`).

### 6.3 Die Pull-Request-Beschreibung

Sie nennt:

- **Was** geaendert wurde und **warum**,
- die **tatsaechliche Ausgabe** der Pflichtlaeufe — nicht die Zusage, sie gefahren zu haben,
- betroffene **Befund-IDs**,
- was **offen** bleibt und was ausdruecklich **nicht entschieden** wurde.

Ein PR schliesst nie einen Befund; das tut allein ein ADR. Ein PR mit rotem CI-Lauf geht nicht
ins Review — die CI faehrt `--strict`, den Korpuslauf und eine JSON-Ladepruefung.

---

## 7. Sprachregel: Deutsch ist primaer

- **Deutsch ist Primaersprache und semantische Autoritaet.** Bedeutungen, Regeltexte, Befunde
  und Entscheidungen entstehen zuerst auf Deutsch.
- **Englisch ist sekundaere offizielle Dokumentationssprache**: abgeleitet, offiziell,
  zitierfaehig — aber nie Quelle einer Festlegung.
- **Bei Widerspruch gilt die deutsche Fassung.** Der Widerspruch wird zusaetzlich als Befund
  gemeldet und nicht durch stille Anpassung der deutschen Seite aufgeloest.
- Projektdateien werden auf Deutsch geschrieben, UTF-8 ohne BOM, Unix-Zeilenenden.
- Stil: nuechtern und praezise. Keine Marketingsprache, keine Werturteile ueber die Sprache,
  keine Modell- oder Produktnamen von Assistenzsystemen (zulaessig ist allein der vereinbarte
  Hinweis, dass Claude Code als Pruefwerkzeug dient).
- Nicht uebersetzt werden: Orbis-Lemmata, Befund-IDs, Regel- und Objekt-IDs, Dateinamen,
  Paragraphenverweise (`§26.8`), JSON-Feldnamen und die Marker `[REGELLUECKE]`,
  `[REGELKONFLIKT]`, `[REGELUNKLARHEIT]`.

---

## 8. Dateinamenskonventionen

- **Regel:** Versionsnummern in Dateinamen mit **Unterstrich**: `Orbis-Testkorpus-0_1.md`,
  `Orbis-Audit-0_1.md`, `Orbis-Testbericht-0_1.md`,
  `decisions/Entscheidungsvorlage-0_9_4.md`.
- **Ausnahme 1:** Die Referenzgrammatik traegt ihre Version mit Punkten:
  `Orbis-Grammatik-0.9.3.md`. Historisch gewachsen und nicht nachtraeglich zu vereinheitlichen,
  weil die Datei eingefroren ist.
- **Ausnahme 2:** `archive/corpus/Orbis-Testkorpus-0.1.md` (mit Punkt) ist der archivierte Chat-Entwurf. Der
  Punkt ist hier kein Formatfehler, sondern das Unterscheidungsmerkmal zur kanonischen Fassung
  mit Unterstrich. Die Archivfassung wird weder bearbeitet noch als Quelle verwendet.
- Artefakte in `language/`, `script/`, `tools/`, `tests/`, `docs/` und `reports/` tragen die
  Version **im Inhalt** (Metadatenfeld), nicht im Dateinamen — so brechen Verweise nicht bei
  jedem Versionssprung.
- Historische Fassungen wandern nach `archive/` und behalten ihren Originalnamen. Sie werden
  nie ueberschrieben.

Merksatz: Unterstrich ist die Regel; der Punkt markiert entweder die eingefrorene Grammatik
oder die Archivfassung des Korpus — nie etwas Drittes.

---

## 9. Wohin welche Datei gehoert

| Was du beitraegst | Wohin |
|---|---|
| Sprachdaten (Phonologie, Morphologie, Syntax, Lexikon, Proto, Korpus) | `language/` im jeweiligen Unterverzeichnis |
| Neuer oder praezisierter Befund | `language/findings/` (Register) und der zugehoerige Bericht |
| Neue Korpussaetze | `language/corpus/` bzw. `Orbis-Testkorpus-0_1.md` |
| Lexikoneintrag (`ORB-LEX-*`) | `language/lexicon/entries/`, Schema: `language/lexicon/lexicon.schema.json` |
| Schriftdaten, Glyphen, Zerlegung | `script/manus/`, `script/magna/`, `script/traces/` |
| Werkzeug oder Skript | `tools/` (`validator`, `lexicon`, `corpus`, `documentation`, `migration`) |
| Testfall fuer Werkzeuge oder Daten | `tests/` im passenden Unterverzeichnis |
| Dokumentation deutsch / englisch | `docs/de/` (kanonisch) / `docs/en/` (abgeleitet) |
| Entscheidung (ADR, `ORB-ADR-*`) | `docs/decisions/` — angelegt von den Sprachdesignern |
| Laufprotokoll, Messstand | `reports/` |
| Historische Fassung | `archive/` — unveraendert, nie als aktuelle Quelle |
| Tastaturbelegung | `keyboard/` — setzt eine nummerierte Manus-Fassung voraus |

Nicht hineingehoert:

- Sprachregeln in Programmcode (`tools/`) statt in `language/`.
- Berichte oder Prosa in `language/`.
- Grammatikregeln in `script/` — Schrift und Grammatik werden getrennt gefuehrt
  (`ORBIS-VERF Art. 19`).
- Etwas noch Gueltiges in `archive/`.
- Leere Platzhalterdateien, damit eine Struktur vollstaendig aussieht.

Im Zweifel: Die Datei dorthin legen, wo sie gesucht wuerde, und die Frage im Pull Request
stellen. Ein falsch abgelegter, gut belegter Beitrag ist leicht zu verschieben.

---

## 10. Wenn etwas unklar ist

Unklarheit ist hier ein normaler Zustand und kein Versaeumnis. Der richtige Umgang damit:

1. Nicht raten. Nicht "vorlaeufig" festlegen. Nicht durch Auslegung schliessen.
2. Den Fall als Befund beschreiben — mit Beleg und mit der ausdruecklichen Angabe, welche
   Frage offen bleibt.
3. Wenn hilfreich: Optionen mit Kosten und Folgeaenderungen aufbereiten, ohne eine
   auszuwaehlen.
4. Die Entscheidung den Sprachdesignern ueberlassen.

Ein unfertiger Beitrag mit sauberem Befund ist ein gutes Ergebnis. Ein fertiger Beitrag mit
einer geratenen Regel richtet Schaden an, der erst Versionen spaeter sichtbar wird.

---

*Claude Code wird in diesem Projekt ausschliesslich als Pruef- und Werkzeug-Assistent
eingesetzt, nicht als Sprachdesigner.*
