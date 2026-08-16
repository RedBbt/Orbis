# ORBIS — Die Pronomen

*Beschreibt Orbis-Grammatik 0.9.3. Diese Datei ist Dokumentation, nicht die Referenz.*

---

## 1. Zwei Bestände mit sehr unterschiedlichem Reifegrad

§13 der Grammatik zerfällt in zwei ungleiche Hälften:

| Bereich | Regelstand | Befunde |
|---|---|---|
| **Personalpronomen** (§13.1–§13.3) | vollständig dekliniert, Höflichkeitsform und Possessiv geregelt | keine (Audit §9.1) |
| **Übrige Pronomen** (§13.4) | nur eine Formenliste ohne Deklination und ohne Syntax | L-02, L-04, L-06, dazu K-02 |

Dieses Kapitel behandelt beide Hälften getrennt. Abschnitt 2–4 beschreiben geregelten
Bestand, Abschnitt 5 die offenen Bereiche. Für die offenen Bereiche gilt durchgehend:
Die fehlenden Formen werden hier **nicht** ergänzt und **nicht** per Analogie erschlossen.

---

## 2. Personalpronomen (§13.1)

Neun Formenreihen, jede in vier Fällen. Die Tabelle steht in §13.1 vollständig; sie ist
hier unverändert wiedergegeben.

| | Nom | Akk | Dat | Gen |
|---|---|---|---|---|
| ich | **vim** | vin | viş | vis |
| du (vertraut) | **şet** | şen | şeş | şes |
| Sie (höflich) | **şevar** | şevan | şevaş | şevas |
| er | **ro** | ron | roş | ros |
| sie | **lo** | lon | loş | los |
| es | **no** | non | noş | nos |
| wir | **viñ** | viñan | viñaş | viñas |
| ihr | **şeñ** | şeñan | şeñaş | şeñas |
| sie (Pl) | **oñ** | oñan | oñaş | oñas |

### 2.1 Beobachtungen an der Tabelle

Die Kasusmarker sind dieselben wie beim Nomen (§8): **Nom —, Akk -n, Dat -ş, Gen -s**.
In den drei Pluralreihen (*viñ, şeñ, oñ*) und bei der Höflichkeitsform tritt vor dem
Marker ein **-a-** auf (*viñan, şeñaş, oñas, şevan*) — dieselbe Stelle, an der §9 beim
Nomen den Echovokal ansetzt. Der Nominativ **şevar** endet auf *-r*, die obliquen Formen
bauen auf *şeva-*.

Das ist eine Beschreibung der belegten Tabelle, **keine Ableitungsregel**: §13.1 gibt die
36 Formen als Liste und formuliert kein Bildungsmuster. Wer neue Pronomen bilden wollte,
hätte keine Regel — die Klasse ist geschlossen, die Frage stellt sich in 0.9.3 nicht.

Die Form **oñ** (sie Pl) hat die Silbenform VK, die §5.1 nicht führt — Teilfall des
Silbenformen-Konflikts **K-01**. Das betrifft die Phonotaktik, nicht die Deklination.

### 2.2 Belege

| Form | Beleg | Übersetzung |
|---|---|---|
| vim (Nom Sg 1) | *Vim vandam.* (Testkorpus 001–150, Test 005) | Ich komme. |
| vin (Akk Sg 1) | *Vim milkam vin.* (Test 032) | Ich sehe mich. |
| viş (Dat Sg 1) | *Vim dalvam viş xlan nauşen.* (Test 034) | Ich gebe mir Zeit. |
| vis (Gen Sg 1) | *xna breun vis* (§13.3) | mein Haus |
| şet (Nom Sg 2) | *Kelnan vreston leşnaş şet?* (Test 079) | Welches Buch liest du? |
| lo (Nom Sg 3 f) | *Lo saivat xlan taiven.* (Test 029) | Sie liebt die Sprache. |
| non (Akk Sg 3 n) | *Vim xa zavam non.* (Test 087) | Ich weiß es nicht. |
| viñ (Nom Pl 1) | *Viñ stanamen.* (Test 007) | Wir bleiben. |
| şeñ (Nom Pl 2) | *Kur maldaşen şeñ?* (Test 077) | Wo wartet ihr? |
| oñas (Gen Pl 3) | *xrañ valruñ oñas* (§13.3) | ihre Männer |

---

## 3. Höflichkeitsform (§13.2)

> **şevar verlangt das Verb in der 3. Person Plural.**

