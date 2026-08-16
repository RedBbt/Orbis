# ORBIS — Aufbau des Lexikons

*Beschreibt Orbis-Grammatik 0.9.3. Diese Datei ist Dokumentation, nicht die Referenz.*

---

## 1. Was das Lexikon ist

Der Wortschatz von Orbis steht in §24 der Grammatik — als Listen, thematisch geordnet, mit
kurzer deutscher Glosse. Ab Version 0.9.3 ist er **eingefroren** (§24): Ein Wort wird nur
noch geändert, wenn es gegen die Phonotaktik verstößt, grammatisch inkonsistent ist,
problematisch mit einem anderen Wort kollidiert oder eine widersprüchliche Bedeutung
trägt. Geschmacksfragen reichen nicht mehr.

Das Lexikon unter `language/lexicon/` ist die **maschinenlesbare Fassung genau dieses
Bestands**. Es fügt keine Wörter hinzu und ändert keine Bedeutung; es macht die Angaben der
Grammatik prüfbar, verweisbar und generierbar. Weicht es von der Grammatik ab, gilt die
Grammatik — die Abweichung ist ein Befund.

| Datei | Inhalt |
|---|---|
| `language/lexicon/index.json` | Gesamtverzeichnis, 281 Einträge mit Datei-Zeiger |
| `language/lexicon/entries/<lemma>.json` | ein Eintrag je Grundform |
| `language/lexicon/lexicon.schema.json` | Schema eines Eintrags |
| `language/lexicon/concepts/concepts.json` | 131 Bedeutungskonzepte (`ORB-CON-*`) |
| `language/lexicon/concept.schema.json` | Schema eines Konzepts |
| `language/lexicon/word_families.json` | die zwei in §21.1 belegten Wortfamilien |

Zur Bedeutungsmodellierung (Konzept ↔ Lexem, Relationen, Synonymdifferenzierung) siehe
`SEMANTIK.md`.

---

## 2. Bestandsübersicht

**281 Grundformen · 131 Konzepte · Lexicon 0.1 gegen Grammar 0.9.3.**

Die 281 sind Grundformen im Sinne des Lexikons: Wörterbuchformen der offenen Klassen und
zusätzlich die vollständig aufgezählten Formen der geschlossenen Klassen (Artikel,
Personalpronomen). Flektierte Formen offener Wörter — *valrun, milkaten, vlaidnañaş* —
sind keine Einträge; sie werden aus den Paradigmen erzeugt (`docs/generated/de/PARADIGMEN.md`).

### 2.1 Nach Wortart

| Wortart | Einträge | Herkunft in der Grammatik |
|---|---|---|
| **nomen** | 71 | 15 Kernwörter (§24.1) + 3 der 10-Prozent-Gruppe (§10.1) + 13 M (§24.2) + 15 F (§24.3) + 13 N (§24.4) + 9 Abstrakta auf -uma (§24.6) + 3 Zusammensetzungen (§21.3) |
| **pronomen** | 58 | 36 Personalpronomenformen (§13.1) + 6 Demonstrativa + *se* + *fai* + 5 Indefinita (§13.4) + 6 Fragewörter + *kelra/kella/kelna* (§18.2) |
| **artikel** | 36 | bestimmt 3 Genera × 4 Kasus × 2 Numeri + unbestimmt 3 × 4 (kein Plural, §11.2) |
| **verb** | 34 | 28 Verbwurzeln (§24.5, davon 8 unregelmäßig) + 6 Modalwurzeln (§16.1) |
| **adjektiv** | 20 | §24.7 |
| **partikel** | 20 | 16 Adverbien/Partikeln (§24.9) + 4 Grußformeln (§13.2) |
| **präposition** | 16 | §19 |
| **zahl** | 15 | 10 Grundzahlen + *munar*, *kraven* + 3 Komposita (§24.8) |
| **konjunktion** | 11 | 4 nebenordnende + 7 unterordnende (§20) |
| **Summe** | **281** | |

Die Konjunktionen *ze, vu, klas, xer* stehen in §24.9 zusammen mit den Partikeln, werden
im Lexikon aber nach ihrer Funktion in §20 als Konjunktion geführt. Das ist eine Einordnung
der Datenebene, keine Bedeutungsänderung.

### 2.2 Nach Konzeptbindung

131 der 281 Einträge verweisen auf ein Konzept `ORB-CON-*`: alle Nomen, Verben und
Adjektive sowie die sechs Fragepronomen. Die übrigen 150 sind Funktionswörter und
Flexionsformen geschlossener Klassen mit rein grammatischer Bedeutung. Einzelheiten in
`SEMANTIK.md` §2.2.

