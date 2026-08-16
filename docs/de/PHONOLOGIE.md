# Orbis — Phonologie

*Beschreibt Orbis-Grammatik 0.9.3. Diese Datei ist Dokumentation, nicht die Referenz.*

---

## 1. Gegenstand

Dieses Kapitel beschreibt das Lautinventar von Standard-Orbis: die 19 Konsonanten und
5 Vokale aus §2.1–2.2, die Diphthonge aus §2.3 und die beiden Klanggruppen aus §3.2.
Es beschreibt ferner, welche dieser Aussagen **verbindlich** sind (§3.3) und welche
**beschreibende Richtlinien** ohne Verbotswirkung sind (§3.4, §3.5).

Die Verteilung der Laute auf Silben (Anfangs- und Endgruppen, Silbenformen) steht nicht
hier, sondern in `PHONOTAKTIK.md` (§5). Lautwerte und Betonung stehen in `AUSSPRACHE.md`
(§2, §4, §23). Die historische Herkunft der Formen steht in `PROTO_ORBIS.md` (§22).

---

## 2. Konsonanten (§2.1)

Orbis hat **19 Konsonanten**. Die Gruppierung und die Aussprachehinweise der folgenden
Tabelle stammen wörtlich aus §2.1; die Spalte „Belege" nennt Wörter des eingefrorenen
Wortschatzes (§24) bzw. der Beispielsätze (§25).

| Gruppe | Laute | Beschreibung laut §2.1 | Belege |
|---|---|---|---|
| Stimmlose Verschlusslaute | **p · t · k** | wie deutsch, ohne starke Behauchung | *xerp* Feuer, *pliso* Feder (§24) · *taiv* Sprache, *talru* Sprecher (§24) · *kaun* Mensch, *kavla* Stadt (§24) |
| Stimmhafte Verschlusslaute | **b · d · g** | wie deutsch | *breun* Haus, *brasi* Brot (§24) · *draun* Vater, *zaldre* Tag (§24) · *grein* Erde, *granz* alt (§24) |
| Affrikate | **ç** | wie *tsch* | **kein Beleg** — siehe §6 dieses Kapitels |
| Stimmlose Reibelaute | **f · s · ş · x** | *s* immer scharf; *ş* wie *sch*; *x* hinten im Rachen | *fai* dass (§20) · *sarla* Frau (§24) · *şirn* Kind (§24) · *xerp* Feuer (§24) |
| Stimmhafte Reibelaute | **v · z · j** | *z* wie in *Rose*; *j* wie französisch *jour* | *valru* Mann, *virn* Leben (§24) · *zaldre* Tag, *zaub-* hören (§24) · **kein Beleg für j** — siehe §6 |
| Nasale | **m · n · ñ** | *ñ* wie in *señor* | *moks* Tod, *mela* Wanderin (§24) · *nauş* Zeit (§24) · Pluralmarker *-ñ-*: *melruñ* die Wanderer (§25.1) |
| Fließlaute | **l · r** | *r* deutlich gerollt | *luiv* Sonne (§24) · *rusk-* schreiben (§24.5), *valru* Mann (§24) |

**Nicht vorhanden (§2.1):** *h, w, th, pf, ts* sowie *ng* als eigener Laut.

Zur Zählung: Die sieben Gruppen ergeben 3 + 3 + 1 + 4 + 3 + 3 + 2 = 19 Konsonanten.
§3.3 erklärt genau dieses Inventar für verbindlich — ein Wort mit einem anderen
Konsonanten ist kein gültiges Orbis.

---

## 3. Vokale (§2.2)

Fünf Vokale: **a · e · i · o · u**

§2.2 legt fest: „rein und klar, immer voll ausgesprochen. Kein Schwa, keine Reduktion.
Ein *e* am Wortende ist ein volles *e*."

