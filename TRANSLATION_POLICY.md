# TRANSLATION_POLICY — Sprach- und Uebersetzungspolitik fuer Orbis

Status: verbindlich
Gilt fuer: Repository RedBbt/Orbis, alle Ebenen (Grammatik, Lexikon, Korpus, Berichte, Governance)
Bezug: CLAUDE.md, Orbis-Grammatik-0.9.3.md (READ ONLY), Orbis-Audit-0_1.md

Dieses Dokument regelt, in welchen Sprachen Orbis-Inhalte gefuehrt werden, welche
Sprache im Konfliktfall gilt und welche Felder auf welcher Ebene vorhanden sein
muessen. Es regelt nicht den Inhalt der Sprache Orbis selbst.

---

## 1. Grundsatz

- **Deutsch ist PRIMARY LANGUAGE und semantische Autoritaet.** Die deutsche
  Bedeutungsangabe ist die kanonische Bedeutung eines Lexems, einer Regel oder
  eines Korpussatzes.
- **Englisch ist SECONDARY OFFICIAL DOCUMENTATION LANGUAGE.** Englische Fassungen
  sind offizieller Bestandteil der Dokumentation, aber abgeleitet.
- **Bei Widerspruch zwischen deutscher und englischer Fassung gilt die deutsche
  Fassung.** Der Widerspruch ist zusaetzlich als Befund zu melden und nicht durch
  stille Anpassung der deutschen Seite aufzuloesen.
- Englische Fassungen duerfen die kanonische Bedeutung weder erweitern noch
  verengen noch praezisieren. Wer beim Uebersetzen eine Praezisierung fuer noetig
  haelt, meldet dies als Regelluecke oder Regelunklarheit an die Sprachdesigner,
  statt sie in der englischen Fassung vorwegzunehmen.
- Weitere Sprachen sind derzeit nicht vorgesehen. Sollten sie eingefuehrt werden,
  gelten sie ebenfalls als abgeleitet aus dem Deutschen, nie aus dem Englischen.

---

## 2. Geltungsbereich

Diese Politik gilt fuer:

| Ebene | Beispiele | Deutsch | Englisch |
|---|---|---|---|
| Grammatikdokumentation | Grammatik, Regelbeschreibungen, `ORB-GRAM-*` | kanonisch | abgeleitet |
| Lexikoneintraege | `ORB-LEX-*`, Konzepte `ORB-CON-*` | kanonisch | abgeleitet, Pflicht nach Migration |
| Korpussaetze | `ORB-SENT-*`, Testkorpus | kanonisch | Pflicht |
| Berichte | Test-, Validator-, Manus-Berichte | kanonisch | optional |
| Governance-Dateien | README, CLAUDE.md, Entscheidungen `ORB-ADR-*` | kanonisch | optional |
| Schrift und Tastatur | Manus `ORB-MANUS-*`, Keyboard | kanonisch | optional |

"Optional" heisst: eine englische Fassung darf fehlen; existiert sie, unterliegt
sie vollstaendig dieser Politik.

Die eingefrorene Referenzgrammatik `Orbis-Grammatik-0.9.3.md` wird durch diese
Politik nicht geaendert. Eine englische Fassung der Grammatik ist eine eigene,
zusaetzliche Datei und ersetzt die deutsche nie.

---

## 3. Pflichtfelder je Ebene

### 3.1 Lexem (canonical, `ORB-LEX-*`)

| Feld | Status |
|---|---|
| `de.short` | Pflicht |
| `de.definition` | Pflicht |
| `en.short` | Pflicht nach Abschluss der Migration |
| `en.definition` | Pflicht nach Abschluss der Migration |
| `usage_note` | bedingt Pflicht (siehe Abschnitt 5) |
| `translation_status` | Pflicht (siehe Abschnitt 6) |

- `de.short`: knappe Bedeutungsangabe, in der Regel ein bis drei Woerter.
- `de.definition`: vollstaendige Bedeutungsangabe inklusive Bedeutungsumfang und
  Abgrenzung zu benachbarten Lexemen.
