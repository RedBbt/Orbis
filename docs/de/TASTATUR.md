# Orbis — Tastatur: Stand der Planung

*Beschreibt Orbis-Grammatik 0.9.3. Diese Datei ist Dokumentation, nicht die Referenz.*

---

## 1. Gegenstand und Status

Dieses Kapitel beschreibt, was die Grammatik in §26.8 zur Eingabe von Orbis Manus vorgibt,
wie die geplante Verarbeitungskette aussieht und warum sie derzeit nicht gebaut werden
kann. Es beschreibt einen **Planungsstand**, keine Spezifikation.

| Gegenstand | Stand |
|---|---|
| Orbis Keyboard | **keine freigegebene Fassung** (0.x); nicht als kompatibel geführt |
| Regelbasis | ausschließlich §26.8; die Tastatur hat **keine eigene Regelbasis** |
| Voraussetzung | eine nummerierte Manus-Fassung (`ROADMAP.md`, Phase F blockiert Phase G) |
| Blockade | **[REGELLÜCKE L-09]** (Silbifizierung), zusätzlich **[REGELLÜCKE L-10]** und **[REGELUNKLARHEIT U-10]** |

Die Richtung der Ableitung ist festgelegt: Ein Layout wird **aus** der Manus-Spezifikation
abgeleitet, nicht umgekehrt. Ein Layoutwunsch ändert keine Schriftregel. Solange L-09,
L-10 und U-10 offen sind, sind alle Layouts Entwürfe (`experimental`).

---

## 2. Was §26.8 vorgibt

### 2.1 Das Eingabeprinzip

> Eingabe wie beim koreanischen Hangul: Laute **in Sprechreihenfolge** tippen, das System
> setzt den Silbenblock zusammen.

Getippt wird also die Lautkette, dargestellt wird der fertige Silbenblock nach §26.1. Die
Tastatur ist damit keine Zeichenabbildung, sondern eine **Eingabemethode mit
Komponierschritt**.

### 2.2 Die Eingabereihenfolge

> **Kernkonsonant → zweiter Anfangskonsonant → Vokal → Coda 1 → Coda 2**

Die Reihenfolge entspricht Position für Position der Silbenformel §26.1. Zwei weitere
Festlegungen von §26.8:

| Festlegung | Wortlaut §26.8 |
|---|---|
| Blockabschluss | „Ein neuer Kernkonsonant schließt den vorherigen Block ab." |
| Interpunktion | „Das Abschlusszeichen liegt auf einer eigenen Taste." |

Der Blockabschluss ist implizit: Es gibt keine Bestätigungstaste für eine fertige Silbe.
Das Abschlusszeichen dagegen wird ausdrücklich getippt und ist damit die einzige
Sprachebene oberhalb der Silbe, die §26.8 der Tastatur zuweist.

### 2.3 Die Belegungsrechnung und [REGELUNKLARHEIT U-10]

§26.8 rechnet:

> **20 Konsonantentasten + 4 Vokaltasten + 1 Diphthongtaste + 6 Abschlusstasten = 31 Belegungen.**

**Befund-ID: U-10** (`Orbis-Audit-0_1.md` §21 und §A). Orbis hat **19** Konsonanten (§2.1);
die 20. Kernform ist nach §26.2 der **Vokalträger** und damit kein Konsonant. Korrekt wäre
„19 Konsonantentasten + 1 Vokalträgertaste"; die **Summe 31 bleibt richtig**. Das Audit
stuft den Punkt als Dokumentationsfehler ein, nicht als Systemfehler.

Für die Belegungsplanung ist der Unterschied dennoch praktisch: Die Vokalträgertaste ist
die Taste für vokalisch anlautende Silben (*aul*, *eird*, *ain*, *oñ*) und verhält sich in
der Eingabelogik anders als eine Konsonantentaste — sie eröffnet einen Block ohne
Anfangskonsonant. Die Korrektur des Wortlauts erscheint in einer künftigen
Grammatikversion, nicht durch Änderung der 0.9.3; diese Dokumentation markiert sie nur.

