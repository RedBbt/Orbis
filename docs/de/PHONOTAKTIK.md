# Orbis — Phonotaktik

*Beschreibt Orbis-Grammatik 0.9.3. Diese Datei ist Dokumentation, nicht die Referenz.*

---

## 1. Gegenstand

Dieses Kapitel beschreibt §5 der Grammatik: welche Silbenformen erlaubt sind (§5.1),
welche Konsonantengruppen am Silbenanfang stehen dürfen (§5.2), unter welchen Bedingungen
zwei Konsonanten am Silbenende stehen dürfen (§5.3) und was §5.4 zu Wortlänge und
Wortausgang sagt.

Alle drei Regeln sind über §3.3 **verbindlich**: Ein Wort, das gegen sie verstößt, ist
kein gültiges Orbis. Das Lautinventar selbst steht in `PHONOLOGIE.md` (§2).

Ein zentraler Vorbehalt gilt für das ganze Kapitel: **Die Liste der Silbenformen in §5.1
ist unvollständig** (Regelkonflikt K-01, §3), und **eine Regel zur Silbentrennung existiert
nicht** (Regellücke L-09, §5). Beides wird hier benannt, nicht behoben.

---

## 2. Erlaubte Silbenformen (§5.1)

§5.1 nennt sechs Formen. K = Konsonant, V = Vokal oder Diphthong.

> **V · KV · KVK · KKV · KKVK · KVKK** (letzteres selten)

§5.1 selbst führt **keine Beispielwörter** auf. Die folgende Tabelle belegt jede Form
daher mit **einsilbigen** Wörtern der Grammatik, bei denen die Zuordnung eindeutig ist —
bei mehrsilbigen Wörtern hinge sie von der fehlenden Silbentrennungsregel ab (L-09, §7).

| Form | Aufbau | Einsilbige Belege |
|---|---|---|
| **V** | nur Vokal | **kein einsilbiger Beleg** — der Wortschatz enthält kein Wort aus einem bloßen Vokal. Offene V-Silben entstehen nur beim Zerlegen mehrsilbiger Wörter (z. B. *oñas* als *o·ñas*, §13.1) und hängen damit an L-09 |
| **KV** | Konsonant + Vokal | *ro* er, *lo* sie, *no* es (§13.1) · *xa* nicht, *ze* und, *vu* oder (§24.9) · *se* sich (§13.4) |
| **KVK** | Konsonant + Vokal + Konsonant | *kaun* Mensch, *nauş* Zeit, *şaul* Name (§24.1) · *vim* ich (§13.1) |
| **KKV** | Zweiergruppe + Vokal | *xra · xla · xna* bestimmter Artikel, *vra · vla · vna* unbestimmter Artikel (§11) · *zva* mit, *kru* auf (§19) |
| **KKVK** | Zweiergruppe + Vokal + Konsonant | *breun* Haus, *grein* Erde, *draun* Vater (§24.1) · *span* über, *şlim* zwischen (§19) |
| **KVKK** | Konsonant + Vokal + Zweiercoda (**selten**) | *virn* Leben, *moks* Tod, *xerp* Feuer (§24.1) · *tolm* langsam (§24.7) · *kalm* 4, *mern* 5, *xelm* 10 (§24.8) |

§3.3 verweist auf genau diese Liste und macht sie verbindlich. Drei und mehr Konsonanten
am Silbenanfang sind „ausnahmslos verboten" (§5.2); mehr als zwei Konsonanten in der Coda
lässt §5.3 nicht zu.

---

## 3. [REGELKONFLIKT K-01] — die Liste in §5.1 ist unvollständig

**Befund-ID: K-01** (`Orbis-Audit-0_1.md` §2.1 und §A). Priorität P1.

§5.1 führt weder **VK/VKK** (vokalisch anlautende geschlossene Silben) noch **KKVKK**
(Zweieranlaut + Zweiercoda). Beide Formen werden vom eingefrorenen Wortschatz und von den
Beispielen der Grammatik selbst gebraucht. Nach dem Wortlaut von §3.3 wären die
betroffenen Wörter „kein gültiges Orbis" — obwohl die Grammatik sie führt.

### 3.1 Fehlende Form VK / VKK

