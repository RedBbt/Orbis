# ORBIS — Formenlehre: Überblick

*Beschreibt Orbis-Grammatik 0.9.3. Diese Datei ist Dokumentation, nicht die Referenz.*

---

## 1. Gegenstand und Aufbau dieses Kapitels

Die Formenlehre von Orbis umfasst alles, was an einem Wort flektiert oder abgeleitet
wird: Geschlecht, Kasus und Numerus beim Nomen (§6–§11), Kongruenz und Steigerung
beim Adjektiv (§12), Person, Numerus und Tempus beim Verb (§14–§16) sowie die
Wortbildung (§21). Dieses Kapitel gibt den Überblick; die Einzelheiten stehen in den
Kapiteln, auf die es verweist.

| Kapitel | Datei | Gegenstand |
|---|---|---|
| Nomen | `docs/de/NOMEN.md` | §6–§11: 45 Endungen, vier Fälle, Plural, unregelmäßige Nomen, Artikel |
| Verben | `docs/de/VERBEN.md` | §14–§16: Konjugation, Zeiten, unregelmäßige Verben, Modalität, Passiv |
| Adjektive | `docs/de/ADJEKTIVE.md` | §12: attributiv, prädikativ, Steigerung, Adverb, Nominalisierung |

Nicht Gegenstand der Formenlehre sind Satzbau (§17–§20), Lautsystem (§2–§5),
Betonung (§23) und die Schrift Orbis Manus (§26). Manus- und Schriftregeln werden hier
nicht mit Grammatikregeln vermischt.

---

## 2. Das Aufbauprinzip

Orbis baut seine Wortformen agglutinierend von links nach rechts auf. Die
Grundformel steht in §8:

> **Stamm + Klassenkonsonant + Themavokal + Kasusmarker**

Für das Nomen ergänzt §6 den Zweck der beiden mittleren Bausteine: Der
**Klassenkonsonant** trägt das Geschlecht, der **Themavokal** gehört fest zum Wort und
sorgt für Klangvielfalt. Der Plural schiebt sich nach §9 zwischen Themavokal und
Kasusmarker.