Die Höflichkeitsform ist damit nicht bloß ein weiteres Pronomen, sondern zieht eine
Kongruenzverschiebung nach sich: Das Pronomen steht im Singular der Anrede, das Verb
in der Pluralendung *-ten / -men / -şen* (§14).

| Anrede | Beleg | Übersetzung |
|---|---|---|
| vertraut | *Şet melaş.* (§13.2) | Du gehst. |
| höflich | *Şevar melaten.* (§13.2) | Sie gehen. |
| höflich, Frage mit Modalverb | *Valnaten şevar vin zaubex?* (§25.1; Test 114) | Können Sie mich hören? |

Die Grammatik führt die Höflichkeitsform ohne Pluralpendant: Eine eigene Form für die
höfliche Anrede mehrerer Personen nennt §13.1 nicht; *şevar* deckt beide ab, weil das
Verb ohnehin im Plural steht.

**Grußformeln** stehen in §13.2 unmittelbar bei der Höflichkeitsform:
**selvai** (Hallo) · **melai** (Auf Wiedersehen) · **selves** (Danke) · **praum** (Bitte).

---

## 4. Possessiv (§13.3)

Orbis hat **keine eigenen Possessivpronomen**. Die Rolle übernimmt der Genitiv des
Personalpronomens, und zwar **nachgestellt**:

| Orbis | Deutsch | Quelle |
|---|---|---|
| *xna breun vis* | mein Haus | §13.3 |
| *xla sarla şes* | deine Frau | §13.3 |
| *xrañ valruñ oñas* | ihre Männer | §13.3 |
| *Nunda melam vim dun xnaş breuneş vis.* | Heute gehe ich zu meinem Haus. | §25.1 |

Das Possessiv ist **unveränderlich**: *vis* bleibt *vis*, gleich in welchem Kasus das
Bezugsnomen steht (*dun xnaş breuneş vis* — Bezugsnomen im Dativ, Possessiv unverändert).
Der Kasus wird am Artikel und am Nomen markiert, nicht am nachgestellten Genitiv.