**Nicht ausgeführt in §26.8:** wie eine einzige Diphthongtaste die sechs Diphthonge aus
§26.4 erzeugt (dort ist jeder Diphthong Erstvokalzeichen plus kleiner zweiter Punkt).
Ebenfalls nicht ausgeführt: Zahlzeichen, Groß-/Auszeichnungsformen und das Verhalten bei
phonotaktisch unzulässiger Eingabe. Das Audit vergibt dafür keine Befund-IDs; hier wird
nichts ergänzt.

---

## 3. Architekturskizze der Verarbeitungskette

Die geplante Kette hat drei Stufen (`ROADMAP.md`, Phase G). Jede Stufe liest ausschließlich
aus `language/` bzw. `script/`; es gibt keine zweite Regelfassung im Code.

```
Eingabe (Lautkette + grammatische Merkmale)
        │
        ▼
  MorphologyEngine      Stamm + Kasus/Numerus/Tempus/Person  →  Wortform
        │                (language/morphology/, §8–§16)
        ▼
  Syllabifier           Wortform  →  Silbenfolge
        │                (language/phonology/, §5 — BLOCKIERT durch L-09)
        ▼
  ManusComposer         Silbenfolge  →  Manus-Silbenblöcke
        │                (script/manus/, §26.1–26.7)
        ▼
Ausgabe (Manus-Text, optional mit Abschlusszeichen §26.7)
```

### 3.1 Beispiel: *valru* + DATIV → *valruş* → Manus

| Stufe | Eingabe | Ausgabe | Grundlage |
|---|---|---|---|
| **MorphologyEngine** | *valru* (Mann, Klasse M-A, §24.2) + Dativ Singular | **valruş** | §8: Dativmarker **-ş**; belegte Reihe *valru · valrun · valruş · valrus* (§8) |
| **Syllabifier** | *valruş* | Silbenfolge — **nicht eindeutig bestimmbar** | §5.1 listet zulässige Silbenformen, aber keine Zerlegungsregel → **L-09** |
| **ManusComposer** | Silbenfolge | Silbenblöcke nach §26.1 | §26.2–26.6 |

Bei der Zerlegung *val·ruş* ergäbe der Composer zwei Blöcke:

| Block | Kernform | Beizeichen | Vokal | Coda |
|---|---|---|---|---|
| 1 | *v* (Familie ISH) | — | *a*, inhärent (nicht geschrieben, §26.4) | *l*, unten rechts (§26.5) |
| 2 | *r* (Familie TAL) | — | *u*, Punkt unten (§26.4) | *ş*, unten rechts (§26.5) |

Der Dativ ist im Schriftbild damit **kein eigenes Zeichen**, sondern die Coda des letzten
Blocks. Genau das ist der Punkt, an dem die experimentelle Morphem-Ebene ansetzen würde
(§5) — die Grammatik 0.9.3 kennt sie nicht.

Die Alternativzerlegung *valr·uş* ergäbe dagegen einen ersten Block mit **zwei** Codas
(*l* und *r*, gestaffelt nach §26.6) und einen zweiten Block mit **Vokalträger** statt
Kernkonsonant — ein sichtbar anderes Schriftbild für dieselbe Wortform.

> Nachgerechnet mit dem Zerlegungswerkzeug des Repos (Analysewerkzeug, **keine
> Sprachregel**): *valruş* hat gegen die wörtliche §5.1-Liste eine Zerlegung (*val·ruş*),
> gegen die um VK/VKK/KKVKK erweiterte Liste zwei (*val·ruş*, *valr·uş*). Die
> Grundform *valru* ist bereits im Schreibtest als mehrdeutig geführt (*val·ru* /
> *valr·u*, `Orbis-Manus-Schreibtest-0_1.md`). Welche Zerlegung gilt, ist offen: es hängt
> an **L-09** und zusätzlich an **[REGELKONFLIKT K-01]**, weil dieser über die erweiterte
> Formenliste entscheidet.

### 3.2 Weitere Anforderungen an die Kette

- **Rundlauftest** als Abnahmekriterium: Eingabe → Manus → Rückzerlegung → Ausgangsform,
  über den gesamten Lexikonbestand (`ROADMAP.md`, Phase G).