Am vollständig belegten Beispiel *valruñuş* (Dativ Plural von *valru* „Mann", §9):

| Position | Bestandteil | Funktion | Paragraph |
|---|---|---|---|
| 1 | *val-* | lexikalischer Stamm | §8 |
| 2 | *-r-* | Klassenkonsonant, maskulin (Unterklasse M-A) | §7.1 |
| 3 | *-u-* | Themavokal | §6 |
| 4 | *-ñ-* | Pluralmarker | §9 |
| 5 | *-u-* | Echovokal (nur in den obliquen Fällen) | §9, U-09 |
| 6 | *-ş* | Kasusmarker Dativ | §8 |

Die Grammatik führt keine Liste lexikalischer Nominalstämme; sie gibt die Formel (§8)
und die fertigen Formen. Wo ein Stamm ausdrücklich belegt ist, lässt sich der Aufbau
direkt zeigen — §21.1 dokumentiert die Wurzel **mel-** „gehen" mitsamt ihrer Wortfamilie:

| Form | Aufbau | Klasse | Bedeutung |
|---|---|---|---|
| *melex* | mel- + -ex | Infinitiv | gehen |
| *melru* | mel- + r + u | M-A | Wanderer |
| *mela* | mel- + l + a, Fugenregel §21.4 | F-A | Wanderin |
| *melna* | mel- + n + a | N-A | Weg |
| *melisto* | mel- + -isto | N-C | Fahrzeug |
| *melvi* | mel- + -vi | Adjektiv-Grundform | reiselustig |
| *meluma* | mel- + -uma | F-C | Reise |

Dasselbe Muster ist in §21.1 an der Wurzel *tal-* „sprechen" ein zweites Mal
durchgeführt (*talex, talru, tala, talna, talisto, talvi, taluma*).

---

## 3. Die drei Nomengruppen

Die Grammatik teilt die Nomen in eine reguläre Hauptgruppe und zwei historisch
erklärte Restgruppen. Ausführlich: `docs/de/NOMEN.md`.

| Gruppe | Umfang laut Grammatik | Kennzeichen | Singular | Plural | Paragraph |
|---|---|---|---|---|---|
| **Reguläre Nomen** | „etwa 90 % aller Nomen" | Klassenkonsonant + Themavokal sichtbar am Wortende | Kasusmarker direkt an den Themavokal | **-ñ-** + Echovokal | §6, §7, §8, §9 |
| **10-Prozent-Gruppe** | 3 Wörter namentlich geführt | Endvokal historisch geschwunden, Geschlecht am Restkonsonanten erkennbar | Bindevokal **-e-** + Kasusmarker | **nicht geregelt — L-07** | §10.1 |
| **15 Kernwörter** | 15 Wörter, abschließend aufgezählt | echte Ausnahmen, Geschlecht nur aus dem Wörterbuch | Bindevokal **-e-** + Kasusmarker | **-ei** + Kasusmarker | §10.2, §10.3, §24.1 |

Belege je Gruppe:

- regulär: *valru · valrun · valruş · valrus* (§8), Plural *valruñ · valruñun · valruñuş · valruñus* (§9)
- 10-Prozent-Gruppe: *velkran · velkranen · velkraneş · velkranes* (§10.1)
- Kernwörter: *kaun · kaunen · kauneş · kaunes*, Plural *kaunei · kaunein · kauneiş · kauneis* (§10.3)

Die Prozentangaben sind Aussagen der Grammatik über den Wortschatz insgesamt (§6:
„Bei etwa 90 % aller Nomen ist das Geschlecht sofort an der Endung erkennbar"), nicht
eine Auszählung der in 0.9.3 namentlich geführten Wörter.

---

## 4. Das Verb

> **Wurzel + Tempusvokal + Personendung** (§14)

Der Tempusvokal ist **-a-** (Gegenwart), **-o-** (Vergangenheit) oder **-ai-** (Zukunft,
§15); die Personendungen sind **-m · -ş · -t** im Singular und **-men · -şen · -ten** im
Plural (§14). Beleg: *milkam · milkoş · milkait · milkaten* aus dem vollständigen
Paradigma von *milkex* „sehen" (§15.1).

Das Verb hat keinen Klassenkonsonanten und keinen Themavokal — die Nominalformel aus
§8 gilt für das Verb nicht. Acht häufige Verben weichen im Stamm ab (§15.2); Einzelheiten
in `docs/de/VERBEN.md`.

---

## 5. Das Adjektiv

Das Adjektiv hat zwei Zustände (§12):

| Zustand | Form | Beleg |
|---|---|---|
| attributiv | Stamm + **r / l / n** + **a** + Marker, kongruent mit dem Nomen | *xra vlaidra valru* (§12.1) |
| prädikativ | unveränderte Grundform nach *esex*, *vurnex*, *stanex* | *Lo loşn est.* (§12.2) |

Der attributive Baustein **r / l / n + a** ist derselbe wie beim Artikel (§11) — die
A-Reihe der Klassenkonsonanten. Adjektiv und Artikel zeigen damit immer nur das
Geschlecht, nie die Unterklasse des Nomens: *xnañaş vlaidnañaş milneñeş* (§12.1).
Einzelheiten in `docs/de/ADJEKTIVE.md`.

---

## 6. Was die Klangregeln nicht mitzählen (§3.5)

Die Klangrichtlinien (§3.4) gelten **ausschließlich für den lexikalischen Stamm**.
Grammatische Morphologie darf ein Wort niemals nachträglich klanglich „ungültig" machen.
Ausdrücklich nicht mitgezählt werden (§3.5):

- Kasusmarker *-n, -ş, -s*
- Pluralmarker *-ñ-* samt Echovokal und *-ei*
- die 45 Geschlechtsendungen
- Personendungen *-m, -ş, -t, -men, -şen, -ten*
- Tempusmarker *-a-, -o-, -ai-*
- reguläre Adjektivendungen *-ra, -la, -na* …
- Infinitiv *-ex* und Partizip *-ut*
- produktive Ableitungsmorpheme *-ru, -la, -na, -isto, -uma, -vi, şu-, xa-, re-, dra-, su-*

Belegtes Beispiel der Grammatik: *milkaiten* ist einwandfrei, geprüft wird allein der
Stamm *milk-*.

---

## 7. Die Fugenregel (§21.4)

Eine Regel gilt quer durch die gesamte Formenlehre:

> **Treffen an einer Morphemfuge zwei identische Konsonanten aufeinander, verschmelzen
> sie zu einem.** Das gilt für Zusammensetzungen, Ableitungen und Endungen gleichermaßen.

| Anwendungsbereich | Beleg | Paragraph |
|---|---|---|
| Zusammensetzung | *luiv + vresto* → *luivresto* | §21.3, §21.4 |
| Ableitung | *mel + la* → *mela*, *tal + la* → *tala* | §21.1, §21.4 |
| Adjektivendung | *şaln + na* → *şalna*, *girn + na* → *girna*, *xarn + na* → *xarna* | §12.1 |
| Steigerungsinfix | *selv + vi* → *selvi*, *zilv + vira* → *zilvira* | §12.3 |

Für unterschiedliche Konsonanten gilt sie nicht; sie bleiben erhalten, sofern §5.2 und
§5.3 sie zulassen (belegt: *şaln + la* → *şalnla*, Testkorpus 0.1 Test 058 *şalnlaş*).

Zwei belegte Formen widersprechen dieser Regel: die Pronomen *killa, dolla, kella*
(§13.4, §18.2) mit unverschmolzener *l+l*-Fuge — **[REGELKONFLIKT] K-02** — und die Zahl
*telnxelmmern* „35" (§24.8) mit *m+m*-Fuge — **[REGELKONFLIKT] K-03**. Beide sind hier
nicht auflösbar.

---

## 8. Offene Punkte der Formenlehre

Diese Dokumentation entscheidet nichts. Wo die Grammatik 0.9.3 schweigt oder sich
widerspricht, steht die Befund-ID aus `Orbis-Audit-0_1.md` §A.

| ID | Typ | Betrifft | Kurz |
|---|---|---|---|
| K-02 | Konflikt | §13.4, §18.2 ↔ §21.4 | *killa/dolla/kella* gegen die Fugenregel |
| K-03 | Konflikt | §24.8 ↔ §21.4 | *telnxelmmern* gegen die Fugenregel |
| K-04 | Konflikt | §25.1 ↔ §12.4 | Beispielsatz nutzt *tolm* adverbial statt *tolmun* |
| L-03 | Lücke | §18.2 | Deklination von *kem/kelt* |
| L-04 | Lücke | §13.4 | Kasusformen des Reflexivums *se* |
| L-06 | Lücke | §13.4 | Deklination der Demonstrativa und Indefinita |
| L-07 | Lücke | §10.1 | Plural der 10-Prozent-Gruppe |
| L-08 | Lücke | §24.8 | Syntax der Kardinalzahlen |
| U-01 | Unklarheit | §15.2 | Die Formel deckt *es-/nuv-/vurn-* nicht |
| U-02 | Unklarheit | §12, §14 | Partizip attributiv verwendbar? |
| U-08 | Unklarheit | §21.3 | Deklination von Komposita mit Kernwort-Kopf (*taivbreun*) |
| U-09 | Unklarheit | §9 | „Echovokal" ist nur durch die Tabellen definiert |
| U-12 | Unklarheit | §14 | Imperativ-Stütz-e prüft §5.3, nicht §5.1 |

Ein weiterer Befund berührt die Formenlehre nur mittelbar: **K-01** (§5.1 führt die
Silbenformen VK/VKK/KKVKK nicht, obwohl *aul, eird, em, eş, est* und flektierte Formen
wie *trelmrañan* sie brauchen).

---

*Dokumentation zur Grammatik 0.9.3. Bei Abweichung gilt `Orbis-Grammatik-0.9.3.md`.*