> **[REGELLÜCKE L-01] — berührt.** Für den **einfachen** Possessivfall ist die Stellung
> geregelt („nachgestellt", §13.3). Nicht geregelt ist die **Stapelung** von Genitivattribut
> und Possessiv: „Das Buch meines Freundes" könnte *xna vresto xras velkras vis* lauten
> oder anders geordnet sein; ob *vis* sich auf *vresto* oder auf *velkra* bezieht, ist der
> Form nicht anzusehen. Testkorpus 039 ist deshalb als [REGELLÜCKE] gewertet.
> Ebenso offen: die Stellung des Genitivattributs beim reinen Nomen-Genitiv
> (Test 036, *xna breun xras valrus* oder *xras valrus xna breun*).

### 4.1 Reflexiver Gebrauch der 1. und 2. Person

Der Testkorpus bildet reflexive Sätze der 1. und 2. Person über das gewöhnliche
Personalpronomen: *Vim milkam vin* („Ich sehe mich", Test 032), *Vim dalvam viş xlan
nauşen* („Ich gebe mir Zeit", Test 034). Beide Sätze sind formal regelkonform — sie
verwenden nur §13.1. Ob die Grammatik das so **vorsieht** oder ob stattdessen *se*
(§13.4) zu stehen hätte, sagt sie nicht; siehe L-04 in Abschnitt 5.2.

---

## 5. Die übrigen Pronomen (§13.4) — offener Bestand

§13.4 besteht aus einer einzigen Tabelle. Sie listet Grundformen und sonst nichts:
keine Deklination, keine Syntax, keine Kongruenzregel.

| Art | Formen laut §13.4 |
|---|---|
| Demonstrativ (dieser) | **kilra / killa / kilna** |
| Demonstrativ (jener) | **dolra / dolla / dolna** |
| Reflexiv | **se** |
| Relativ | **fai** |
| Indefinit | **kaun** (man) · **kelsu** (jemand) · **xakaun** (niemand) · **kelte** (etwas) · **xakelte** (nichts) |

### 5.1 Demonstrativa — [REGELLÜCKE L-06]

Die Dreierreihe *-ra / -la / -na* ist die A-Reihe der Klassenkonsonanten (§7) und damit
formgleich mit Artikel (§11) und attributivem Adjektiv (§12.1). Ein Deklinationsmuster
wird daraus in §13.4 aber **nicht** abgeleitet.

> **[REGELLÜCKE L-06] Deklination der Demonstrativa nicht definiert.**
> §13.4 nennt nur die Grundformen. Weder Kasus- noch Pluralformen sind angegeben, und ob
> die Wörter als Attribut (*killa sarla*) oder nur als selbstständiges Pronomen dienen,
> ist nicht gesagt. „Ich sehe diesen Mann" ist nicht regelgestützt bildbar.

**Einziger Beleg im gesamten Bestand:** *Kilna est xna traivute.* — „Dies ist das
Gefundene." (§25.2, Kurztext). Belegt ist damit ausschließlich der **Nominativ Neutrum
als selbstständiges Pronomen**. Jede weitere Form wäre Spekulation.

### 5.2 Reflexivpronomen se — [REGELLÜCKE L-04]

> **[REGELLÜCKE L-04] Kasusformen und Personenbereich von se sind undefiniert.**
> §13.4 listet *se* ohne jede Form. Es ist nicht gesagt, ob *se* indeklinabel ist oder ob
> es Kasusformen hätte (\**sen*, \**seş*), ob es nach Präpositionen stehen darf und für
> welche Personen es gilt.

Zwei Testsätze scheitern daran und sind als [REGELLÜCKE] gewertet:

| Test | Deutsch | Problem |
|---|---|---|
| 033 | Er sieht sich. | *Ro milkat se*(?) — der Akkusativ von *se* ist nicht definiert; *Ro milkat ron* hieße „er sieht ihn (einen anderen)". |
| 035 | Sie spricht über sich. | *Lo talat span se*(?) — *span* verlangt Dativ oder Akkusativ (§19); *se* hat weder die eine noch die andere Form. |

Die Lücke hat zwei Seiten: die fehlenden Formen **und** den fehlenden Personenbereich.
Solange nicht entschieden ist, ob 1. und 2. Person überhaupt *se* verwenden, bleibt auch
die in Abschnitt 4.1 beschriebene Praxis (*Vim milkam vin*) ohne ausdrückliche Deckung.

### 5.3 Relativpronomen fai — [REGELLÜCKE L-02]

Von allen Pronomenbefunden ist dieser der folgenreichste: Er blockiert nicht eine Form,
sondern einen **ganzen Satztyp**.

> **[REGELLÜCKE L-02] Der Relativsatz ist vollständig ungeregelt.**
> §13.4 nennt *fai* als Relativpronomen. Es fehlen: Kasusformen von *fai*, die
> Kongruenz mit dem Bezugswort (Genus, Numerus), die Verbstellung im Relativsatz und die
> Stellung des Relativsatzes im Gesamtsatz. §17 erwähnt Relativsätze nicht.

Vier Testsätze sind deshalb nicht bildbar: 100 („Der Mann, der kommt, ist mein Freund"),
101 („Die Frau, die ich sehe, spricht" — bräuchte einen Akkusativ \**fain*), 102 („Der
Mann, dem ich das Buch gebe, wartet" — bräuchte einen Dativ \**faiş*) und 149 (komplexer
Satz mit eingebettetem Relativsatz).

**Homonymie fai / fai.** Dieselbe Form *fai* ist in §20 die unterordnende Konjunktion
„dass" — belegt in *Vim zavam, fai şet zirna vandaiş* („Ich weiß, dass du morgen kommen
wirst", §25.1). Beide Wörter stehen im Lexikon als getrennte Einträge (`fai` Konjunktion,
`fai` Pronomen). Die Kollision ist als **W-03** registriert und bleibt offen; sie wird
ausdrücklich nicht durch eine beiläufige Umformulierung aufgelöst (ORBIS_CONSTITUTION
Art. 6 nennt genau diesen Fall als Beispiel).

### 5.4 Indefinitpronomen — [REGELLÜCKE L-06]

> **[REGELLÜCKE L-06] Deklination der Indefinita nicht definiert.**
> Wie bei den Demonstrativa sind nur die Grundformen gelistet. Obliquen Kasus („jemanden
> sehen", „mit niemandem sprechen") fehlt die Form.

**Beleg:** *Xakaun vandat.* — „Niemand kommt." (Test 088). Der Satz ist [OK], weil er nur
den Nominativ braucht; die Analyse vermerkt ausdrücklich „oblique Formen → L-06".
*xakaun* ist zugleich ein Beispiel für die Vorsilbe **xa-** (§21.2, Gegenteil/Fehlen) auf
der Basis *kaun*.

**Homonymie kaun / kaun.** Das Indefinitum *kaun* „man" ist formgleich mit dem Kernwort
*kaun* „Mensch" (§24.1). Auch das ist unter **W-03** registriert, ebenso wie *vran*
(unbestimmter Artikel M Akk / Partikel „sehr") und *xa* (Negationspartikel / Vorsilbe).

### 5.5 Fragepronomen (§18.2) — [REGELLÜCKE L-03]

Die Fragewörter stehen in §18.2, nicht in §13, teilen aber die Problemlage von §13.4.

| Fragewort | Status |
|---|---|
| **kem** (wer), **kelt** (was) | nur Grundform; Kasusformen **nicht definiert** → L-03 |
| **kur, kan, grais, kolm** | unveränderlich gebraucht, keine Kasusfrage |
| **kelra / kella / kelna** (welcher/welche/welches) | kongruieren adjektivisch — belegt: *Kellan sarlan milkoş?* (§18.2) |

> **[REGELLÜCKE L-03] „Wen?", „Wem?", „Wessen?" sind nicht bildbar.**
> §18.2 listet *kem* und *kelt* nur in der Grundform. Weder Kasusformen (\**kemen*,
> \**kemeş*, \**kemes*) noch Indeklinabilität sind festgelegt. Tests 074, 075 und 076
> sind deshalb [REGELLÜCKE].

Bei *kelra/kella/kelna* ist die Lage besser, aber nicht vollständig: Belegt ist nur der
**Akkusativ** (*Kellan sarlan*). Testkorpus 079 (*Kelnan vreston leşnaş şet?*) und 080
(*Kelnaş şirneş dalvaş şet xnan brasin?*) folgen dem Adjektivparadigma §12.1 per Analogie;
080 ist ausdrücklich als Grenzfall zu L-03 vermerkt.

### 5.6 [REGELKONFLIKT K-02] — killa, dolla, kella gegen die Fugenregel

> **[REGELKONFLIKT K-02] Die Pronomenformen mit l+l widersprechen §21.4.**
> §21.4 lässt zwei identische Konsonanten an einer Morphemfuge verschmelzen und erklärt das
> ausdrücklich für „Zusammensetzungen, Ableitungen und **Endungen** gleichermaßen" — belegt
> an *mel + la → mela*, *tal + la → tala*, *şaln + na → şalna*. Die feminine Reihe der
> Pronomen behält die Fuge dagegen unverschmolzen:

| Form | Fuge | Nach §21.4 zu erwarten |
|---|---|---|
| **killa** (§13.4) | kil + la | \*kila |
| **dolla** (§13.4) | dol + la | \*dola |
| **kella / kellan** (§18.2) | kel + la | \*kela / \*kelan |

Entweder sind diese Formen Ausnahmen von §21.4 — dann sagt das keine Regel — oder sie
müssten anders lauten. Beides ist in 0.9.3 nicht entscheidbar; die Grammatik ist
eingefroren, der Konflikt bleibt stehen. Zum Gegenstück bei den Zahlen (*telnxelmmern*,
K-03) siehe `WORTBILDUNG.md`.

Die maskuline und die neutrale Reihe sind nicht betroffen: *kilra, kilna, dolra, dolna,
kelra, kelna* haben an der Fuge zwei verschiedene Konsonanten.

---

## 6. Befundübersicht zu diesem Kapitel

| ID | Typ | Betrifft | Kurzfassung |
|---|---|---|---|
| **L-02** | REGELLÜCKE | §13.4, §17 | Relativsatzbau fehlt vollständig; dazu Homonymie *fai* „dass" |
| **L-03** | REGELLÜCKE | §18.2 | Kasusformen von *kem/kelt* fehlen |
| **L-04** | REGELLÜCKE | §13.4 | Kasusformen und Personenbereich von *se* fehlen |
| **L-06** | REGELLÜCKE | §13.4 | Deklination der Demonstrativa und Indefinita fehlt |
| **L-01** | REGELLÜCKE | §8, §17 | Stellung des Genitivattributs, Stapelung mit Possessiv (berührt §13.3) |
| **K-01** | REGELKONFLIKT | §5.1 | *oñ* hat die von §5.1 nicht geführte Silbenform VK |
| **K-02** | REGELKONFLIKT | §13.4, §18.2 ↔ §21.4 | *killa/dolla/kella* gegen die Fugenregel |
| **W-03** | WORTSCHATZKOLLISION | §11, §13.4, §20 | Homonyme *fai*, *kaun*, *vran*, *xa* |

Vollständige Beschreibung aller Befunde: `Orbis-Audit-0_1.md` §A und
`docs/generated/de/BEFUNDE.md`. Entschieden wird über sie ausschließlich durch die
Sprachdesigner (ORBIS_CONSTITUTION Art. 16).