- **Fehlerverhalten** bei phonotaktisch unzulässigen Eingaben ist festzulegen; §26.8 sagt
  dazu nichts.
- **Plattformfrage** ist offen; für einen MVP zuerst eine Desktop-Belegung, mobile
  Eingabemethode später.
- **Keine Regelkopie im Code**: jede Zeichenzuordnung und jede Sprachregel hat genau eine
  maschinenlesbare Quelle.

---

## 4. Die Blockade durch [REGELLÜCKE L-09]

**Befund-ID: L-09** (`Orbis-Audit-0_1.md` §2.4 und §A, Priorität P2). Betrifft §5 und §26.

### 4.1 Warum die Kette an der mittleren Stufe stehenbleibt

§5 legt fest, welche Silben erlaubt sind — nicht, wie eine Lautkette zerlegt wird. Für die
Aussprache ist das folgenlos (§23 zählt Silben von hinten und liefert dasselbe Ergebnis);
für die Schrift nicht, weil §26.1 Silbe für Silbe schreibt. **77 von 281 Grundformen
(27 %) haben mehr als eine regelkonforme Manus-Schreibung**
(`Orbis-Manus-Schreibtest-0_1.md`; 203 eindeutig, 1 nicht zerlegbar). Bei flektierten
Formen steigt der Anteil, weil jede V-K-V-Folge zweideutig ist.

Der Syllabifier hat damit keine Regel, aus der er wählen könnte. Ein Programm, das
trotzdem wählt, träfe eine Sprachentscheidung — was Werkzeugen ausdrücklich untersagt ist.

### 4.2 Eingabereihenfolge gelöst, Rückübertragung nicht

Der entscheidende Punkt für die Tastatur (`Orbis-Manus-Schreibtest-0_1.md`, Abschnitt 3):

- **Gelöst durch §26.8:** die **Eingabereihenfolge**. Wer in Sprechreihenfolge tippt,
  bestimmt die Blockgrenzen selbst; „ein neuer Kernkonsonant schließt den vorherigen Block
  ab".
- **Nicht gelöst:** die **Rückübertragung** aus der Lateinschreibung. Dieselbe
  Buchstabenkette bleibt mehrdeutig — *mela* ist `[m;e;l] + [Träger;a]` **oder**
  `[m;e] + [l;a]`.

Das trifft genau die Funktionen, die eine benutzbare Eingabemethode braucht: Konvertierung
vorhandener Texte, Autovervollständigung aus dem Lexikon, Rundlauftest und jede Ausgabe,
die nicht Zeichen für Zeichen von Hand getippt wurde. Kernproblem bleibt: Nach einem Vokal
kann der nächste Konsonant Coda der laufenden Silbe, Kernkonsonant der nächsten Silbe oder
zweiter Anfangskonsonant sein.

### 4.3 Was zusätzlich offen ist

| Punkt | Wirkung auf die Tastatur |
|---|---|
| **L-09** Silbifizierung | Syllabifier ohne Regel; keine eindeutige Ausgabe, kein Rundlauftest |
| **L-10** Strichstärke *f s ş x v z j ç* | 8 von 19 Konsonanten ohne Zeichenparameter — betrifft die Darstellung, nicht die Belegung |
| **U-10** „20 Konsonantentasten" | Terminologie der Belegung; Summe 31 unberührt |
| **K-01** VK/VKK/KKVKK fehlen in §5.1 | entscheidet mit, welche Zerlegungen überhaupt zulässig sind |
| **Glyphensatz** | Zeichen-IDs, Formvarianten und Referenzformen liegen noch nicht vor (`ROADMAP.md`, Phase F) |

**Es wird hier keine Präferenzregel festgelegt und keine der offenen Fragen entschieden.**
Das Repo enthält eine Simulation (`python3 orbis_validator.py --sim-l09`), die
Kandidatenstrategien durchrechnet; der Testbericht nennt zusätzlich die Möglichkeit, freie
Varianz zu erklären und die Schrift mehrdeutig zu lassen. **Silbifizierungs-Simulationen
sind Analysewerkzeuge, keine Sprachregeln, und werden nie als Regel zitiert.** Die Auswahl
treffen ausschließlich die Sprachdesigner.