- Waehrend der laufenden Migration ist ein Lexem mit fehlenden englischen Feldern
  gueltig; nach Abschluss der Migration ist es unvollstaendig.
- Lexeme mit Status `experimental` oder `proposed` sind von der englischen
  Pflicht ausgenommen, solange sie nicht `canonical` sind.

### 3.2 Korpussatz (`ORB-SENT-*`)

| Feld | Status |
|---|---|
| `orbis` | Pflicht |
| `de` | Pflicht |
| `en` | Pflicht |
| `translation_status` | Pflicht |

Ausnahme: offene Saetze ohne kanonische Orbis-Form, siehe Abschnitt 8.

### 3.3 Regel (`ORB-GRAM-PHON/MOR/SYN-*`, `ORB-MANUS-*`)

| Feld | Status |
|---|---|
| `de.title`, `de.text` | Pflicht |
| `en.title`, `en.text` | optional, wenn vorhanden dieser Politik unterworfen |

---

## 4. Ableitungsregel

1. Die englische Fassung wird **aus der deutschen kanonischen Bedeutung**
   abgeleitet.
2. Die englische Fassung wird **nicht aus dem Orbis-Wort erraten**, nicht aus
   dessen Klang, Wurzel, Etymologie oder Aehnlichkeit zu realsprachlichen
   Woertern.
3. Der **Bedeutungsumfang muss erhalten bleiben**. Ein englisches Wort mit
   engerem oder weiterem Umfang als die deutsche Angabe ist keine gueltige
   Uebersetzung.
4. **Keine woertliche Ersetzung, wenn sie den Umfang veraendert.** Traegt kein
   einzelnes englisches Wort den Umfang, wird eine Umschreibung verwendet oder
   der Rest im `usage_note` dokumentiert.
5. Rueckwirkung ist unzulaessig: Aus der englischen Fassung darf nie eine
   Aenderung der deutschen Bedeutung abgeleitet werden.
6. Uebersetzung erzeugt keine Sprachdaten: Beim Uebersetzen entstehen keine neuen
   Orbis-Woerter, Wurzeln oder Affixe.

Beispielhafte Fehlermuster, die zu vermeiden sind:

- Deutsch `de.definition` nennt einen Oberbegriff, Englisch setzt einen
  spezifischeren Unterbegriff ein (Verengung).
- Deutsch grenzt gegen ein Nachbarlexem ab, Englisch waehlt ein Wort, das beide
  Lexeme abdeckt (Verschmelzung).
- Englisch uebernimmt eine Konnotation, die im Deutschen nicht steht (Zusatz).

---

## 5. Umgang mit Nicht-Uebersetzbarem

- Bedeutungsnuancen, die das Englische nicht 1:1 traegt, werden im Feld
  `usage_note` dokumentiert.
- **Nicht glaetten**: Die englische Fassung darf die Nuance nicht dadurch
  aufloesen, dass sie sie weglaesst oder durch eine naheliegende, aber falsche
  Entsprechung ersetzt.
- Der `usage_note` benennt konkret, was fehlt: Umfangsunterschied, Register,
  Abgrenzung zu einem Nachbarlexem, fehlende Kategorie im Englischen.
- Der `usage_note` wird auf Deutsch gefuehrt; eine englische Fassung des
  `usage_note` ist optional.
- Ein `usage_note` ist Pflicht, wenn die englische Fassung den Umfang der
  deutschen Angabe nachweislich nicht vollstaendig abbildet.
- Der `usage_note` ist Dokumentation, keine Regel. Er begruendet keine
  grammatische Festlegung und wird nicht als Grammatikquelle zitiert.

---

## 6. Status-Werte fuer Uebersetzungen

Feld `translation_status`, genau ein Wert je Eintrag und Zielsprache:

| Wert | Bedeutung |
|---|---|
| `missing` | Keine englische Fassung vorhanden. Zulaessig waehrend der Migration, nach deren Abschluss ein Befund. |
| `draft` | Englische Fassung vorhanden, aber nicht nach Abschnitt 4 aus der deutschen Bedeutung abgeleitet oder noch unvollstaendig. Nicht zitierfaehig. |
| `derived` | Englische Fassung regelkonform aus der deutschen kanonischen Bedeutung abgeleitet, aber noch nicht von den Designern geprueft. |
| `reviewed` | Englische Fassung von den Sprachdesignern geprueft und freigegeben. |