| Vokal | Beleg |
|---|---|
| a | *sarla* Frau (§24.3) |
| e | *milne* Auge, *zaldre* Tag (§24) — Endungs-*e* ist voll |
| i | *brasi* Brot, *larki* Stein (§24) |
| o | *verno* Herz, *vresto* Buch (§24) |
| u | *skelnu* Himmel, *veltu* Jahr (§24) |

Es gibt keine Längen-, Dehnungs- oder Doppelschreibung (§4.1). Vokallänge ist in
0.9.3 nicht phonemisch geregelt und wird hier nicht ergänzt.

Zur Abschwächung von unbetontem **-a** in der Umgangsaussprache (*sarla* → [sarlə])
siehe §4.2 und `AUSSPRACHE.md` — das ist Ebene B, nicht Ebene A.

---

## 4. Diphthonge (§2.3)

§2.3 überschreibt den Abschnitt mit „Diphthonge (6)" und unterscheidet dabei
ausdrücklich zwischen **belegt**, **regulär aber unbelegt** und **offen**.

| Diphthong | Status laut §2.3 | Belege aus §2.3 / §24 |
|---|---|---|
| **ai** | belegt, im Wortschatz notwendig | *taiv, saiv-, traiv-, vlaid, taisa, mai*; Zukunftsvokal *-ai-* (§15) |
| **au** | belegt, im Wortschatz notwendig | *kaun, nauş, şaul, draun, zaub-, klaun, traus* |
| **ei** | belegt, im Wortschatz notwendig | *veiş, grein, eird*; Kernwort-Plural *-ei* (§10.3) |
| **ui** | belegt, im Wortschatz notwendig | *luiv, luid* |
| **eu** | belegt, im Wortschatz notwendig | *breun* — der einzige Beleg |
| **oi** | **regulär, aber derzeit unbelegt** | kein Wort des Lexikons; in Orbis Manus schreibbar (§26.4) |
| **ou** | **[NOCH ZU ENTSCHEIDEN]** (§2.3, §30) | keine — **nicht verwenden**, solange nicht entschieden |

**Zu *oi*:** §2.3 formuliert den Status ausdrücklich: *oi* „ist ein zulässiger produktiver
Diphthong und in Orbis Manus schreibbar. Er wird bisher von keinem Wort des Lexikons
benutzt und ist deshalb kein Beleg für die Notwendigkeit des Systems, sondern eine offene
Lücke, die neue Wörter füllen dürfen." *oi* ist damit erlaubt, aber unbelegt.

**Zu *ou*:** §2.3 und §30 führen *ou* als offenen Punkt. Ob es aufgenommen wird, ist eine
Entscheidung der Sprachdesigner. Bis dahin ist *ou* **kein** Bestandteil des Inventars und
darf in Wörtern, Testsätzen und Werkzeugen nicht verwendet werden. Diese Dokumentation
entscheidet die Frage nicht.

**Weitere Diphthonge werden nicht ergänzt** (§2.3).

Alle Diphthonge werden in **einer** Silbe gesprochen, „mit deutlichem Übergang und ohne
Verschleifung" (§2.3).

Zur Stellung im Wort gilt Richtlinie 4 (§3.4): höchstens ein Diphthong pro Wort,
bevorzugt in der betonten Silbe. Das ist eine Richtlinie, kein Verbot (siehe §5).

---

## 5. Klanggruppen und Regelstatus

### 5.1 Die zwei Lautgruppen (§3.2)

§3.2 teilt die 19 Konsonanten in zwei Klanggruppen:

| Gruppe | Laute |
|---|---|
| **Fließlaute** | l · r · n · m · ñ · v · z · s · j |
| **Härtelaute** | p · t · k · b · d · g · f · x · ş · ç |

§3.1 begründet die Einteilung: „Der Fluss kommt von **l, r, n, m, v, z, s**; die Härte von
**p, t, k, b, d, g, f, x, ş, ç**. Entscheidend ist das Verhältnis im **Gesamtwortschatz**,
nicht die Rechnung im Einzelwort."