### 2.3 Dateinamen

Der Dateiname ist eine ASCII-Umschrift des Lemmas: *ş* → `sh` (*veiş* → `veish.json`,
*şirn* → `shirn.json`, *nauş* → `naush.json`, *şaul* → `shaul.json`). Homonyme bekommen
eine angehängte Ziffer: `fai.json` (Konjunktion „dass") und `fai__2.json`
(Relativpronomen), ebenso `kaun`/`kaun__2` und `vran`/`vran__2` — siehe Befund **W-03**.
Das Lemma selbst steht unverändert in Orbis-Standardschreibung im Feld `lemma`.

---

## 3. Pflichtfelder eines Eintrags

Das Schema kennt zwei Stufen: Felder, ohne die ein Eintrag nicht gültig ist, und Felder,
die ein Eintrag zusätzlich braucht, um **kanonisch** zu sein.

### 3.1 Pflicht für jeden Eintrag (`required`)

| Feld | Inhalt |
|---|---|
| `lexeme_id` | stabile ID `ORB-LEX-000000`. „Wechselt NIE, auch nicht bei Umbenennung des Lemmas." |
| `lemma` | Grundform in Orbis-Standardschreibung |
| `status` | einer der acht Statuswerte (Abschnitt 4) |
| `wortart` | eine von 13 Wortarten (nomen … wurzel) |
| `de` | `short` (Kurzglosse) und `definition` — **kanonisch und autoritativ** |
| `phonologie` | mindestens `phonemfolge` |
| `qualitaet` | `geprueft` und `validatorstatus` |

### 3.2 Zusätzlich für `status: canonical` (`required_for_canonical`)

`de.short` · `de.definition` · **`en.short`** · **`en.definition`** · `wortart` ·
`phonologie.phonemfolge` · `qualitaet.validatorstatus`

Nur ein kanonischer Eintrag darf ohne Warnung in offiziellen Beispielen verwendet werden
(Schema, Feld `status`).

**Stand 0.1:** Alle 281 Einträge tragen `status: canonical`, `de.short`, `de.definition`
und `en.short`. **`en.definition` ist bei keinem Eintrag gefüllt** — die deutsche
Definition ist bislang die migrierte Wörterbuchglosse in Satzform, die englische Fassung
beschränkt sich auf die Kurzglosse. Diese Lücke ist als **W-04** registriert
(Dokumentationslücke, P2, offen) und ausdrücklich Redaktionsarbeit der Sprachdesigner:
Werkzeuge dürfen Definitionen nicht selbst formulieren (ORBIS_CONSTITUTION Art. 6 und
Art. 16).

### 3.3 Die weiteren Feldgruppen

| Gruppe | Zweck | Stand 0.1 |
|---|---|---|
| `grammatik` | Genus, Klasse, Themavokal, erzeugte `kasusformen`, Konjugationsklasse, Rektion, Transitivität | aus den Regeldaten erzeugt |
| `phonologie` | `phonemfolge`, `silbifizierung` bzw. `silbifizierung_kandidaten`, `phonotaktik_status` | bei 77 Einträgen ist die Silbifizierung mehrdeutig → `null` plus Kandidatenliste (**L-09**) |
| `manus` | Schriftzerlegung, `ambiguitaet`, `befund` | `blocked`, wo L-09 greift; sonst `provisional` |
| `semantik` | `concept_ids`, `synonyme`, `relationen`, `konnotation`, `bedeutungsnuancen` | nur 18 `antonym`-Relationen belegt (§24.7) |
| `wortfamilie` | Wurzel, `family_id`, Ableitungen, Komposita | gefüllt für die zwei Familien aus §21.1 |
| `etymologie` | `status`, `proto_form`, `lautgesetze` | `unknown`, wo §22 nichts hergibt — es wird nichts rekonstruiert |
| `gebrauch` | Kollokationen, typische Konstruktionen | leer (W-04) |
| `beispiele` | Verweise auf `ORB-SENT-*` | die generierten Seiten lösen sie aus dem Testkorpus auf |
| `qualitaet` | `validatorstatus`, `offene_befunde`, `quelle` | vollständig gefüllt; `quelle` nennt den Paragraphen |

Das Feld `qualitaet.offene_befunde` ist der Anker zwischen Lexikon und Befundregister.
Verteilung im Bestand: **W-04** an allen 281 Einträgen, **L-09** an 77, **L-08** an 15,
**K-01** an 14, **L-06** an 11, **U-01** an 8, **K-05** und **U-03** an je 6, **W-03** an 4,
**L-07**, **U-07** und **K-02** an je 3, **L-03** an 2, sowie **K-03**, **L-02**, **L-04**
und **U-08** an je einem.

---

## 4. Statusmodell

Acht Werte, gestaffelt vom Entwurf bis zur Ablehnung:

| Status | Bedeutung |
|---|---|
| **draft** | Entwurf, noch nicht vorgelegt |
| **proposed** | den Sprachdesignern zur Entscheidung vorgelegt |
| **review** | in Prüfung |
| **canonical** | beschlossener Bestand — **nur dieser Status darf ohne Warnung in offiziellen Beispielen verwendet werden** |
| **deprecated** | überholt, aber noch dokumentiert |
| **historical** | historische Form (Proto-Orbis, ältere Schicht), nicht Gegenwartssprache |
| **experimental** | ausdrücklich als Experiment gekennzeichnet (ORBIS_CONSTITUTION Art. 20) |
| **rejected** | geprüft und verworfen; der Eintrag bleibt als Entscheidungsgedächtnis erhalten |

**Stand 0.1:** alle 281 Einträge `canonical`. Das ist folgerichtig — sie stammen
sämtlich aus dem eingefrorenen Wortschatz der Grammatik 0.9.3. Neue Wörter würden bei
`draft` beginnen und den Weg über `proposed` und eine dokumentierte Entscheidung nehmen
(Art. 4, Art. 5).

Die 131 Konzepte tragen dagegen durchgehend `status: draft` — die Wörter sind beschlossen,
ihre ausformulierten Bedeutungsdefinitionen noch nicht (W-04).

---

## 5. Häufigkeitsstufen

Das Feld `haeufigkeit` trägt neun Werte:

| Stufe | Lesart |
|---|---|
| **CORE** | Kernbestand, in jedem Text zu erwarten |
| **VERY_COMMON** | sehr häufig |
| **COMMON** | häufig |
| **STANDARD** | normaler Gebrauchswortschatz |
| **SPECIALIZED** | fachlich, bereichsgebunden |
| **RARE** | selten |
| **ARCHAIC** | altertümlich |
| **POETIC** | dichterisch |
| **UNRATED** | noch nicht eingestuft |

> **Diese Stufen sind ausdrücklich Zielwerte der Sprachdesigner, keine Korpusstatistik.**
> Das Schema formuliert es unmissverständlich: „Orbis-interne Zielhäufigkeit
> (designer_frequency), KEINE gemessene Korpusstatistik." Orbis hat keinen
> Verwendungskorpus, aus dem sich Häufigkeiten messen ließen; der Testkorpus 0.1 ist eine
> **Prüf**sammlung von 150 Sätzen und misst Regelabdeckung, nicht Wortgebrauch.

**Stand 0.1** — die Einstufung folgt bislang der Wortklasse, nicht einer Einzelbewertung:

| Stufe | Einträge | Zusammensetzung |
|---|---|---|
| **CORE** | 95 | 36 Artikelformen · 36 Personalpronomenformen · 15 Kernwörter (§24.1) · 8 unregelmäßige Verben (§15.2) |
| **VERY_COMMON** | 39 | 16 Präpositionen · 11 Konjunktionen · 6 Modalverben · 6 Fragewörter |
| **COMMON** | 32 | 20 Partikeln und Grußformeln · 12 Grundzahlen |
| **STANDARD** | 3 | die 10-Prozent-Gruppe *velkran, soralm, prilm* |
| **UNRATED** | 112 | 53 reguläre Nomen · 20 reguläre Verben · 20 Adjektive · 16 Pronomen aus §13.4/§18.2 · 3 Zahlkomposita |

Die Stufen **SPECIALIZED**, **RARE**, **ARCHAIC** und **POETIC** sind im Bestand 0.1 von
keinem Eintrag belegt. Auch die Felder `register` (alle `neutral`) und `lernstufe` (alle
`unbestimmt`) warten auf eine Designerentscheidung.

---

## 6. Wortschatzlücken — [W-01]

> **W-01 (P2, offen): Wortschatzlücken für die Grundkommunikation.**
> Es fehlen gängige Grundverben und eine Konstruktion:

| Fehlend | Lage |
|---|---|
| **sagen** | §24.5 definiert *tal-* als „sprechen". Testkorpus 104 („Sie sagt, dass sie kommt") ist deshalb als [TESTPROBLEM] gewertet: *Lo talat, fai lo vandat* würde die Bedeutung ohne Wörterbuchgrundlage verschieben. |
| **zeigen** | keine Wurzel im Bestand |
| **suchen** | keine Wurzel im Bestand; *traiv-* ist „finden", nicht „suchen" |
| **es gibt** | keine Existenzkonstruktion; *es-* ist Kopula (§15.2, §17.5) |