| Wort | Silbenform | Fundstelle |
|---|---|---|
| **aul** Wasser | VK | Kernwort §24.1; alle Formen *aulen, auleş, aules* §10.3 |
| **eird** Welt | VKK | Kernwort §24.1; alle Formen *eirden, eirdeş, eirdes* §10.3 |
| **ain** ja | VK | §24.9 |
| **oñ** sie (Pl.) | VK | Personalpronomen §13.1 |
| **est** er/sie/es ist | VKK | *esex*, §15.2 |
| **em**, **eş** ich bin / du bist | VK | *esex*, §15.2 |
| **aulmelna** Kanal | VK (erstes Glied) | Zusammensetzung §21.3 |

Beleg im laufenden Text der Grammatik: *„Lo loşn est."* — Sie ist schön (§12.2);
*„Vim xa valnam soñex, grali xla kirva vran luid est."* (§25.1).

### 3.2 Fehlende Form KKVKK

| Wort | Silbenform | Fundstelle |
|---|---|---|
| **granz** alt | KKVKK | Adjektiv §24.7 — und zugleich Coda-Beispiel in §5.3(a) |
| **trelm** lang | KKVKK | Adjektiv §24.7; flektiert *trelmrañan* §25.2 |
| **vresn** schwach | KKVKK | Adjektiv §24.7 |
| **skirm** wenig | KKVKK | Adverb §24.9 |
| **prilm** Handwerk | KKVKK | 10-Prozent-Gruppe §10.1 |
| **prens-** nehmen | KKVKK (Imperativ *Prens!*) | Verbwurzel §24.5 — und Coda-Beispiel in §5.3(b) |
| **dremn-** denken | KKVKK (Imperativ *Dremn!*) | Verbwurzel §24.5 |
| **vlent-** laufen | KKVKK (Imperativ *Vlent!*) | Verbwurzel §24.5 |

Beleg im laufenden Text: *„Xna breun granz stanat, klas xla kavla zirv vurt."* (§25.1);
*„Vra melru molet dral xrañan trelmrañan zaldreñen."* (§25.2).

### 3.3 Die Schärfe des Konflikts

§5.3 nennt **granz** und **prens** selbst als Beispiele für zulässige Codas. Die
Coda-Regel setzt damit Silbenformen voraus, die §5.1 nicht führt. Der Konflikt liegt
innerhalb von §5, nicht zwischen §5 und dem Lexikon allein.