Zu beachten: Die Klanggruppen aus §3.2 sind **nicht** identisch mit den artikulatorischen
Gruppen aus §2.1. *s* und *z* stehen artikulatorisch bei den Reibelauten, klanglich aber
bei den Fließlauten; *ş* und *x* stehen bei den Härtelauten. Die §3.2-Einteilung ist eine
Klangkategorie, keine phonetische.

Die Coda-Regel §5.3(a) verwendet dagegen den Ausdruck „Fließlaut oder Nasal (l, r, m, n)"
in einem engeren Sinn — dort sind nur diese vier Laute gemeint, nicht die neun aus §3.2.
Siehe `PHONOTAKTIK.md` §4.

### 5.2 Verbindlich: §3.3

§3.3 nennt die Bedingungen, unter denen ein Wort **kein gültiges Orbis** ist. Phonologisch
relevant sind die ersten drei Zeilen:

| Bereich | Regel (§3.3) |
|---|---|
| Phoneminventar | nur die 19 Konsonanten, 5 Vokale und 6 Diphthonge aus §2 |
| Silbenstruktur | nur V, KV, KVK, KKV, KKVK, KVKK (§5.1) |
| Anfangsgruppen | nur die Liste aus §5.2 |
| Endgruppen | nur nach den Bedingungen in §5.3 |

§3.3 schließt mit dem Satz: „Alles andere ist Klang, nicht Gesetz."

Zur Silbenstruktur-Zeile ist der Regelkonflikt **K-01** zu beachten: §5.1 führt nicht alle
Silbenformen, die der eingefrorene Wortschatz tatsächlich braucht. Siehe `PHONOTAKTIK.md`
§3.

### 5.3 Beschreibend: §3.4 und §3.5

§3.4 stellt fünf **Klangrichtlinien** auf und sagt dazu ausdrücklich: „Ein Wort wird
**nicht ungültig**, weil es davon abweicht. Sie sind Werkzeug beim Erfinden, nicht
Prüfstempel beim Zulassen."

| Nr. | Richtlinie (§3.4) | Kurzfassung |
|---|---|---|
| 1 | Flusstendenz | Im Gesamtwortschatz überwiegen die Fließlaute deutlich; nicht im Einzelwort nachgerechnet |
| 2 | Härtelaute | Typisch 0–2 Härtelaute im lexikalischen Stamm; mehr ist selten, aber nicht verboten |
| 3 | Wortausgang | Weiche Ausgänge auf Vokal oder *n, r, l, m, s* bilden die Mehrheit |
| 4 | Diphthongstellung | Höchstens ein Diphthong pro Wort, bevorzugt in der betonten Silbe |
| 5 | Silbengewicht | Alltagswörter 2 Silben, gewichtige/abstrakte Begriffe 3–4; Einsilber meist Funktions- oder Kernwörter |

Zu Richtlinie 2 nennt §3.4 als Beispiele phonologisch einwandfreier Formen: *kadru*,
*grondo*, Wurzel *kred-*. Zu Richtlinie 3 nennt §3.4 als belegte harte Ausgänge die
Verbstämme *milk-, nast-, rusk-* und die Kernwörter *xerp, moks, eird*.

**§3.5 begrenzt den Geltungsbereich:** Die Richtlinien gelten „**ausschließlich für den
lexikalischen Stamm**. Grammatische Morphologie darf ein Wort niemals nachträglich
klanglich ‚ungültig' machen."

Nicht mitgezählt werden laut §3.5:

- Kasusmarker (*-n, -ş, -s*)
- Pluralmarker (*-ñ-* samt Echovokal, *-ei*)
- Geschlechtsendungen (die 45 Endungen, §7)
- Personendungen (*-m, -ş, -t, -men, -şen, -ten*)
- Tempusmarker (*-a-, -o-, -ai-*)
- reguläre Adjektivendungen (*-ra, -la, -na* …)
- Infinitiv *-ex* und Partizip *-ut*
- produktive Ableitungsmorpheme (*-ru, -la, -na, -isto, -uma, -vi, şu-, xa-, re-, dra-, su-*)