W-01 ist **kein Regelverstoß**, sondern eine Bestandslücke: Die Grammatik funktioniert,
der Wortschatz reicht für bestimmte Alltagssätze nicht. Der Testbericht 0.1 nennt zwei
Lösungsrichtungen — gezielte Neuwörter über die §22-Werkstatt oder eine dokumentierte
Bedeutungserweiterung vorhandener Wurzeln — und entscheidet keine von beiden. Bis zu einer
Entscheidung der Sprachdesigner wird die Lücke **benannt, nicht gefüllt** (CLAUDE.md §2,
ORBIS_CONSTITUTION Art. 16).

Daneben stehen die beiden Kollisionsbefunde des Wortschatzes: **W-02** (*velkran* =
Nominativ „Freundschaft" und Akkusativ von *velkra*) und **W-03** (Homonyme *fai*, *kaun*,
*vran*, *xa*). Beide sind in `SEMANTIK.md` §6 ausgeführt.

---

## 7. Generierte Detailseiten

Aus den Daten erzeugt `tools/documentation/build.py` je Eintrag eine Detailseite:

**`docs/generated/de/lexicon/`** — 281 Lemma-Seiten plus `INDEX.md` als Gesamtverzeichnis.
Die englische Entsprechung liegt unter `docs/generated/en/lexicon/`.