- Der Wechsel nach `reviewed` erfolgt ausschliesslich durch die Sprachdesigner.
- Aenderungen an der deutschen kanonischen Bedeutung setzen abhaengige
  Uebersetzungen von `reviewed` oder `derived` auf `draft` zurueck.
- Werkzeuge duerfen `missing` → `draft` → `derived` setzen, nie `reviewed`.

---

## 7. Was NICHT uebersetzt wird

Unveraendert in jeder Sprachfassung bleiben:

- **Orbis-Lemmata selbst** (Woerter, Wurzeln, Affixe, Formen der Sprache Orbis).
- **Befund-IDs**: `K-01`..`K-05`, `L-01`..`L-10`, `U-01`..`U-14`, `W-01`.
- **Regel-IDs**: `ORB-GRAM-PHON-*`, `ORB-GRAM-MOR-*`, `ORB-GRAM-SYN-*`,
  `ORB-MANUS-*`, sowie `ORB-LEX-*`, `ORB-CON-*`, `ORB-SENT-*`, `ORB-ADR-*`.
- **Dateinamen** und Verzeichnisnamen, einschliesslich ihrer Versionsanteile.
- Paragraphenverweise auf die Grammatik (zum Beispiel `§26.8`).
- Feldnamen und Schluessel in JSON-Daten.

Marker wie `[REGELLUECKE]`, `[REGELKONFLIKT]` und `[REGELUNKLARHEIT]` bleiben in
der deutschen Form; in englischen Fassungen darf eine Erlaeuterung danebenstehen,
der Marker selbst wird nicht ersetzt.

---

## 8. Sonderfall offene Saetze

- Fuer Korpussaetze ohne kanonische Orbis-Form (weil eine Regelluecke, ein
  Regelkonflikt oder eine Regelunklarheit die Form offen laesst) wird **keine
  Uebersetzung als kanonisch ausgegeben**.
- Solche Saetze tragen den Status `open`.
- Beim Status `open` gilt:
  - Das Feld `de` beschreibt die beabsichtigte Bedeutung, nicht eine bestaetigte
    Orbis-Form.
  - Das Feld `en` ist optional und, falls vorhanden, ausdruecklich nicht
    kanonisch.
  - Das Feld `orbis` bleibt leer oder enthaelt ausschliesslich als solche
    gekennzeichnete Kandidaten.
  - Der zugehoerige Befund (`K-xx`, `L-xx`, `U-xx`) wird referenziert.
- Ein Satz verlaesst den Status `open` erst, wenn die Sprachdesigner die
  zugrunde liegende Regelfrage entschieden haben. Werkzeuge und Pruefassistenten
  entscheiden sie nicht.

---

## 9. Pruefung

- **CI prueft das Vorhandensein der Pflichtfelder, nicht die Qualitaet der
  Uebersetzung.** Geprueft werden: Existenz und Nichtleere der Pflichtfelder je
  Ebene, Gueltigkeit des `translation_status`-Werts, Konsistenz zwischen Status
  und Feldbestand (zum Beispiel: `derived` ohne `en.definition` ist ein Fehler),
  `usage_note`-Pflicht laut Abschnitt 5, Sonderfall `open` laut Abschnitt 8.
- **Die Qualitaet der Uebersetzung pruefen die Sprachdesigner.** Semantische
  Treue, Umfangserhalt und Registerwahl sind keine maschinellen Kriterien.
- Verstoesse gegen Pflichtfelder werden als Befund gemeldet und nicht durch
  automatisch erzeugte Platzhaltertexte verdeckt.
- Waehrend der laufenden Migration ist `missing` bei englischen Lexemfeldern
  kein CI-Fehler, sondern eine Warnung; nach Abschluss der Migration wird sie
  zum Fehler.
- Claude Code dient in diesem Repository ausschliesslich als Pruef- und
  Werkzeug-Assistent und trifft keine Uebersetzungs- oder Sprachentscheidungen.