Beleg aus §3.5: *milkaiten* ist ein einwandfreies Wort — geprüft wird nur der Stamm
*milk-*.

Der Begriff **Echovokal** in der Pluralmarker-Zeile ist in der Grammatik nirgends
definiert, sondern nur durch Tabellen in §9 belegt — Befund **U-09** (Regelunklarheit).

### 5.4 Nebenwirkung auf die Unterklassen (§3.6)

Die Klassenkonsonanten **k, d, t** sind selbst Härtelaute. Nomen der Unterklassen M-B,
M-C und N-C tragen deshalb tendenziell einen Härtelaut mehr als die A-Reihe (§3.6):
*narku* (M-B), *vrondo* (M-C), *vresto* (N-C) gegenüber *valru* (M-A), *sarla* (F-A).

§3.6 bezeichnet das ausdrücklich als „eine Beobachtung, keine Vorschrift". Ob daraus
zusätzlich eine grammatische Funktion wird, ist **[NOCH ZU ENTSCHEIDEN]** (§3.6, §30).

---

## 6. Offene Punkte und Beobachtungen

| Punkt | Status |
|---|---|
| Diphthong *ou* | **[NOCH ZU ENTSCHEIDEN]** (§2.3, §30) — nicht verwenden |
| Durchgehende Vokalharmonie | **[NOCH ZU ENTSCHEIDEN]** (§30) |
| Endgültige Konsonantenclusterliste | **[NOCH ZU ENTSCHEIDEN]** (§30) |
| Silbenformenliste §5.1 unvollständig | **[REGELKONFLIKT K-01]** — siehe `PHONOTAKTIK.md` |
| „Echovokal" nirgends definiert | **[REGELUNKLARHEIT U-09]** (§9) |
| Strichstärke für *f s ş x v z j ç* undefiniert | **[REGELLÜCKE L-10]** (§26.9) — betrifft Manus, nicht die Phonologie |
| Endgültige Funktion der Unterklassen | **[NOCH ZU ENTSCHEIDEN]** (§3.6, §30) |

**Beobachtung ohne Befund-ID:** Für die Affrikate **ç** und den stimmhaften Reibelaut
**j** enthält der eingefrorene Wortschatz 0.9.3 (§24, 281 erfasste Grundformen in
`language/lexicon/entries/`) **kein einziges Wort**. Beide Laute sind durch §2.1 und §3.3
regulärer Bestandteil des Inventars und in Orbis Manus mit eigenen Kernformen vertreten
(§26.2: Familie KAI für *ç*, Familie ISH für *v z j*) — sie sind lediglich unbelegt, wie
*oi*. Die Grammatik erklärt diese Lücke nicht und das Audit vergibt dafür keine Befund-ID;
hier wird sie nur festgehalten, nicht bewertet und nicht geschlossen.

---

## 7. Querverweise

| Thema | Ort |
|---|---|
| Silbenformen, Anfangs- und Endgruppen, Silbengrenzen | `PHONOTAKTIK.md`, Abschnitt 5 |
| Lautwerte, Umgangsaussprache, Betonung | `AUSSPRACHE.md` (§2, §4, §23) |
| Lautgesetze und Wortherleitung | `PROTO_ORBIS.md` (§22) |
| Schriftzeichen für Laute und Diphthonge | Grammatik §26 (Orbis Manus) |
| Befund-IDs und Regelbasis | `Orbis-Audit-0_1.md` |

---

*Quelle aller Regelaussagen: `Orbis-Grammatik-0.9.3.md` (READ ONLY). Bei Abweichung
zwischen dieser Dokumentation und der Grammatik gilt die Grammatik.*