**Nicht entscheidbar an dieser Stelle:** ob §5.1 um VK, VKK und KKVKK erweitert wird, ob
die betroffenen Wörter anders zerlegt werden sollen oder ob eine andere Auflösung gilt.
Das ist eine Designerentscheidung (Redaktionskandidat für 0.9.4). Werkzeuge des Repos
prüfen strikt gegen die **gelistete** Menge und melden Abweichungen als K-01, statt die
Liste stillschweigend zu erweitern (`language/phonology/syllable_shapes.json`,
`orbis_validator.py --lexicon | --examples`, Befundklasse „§5.1-BEFUND").

§30 führt „Endgültige Konsonantenclusterliste" ohnehin als **[NOCH ZU ENTSCHEIDEN]**.

---

## 4. Konsonantengruppen am Silbenanfang (§5.2)

**Maximal zwei Konsonanten. Drei oder mehr sind ausnahmslos verboten.**

Zulässig ist nur diese geschlossene Liste von **25** Gruppen (§5.2, Reihenfolge der
Grammatik):

> **tr · dr · kr · gr · pr · br · pl · bl · fl · vl · fr · vr · vn · sl · şl · şr · sk · st · sp · xr · xl · xn · zv · gl · kl**

Nach Bautyp geordnet, mit Belegen aus §24/§25:

| Typ | Gruppen | Belege |
|---|---|---|
| Verschlusslaut + *r* | **tr · dr · kr · gr · pr · br** | *trelm* lang · *draun* Vater · *kraven* 1000 · *grein* Erde · *prila* Hand · *breun* Haus |
| Verschlusslaut + *l* | **pl · bl · gl · kl** | *pliso* Feder · **bl unbelegt** · *gluvi* Flamme · *klaun* wahr |
| *f/v* + Liquid/Nasal | **fl · vl · fr · vr · vn** | **fl unbelegt** · *vlaiko* Wind · **fr unbelegt** · *vresto* Buch · *vnan* (Artikel, §11.2) |
| *s/ş* + Konsonant | **sl · şl · şr · sk · st · sp** | **sl unbelegt** · *şlim* zwischen · **şr unbelegt** · *skelnu* Himmel · *stan-* bleiben · *span* über |
| *x* + Konsonant | **xr · xl · xn** | *xra / xla / xna* (bestimmter Artikel, §11.1) |
| *z* + *v* | **zv** | *zva* mit (§19) |

**Beobachtung zur Belegung** (`Orbis-Audit-0_1.md` §2.2, nachgerechnet an
`language/lexicon/entries/`): **bl, fl, fr, sl, şr** sind zulässig, aber im eingefrorenen
Wortschatz durch **kein** Wort belegt. *fr* erscheint ausschließlich im §5.3-Beispielwort
*frisk*, das nicht im Wortschatz §24 steht. Das Audit vermerkt dazu ausdrücklich:
**kein Befund an der Liste selbst** — unbelegt heißt zulässig, nicht ungültig. Neue
Wörter dürfen diese Lücken füllen (analog zum Diphthong *oi*, §2.3).

---

## 5. Konsonantengruppen am Silbenende — Coda (§5.3)

**Maximal zwei Konsonanten.** Eine Zweiergruppe ist erlaubt, wenn **eine** der drei
Bedingungen zutrifft (die Bedingungen sind alternativ, nicht kumulativ):

| Bedingung | Wortlaut §5.3 | Beispiele der Grammatik |
|---|---|---|
| **(a)** | Der erste Laut ist Fließlaut oder Nasal (**l, r, m, n**) | *virn, xerp, tolm, teln, xarn, granz* |
| **(b)** | Der zweite Laut ist **s** | *moks, prens* |
| **(c)** | Die Gruppe ist **şn, sn, sk** oder **st** | *loşn, leşn, vesn, frisk, nast* |

Anmerkungen:

- Bedingung (a) verwendet „Fließlaut" **enger** als §3.2. Gemeint sind hier ausdrücklich
  nur *l, r, m, n* — nicht die neun Fließlaute der Klanggruppe (§3.2: l r n m ñ v z s j).
  Siehe `PHONOLOGIE.md` §5.1.
- Bedingung (c) ist eine geschlossene Liste von vier Gruppen. *sn* wurde erst in 0.9.3
  ergänzt; §29 hält fest, dass *vesn* (6), *vresn* (schwach) und *misn* (kurz) nach der
  Coda-Regel von 0.9.2 formal unzulässig waren — „ein Fehler aus 0.9.2, der die Wörter
  selbst nicht betrifft".
- Das Beispielwort *frisk* aus (c) steht **nicht** im Wortschatz §24 (siehe
  `Orbis-Testbericht-0_1.md`, Phase 7). Es belegt die Regel, nicht das Lexikon.
- Die Regel selbst ist eindeutig und maschinell prüfbar; das Audit vermerkt **keinen
  Befund an der Regel**. Der Konflikt betrifft nur die Silbenformenliste (K-01, §3).

Einzelkonsonanten in der Coda sind durch KVK/KKVK ohnehin gedeckt: *kaun, nauş, şaul,
şirn, mel-* (§24).

---

## 6. Wortlänge und Wortausgang (§5.4)

§5.4 ist kurz und ausdrücklich nachrangig:

> „Wortlänge und Wortausgang folgen den Richtlinien in §3.4 — sie sind Tendenz, nicht
> Gesetz. **Verbindlich ist allein §5.3.**"

Damit gilt: Ein Wort mit hartem Endkonsonanten oder ungewöhnlicher Silbenzahl ist
phonotaktisch korrekt, solange §5.1–5.3 eingehalten sind. Die Richtlinien 3 und 5 (§3.4)
beschreiben nur die Häufigkeitsverteilung — siehe `PHONOLOGIE.md` §5.3.

Belegte harte Ausgänge nennt §3.4 selbst: Verbstämme *milk-, nast-, rusk-* und Kernwörter
*xerp, moks, eird*.

---

## 7. [REGELLÜCKE L-09] — es gibt keine Silbentrennungsregel

**Befund-ID: L-09** (`Orbis-Audit-0_1.md` §2.4 und §A). Priorität P2. Betrifft §5 und §26.

§5 legt fest, welche Silben **erlaubt** sind. Nirgends legt die Grammatik fest, wie eine
Lautkette in Silben **zerlegt** wird — es gibt keine Onset-Maximierung, keine
Sonoritätsregel, keine Präferenz. Dadurch sind viele Wörter mehrfach regelkonform
zerlegbar:

| Wort | Mögliche Zerlegungen (alle §5-konform) |
|---|---|
| **mela** Wanderin (§24.3) | **me·la** (KV + KV) oder **mel·a** (KVK + V) |
| **kavla** Stadt (§24.3) | **kav·la** (KVK + KV) oder **ka·vla** (KV + KKV) |
| **drovna** Wald (§24.4) | **drov·na** (KKVK + KV) oder **dro·vna** (KKV + KKV) |
| **vresto** Buch (§24.4) | **vres·to**, **vre·sto** oder **vrest·o** |

**Wo die Lücke folgenlos ist:** für Aussprache und Betonung. Die Betonungsregel §23 zählt
Silben von hinten und liefert bei *mela* in beiden Zerlegungen dasselbe Ergebnis.

**Wo die Lücke wirkt:** in **Orbis Manus** (§26) und bei der Tastatureingabe (§26.8). Die
Manus-Silbenformel (§26.1: Kernkonsonant + optionaler zweiter Anfangskonsonant +
Vokalzeichen + 0–2 Endkonsonanten) schreibt Silbe für Silbe. Dieselbe Standardschreibung
hat deshalb mehrere zulässige Manus-Schreibungen: *mela* ist entweder
m-Kernform + e + l-Coda gefolgt von einem a-Vokalträger, **oder** m-Kernform + e gefolgt
von l-Kernform + a. Beide sind nach §5 und §26 korrekt.

**Quantifizierung:** **77 von 281 Grundformen** des Lexikons sind mehrdeutig zerlegbar
(`Orbis-Manus-Schreibtest-0_1.md`; nachprüfbar mit `orbis_validator.py --manus`). Ein
deterministischer Manus-Composer ist damit blockiert.

**Wichtig:** Die Silbifizierungs-Simulationen des Repos (`orbis_validator.py --sim-l09`,
`tests/manus`) sind **Analysewerkzeuge, keine Sprachregeln**. Sie dürfen nie als Regel
zitiert werden. Welche Zerlegung gilt, entscheiden die Sprachdesigner; diese Dokumentation
entscheidet es nicht.

---

## 8. Zusammenfassung des Regelstatus

| Regel | Paragraph | Status |
|---|---|---|
| Silbenformen V/KV/KVK/KKV/KKVK/KVKK | §5.1 | verbindlich über §3.3 — aber **[REGELKONFLIKT K-01]**: VK/VKK/KKVKK fehlen |
| Anfangsgruppen, 25er-Liste, max. 2 | §5.2 | verbindlich, eindeutig, kein Befund |
| Coda, max. 2, Bedingungen (a)/(b)/(c) | §5.3 | verbindlich, eindeutig, kein Befund |
| Wortlänge und Wortausgang | §5.4 | ausdrücklich Tendenz, nicht Gesetz |
| Silbentrennung | — | **[REGELLÜCKE L-09]** — nicht geregelt |
| Endgültige Konsonantenclusterliste | §30 | **[NOCH ZU ENTSCHEIDEN]** |

---

## 9. Querverweise

| Thema | Ort |
|---|---|
| Lautinventar, Klanggruppen, Regelstatus §3.3/§3.4 | `PHONOLOGIE.md` (§2, §3) |
| Betonung und Lautung | `AUSSPRACHE.md` (§23, §2, §4) |
| Herleitung neuer Wortformen | `PROTO_ORBIS.md` (§22) |
| Silbenschrift, Manus-Formel | Grammatik §26 |
| Befund-IDs K-01, L-09 und Regelbasis | `Orbis-Audit-0_1.md`, `language/findings/findings.json` |
| Maschinenlesbare Fassung | `language/phonology/syllable_shapes.json`, `onsets.json`, `codas.json`, `syllabification.json` |

---

*Quelle aller Regelaussagen: `Orbis-Grammatik-0.9.3.md` (READ ONLY). Bei Abweichung
zwischen dieser Dokumentation und der Grammatik gilt die Grammatik.*