---

## 5. EXPERIMENTELL — NICHT KANONISCH

> **Dieser Abschnitt beschreibt Ideen, die nicht Bestandteil der Grammatik 0.9.3 sind.**
> Sie sind **EXPERIMENTELL und NICHT KANONISCH**, dürfen nirgends als bestehende
> Orbis-Grammatik, bestehendes Lexikon oder bestehende Schrift dargestellt werden und
> werden nicht in Sprachdaten, Korpussätze oder Prüfläufe übernommen. Kanonisch werden sie
> allein durch eine Entscheidung der Sprachdesigner.

### 5.1 EXPERIMENTELL — sichtbare Morphemzeichen

**Idee:** Eine Tastatur könnte grammatische Merkmale nicht nur als Laute setzen, sondern
sie im Schriftbild **sichtbar** machen — etwa Kasus-, Numerus- und Tempuszeichen als eigene
Marken am Silbenblock.

**Stand in der Grammatik 0.9.3:** In §26 gibt es dafür **kein Zeichen und keine Position**.
Der Dativ von *valru* ist in Manus die Coda *ş* des letzten Blocks (§3.1) und von jeder
anderen *ş*-Coda nicht unterschieden. Die Silbenformel §26.1 kennt genau fünf Positionen;
eine Morphemposition ist keine davon.

**Bedingungen, falls diese Ebene je sichtbar wird** (`ROADMAP.md`, Phasen F und G):

- ausschließlich als **abschaltbarer, klar markierter EXPERIMENTAL-Modus**,
- niemals als Voreinstellung und niemals in kanonischen Ausgaben,
- keine Darstellung als bestehende Orbis-Grammatik — an jeder Fundstelle mit Statusangabe,
- ob sie überhaupt sichtbar wird, entscheiden die Sprachdesigner.

### 5.2 EXPERIMENTELL — Wortspuren

**Idee:** Eine Evidenzebene, die anzeigt, woher eine Aussage stammt, mit vier Werten:

| Wortspur | Gedachte Bedeutung |
|---|---|
| **Möglichkeit** | die Aussage ist möglich, nicht gesichert |
| **Erinnerung** | die Aussage stammt aus Erinnerung |
| **gehört / berichtet** | die Aussage stammt von Dritten |
| **selbst erlebt** | die Aussage beruht auf eigener Erfahrung |

**Stand in der Grammatik 0.9.3:** Wortspuren kommen nicht vor — weder als Morphem, noch als
Partikel, noch als Schriftzeichen. Es gibt kein Orbis-Beispiel dafür, weder in der
Grammatik noch im Testkorpus.

**Nicht zu verwechseln mit dem kanonischen Bestand.** Für „Möglichkeit" hat Orbis bereits
zwei belegte Mittel, und beide sind Grammatik, nicht Wortspur:

| Kanonisches Mittel | Ebene | Beleg |
|---|---|---|
| Partikel **mai** vor dem finiten Verb (§16.2) | Morphologie/Syntax | *Vim mai melam.* — Ich würde gehen (§16.2) |
| Abschlusszeichen **verwehend** (§26.7) | Schrift/Pragmatik | „Möglichkeit, Ungewissheit (entspricht *mai*)" (§26.7) |

Für „Erinnerung", „gehört/berichtet" und „selbst erlebt" kennt die Grammatik **keine**
grammatische Kategorie. Das Nomen *soruma* (Erinnerung, §24.6, belegt in §25.1: *Xla
soruma xlas nauşes vran tolm vaşnat.*) ist ein Lexem, keine Evidenzmarkierung. Eine
Evidenzkategorie einzuführen wäre eine Sprachentscheidung und wird hier nicht getroffen.

Ablage im Repo: `script/traces/` — ausdrücklich als **EXPERIMENTELL, NICHT KANONISCH**
geführt und von `language/` getrennt.

### 5.3 Warum die Ebenen technisch getrennt modelliert werden