Jede Seite zeigt in fester Gliederung:

| Abschnitt | Inhalt |
|---|---|
| Kopf | Lemma, Kurzglosse, deutsche Definition |
| Stammdaten | ID, Wortart, Geschlecht, Klasse, Status, Häufigkeit, Domäne, Quelle (§-Verweis) |
| Englisch | abgeleitete Fassung mit Übersetzungsstatus |
| Deklination / Konjugation | die erzeugten Vollformen |
| Lautung und Schrift | Phonemfolge, Silbifizierung (oder Kandidaten bei L-09), Phonotaktikstatus, Manus-Status |
| Bedeutung | verknüpfte Konzepte, Relationen |
| Wortfamilie, Etymologie | Wurzel; bei fehlendem Beleg ausdrücklich „keine Herleitung dokumentiert" |
| Beispielsätze | aus dem Testkorpus, über die Lexem-Verknüpfung aufgelöst |
| Prüfstand | Validatorstatus, offene Befunde mit Klartext, Datum der letzten Prüfung |

Diese Seiten tragen den Kopf `AUTO-GENERATED — DO NOT EDIT DIRECTLY`. Korrekturen gehören
in die Daten unter `language/`, nicht in die generierte Datei. Ebenfalls generiert:
`docs/generated/de/PARADIGMEN.md` (Vollformentabellen) und
`docs/generated/de/BEFUNDE.md` (Befundregister mit allen 33 IDs).

---

## 8. Prüfung

Vor jeder Änderung an Sprachdaten oder Validator:

```
python3 orbis_validator.py --strict
python3 orbis_validator.py --corpus Orbis-Testkorpus-0_1.md
```

`--strict` vergleicht gegen `orbis_baseline.json`; Exit-Code 1 bedeutet **neue** Befunde.
Weitere Läufe: `--lexicon` (Wortschatz gegen Phonotaktik und Endungssystem), `--tables`
(erzeugte Paradigmen), `--manus` (Silbifizierungs-Mehrdeutigkeit, L-09), `--examples`
(Grammatikbeispiele). `--update-baseline` nur auf ausdrücklichen Auftrag.

---

## 9. Befundübersicht zu diesem Kapitel

| ID | Typ | Betrifft | Kurzfassung |
|---|---|---|---|
| **W-01** | WORTSCHATZLÜCKE | §24 | „sagen", „zeigen", „suchen", „es gibt" fehlen |
| **W-02** | WORTSCHATZKOLLISION | §10.1, §24.2 | Formkollision *velkran* |
| **W-03** | WORTSCHATZKOLLISION | §11, §13.4, §18.3, §20, §21.2, §24 | weitere Homonyme |
| **W-04** | DOKUMENTATIONSLÜCKE | §24 | 281 Einträge ohne ausformulierte Definition |
| **L-09** | REGELLÜCKE | §5, §26 | 77 Einträge mit mehrdeutiger Silbifizierung |

Vollständiges Register: `language/findings/findings.json` und
`docs/generated/de/BEFUNDE.md` (33 Befunde: 29 aus dem Audit, dazu W-01 bis W-04).