Die vier Ebenen werden getrennt modelliert, damit ein Experiment nicht per Zitat in den
kanonischen Bestand wandert und damit ein Befund der einen Ebene keinen Schritt auf einer
anderen auslöst:

| Ebene | Zuständig für | Ort im Repo | Status |
|---|---|---|---|
| **Phonologie** | Laute → Manus-Silben (Silbenbau, Zerlegung) | `language/phonology/` → `script/manus/` | kanonisch (§5, §26); Zerlegung offen: L-09 |
| **Morphologie** | Kasus, Numerus, Tempus (Wortformbildung) | `language/morphology/` | kanonisch (§8–§16) |
| **Evidenz** | Wortspuren (Möglichkeit, Erinnerung, gehört/berichtet, selbst erlebt) | `script/traces/` | **EXPERIMENTELL, NICHT KANONISCH** |
| **Pragmatik** | Satzabschlüsse (Aussage, Fortsetzung, Gegensatz, Frage, Möglichkeit, Ende) | `script/manus/` | kanonisch (§26.7) |

Praktische Folge für die Verarbeitungskette: Die MorphologyEngine erzeugt *valruş* aus
*valru* + Dativ, ohne etwas über Schriftzeichen zu wissen; der ManusComposer setzt
Silbenblöcke, ohne etwas über Kasus zu wissen; das Abschlusszeichen wird als eigene Ebene
gesetzt und nie als dritte Coda behandelt (§26.7); eine Evidenzebene existiert in keiner
kanonischen Stufe. Schriftregeln (§26, `script/`) und Grammatikregeln (`language/`)
bleiben getrennt versioniert.

---

## 6. Zusammenfassung des Regelstatus

| Punkt | Paragraph | Status |
|---|---|---|
| Eingabe in Sprechreihenfolge, Blockabschluss durch neuen Kernkonsonanten | §26.8 | vorgegeben, eindeutig |
| Abschlusszeichen auf eigener Taste | §26.8 / §26.7 | vorgegeben, eindeutig |
| Belegungsrechnung, Summe 31 | §26.8 | Summe richtig; **[REGELUNKLARHEIT U-10]** in der Benennung |
| Erzeugung der 6 Diphthonge über 1 Taste | §26.8 / §26.4 | nicht ausgeführt; keine Befund-ID |
| Fehlerverhalten, Zahlzeichen, Plattform | — | in §26 nicht geregelt; Arbeitspakete Phase G |
| Silbifizierung für den Syllabifier | — | **[REGELLÜCKE L-09]** — blockierend |
| Strichstärke *f s ş x v z j ç* | §26.9 | **[REGELLÜCKE L-10]** |
| Silbenformen VK/VKK/KKVKK | §5.1 | **[REGELKONFLIKT K-01]** |
| Morphemzeichen, Wortspuren | — | **EXPERIMENTELL, NICHT KANONISCH** |

---

## 7. Querverweise

| Thema | Ort |
|---|---|
| §26 vollständig: Kernformen, Vokalpunkte, Coda, Abschlusszeichen | `MANUS.md` |
| Feierliche Schriftform und ihre offenen Spiralregeln | `MAGNA.md` (§27) |
| Silbenformen, Anlautgruppen, Coda-Bedingungen, K-01 und L-09 | `PHONOTAKTIK.md` (§5) |
| Kasusmarker und Paradigmen (*valru · valrun · valruş · valrus*) | `NOMEN.md` (§8–§10) |
| Zerlegungstabelle aller 281 Grundformen | `Orbis-Manus-Schreibtest-0_1.md` |
| Befund-IDs L-09, L-10, U-10, K-01 | `Orbis-Audit-0_1.md`, `language/findings/findings.json` |
| Arbeitspakete und Abnahmekriterien | `ROADMAP.md` (Phasen F und G) |
| Kennzeichnungspflicht für Experimentelles | `ORBIS_CONSTITUTION.md` (Art. 20) |

---

*Quelle aller Regelaussagen: `Orbis-Grammatik-0.9.3.md` (READ ONLY). Bei Abweichung
zwischen dieser Dokumentation und der Grammatik gilt die Grammatik.*
