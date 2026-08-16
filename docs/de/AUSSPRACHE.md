# Orbis — Aussprache und Betonung

*Beschreibt Orbis-Grammatik 0.9.3. Diese Datei ist Dokumentation, nicht die Referenz.*

---

## 1. Gegenstand und Vorbehalt

Dieses Kapitel sammelt, was die Grammatik zur **Lautung** sagt: die Aussprachehinweise in
§2.1–2.3, die Ebenentrennung in §4.1–4.2 und die Betonungsregeln in §23.

**Wichtiger Vorbehalt:** Orbis 0.9.3 enthält **keine verbindliche IPA-Zuordnung**. §2.1
beschreibt die Konsonanten in Alltagssprache und über Vergleiche mit Deutsch, Französisch
und Spanisch; eine phonetische Transkription der 19 Konsonanten und 5 Vokale existiert
nicht. Diese Dokumentation ergänzt sie **nicht** — eine IPA-Tabelle wäre eine neue Regel,
und Regeln setzen die Sprachdesigner. Siehe §6 dieses Kapitels.

Die historischen Lautgesetze (§22) sind **keine** Aussprachehinweise; sie stehen in
`PROTO_ORBIS.md`. §4.3 stellt das ausdrücklich klar.

---

## 2. Die drei Ebenen (§4)

§4 trennt drei Dinge, „die in früheren Fassungen vermischt waren und streng getrennt
gehören":

| Ebene | Inhalt | Paragraph | Ort in dieser Dokumentation |
|---|---|---|---|
| **A** | Standardorthographie — Schrift zu Laut | §4.1 | dieses Kapitel, §3 |
| **B** | Natürliche Umgangsaussprache | §4.2 | dieses Kapitel, §5 |
| **C** | Historische Lautgesetze | §4.3, §22 | `PROTO_ORBIS.md` |

Die Trennung ist selbst eine Regelaussage: Was auf Ebene C steht, darf nicht als
Aussprachehinweis gelesen werden, und was auf Ebene B steht, ist keine
Rechtschreibabweichung.

---

## 3. Ebene A — Standardorthographie (§4.1)

§4.1 stellt fest:

> „**Die Schreibung von Standard-Orbis ist nahezu vollständig vorhersehbar.** Jeder
> Buchstabe hat genau einen Lautwert, jeder Laut genau ein Zeichen. Es gibt keine stummen
> Buchstaben, keine Dehnungszeichen, keine Doppelschreibung für Länge."

Daraus folgt (§4.1): „Wer die 19 Konsonanten, 5 Vokale und 6 Diphthonge kennt, kann jedes
geschriebene Orbis-Wort korrekt aussprechen. Einzige Zusatzinformation ist die Betonung,
und die ist zu etwa 85 % durch Regeln bestimmt (§23)."

Praktische Konsequenzen:

- Doppelkonsonanten markieren keine Vokallänge. Wo sie an Morphemfugen entstünden,
  verschmelzen sie ohnehin zu einem Konsonanten (Fugenregel §21.4: *mel + la* → **mela**,
  *tal + la* → **tala**, *şaln + na* → **şalna**, *selv + vi* → **selvi**).
- Ein *e* am Wortende ist ein volles *e*, kein Schwa (§2.2): *milne* Auge, *zaldre* Tag,
  *kelte* (Fragewort, §18.2).
- Vokallänge ist in 0.9.3 nicht geregelt und wird hier nicht ergänzt.

---

## 4. Was §2 zur Lautung sagt

### 4.1 Konsonanten (§2.1)

Die Beschreibungen sind wörtlich aus §2.1 übernommen. Die Spalte „Belege" nennt Wörter
aus §24/§25.

| Gruppe | Laute | Beschreibung laut §2.1 | Belege |
|---|---|---|---|
| Stimmlose Verschlusslaute | **p t k** | „wie deutsch, **ohne starke Behauchung**" | *xerp, taiv, kaun* (§24.1) |
| Stimmhafte Verschlusslaute | **b d g** | „wie deutsch" | *breun, draun, grein* (§24.1) |
| Affrikate | **ç** | „wie *tsch*" | kein Beleg im Wortschatz (s. `PHONOLOGIE.md` §6) |
| Stimmlose Reibelaute | **f s ş x** | „*s* **immer scharf**; *ş* wie *sch*; *x* **hinten im Rachen**" | *fai* (§20), *sarla* (§24.3), *şirn* (§24.1), *xerp* (§24.1) |
| Stimmhafte Reibelaute | **v z j** | „*z* wie in *Rose*; *j* wie französisch *jour*" | *valru* (§24.2), *zaldre* (§24.2); kein Beleg für *j* |
| Nasale | **m n ñ** | „*ñ* wie in *señor*" | *moks, nauş* (§24.1); Pluralmarker *-ñ-* in *melruñ* (§25.1) |
| Fließlaute | **l r** | „*r* **deutlich gerollt**" | *luiv* (§24.1), *valru* (§24.2) |

Der einzige explizite Negativhinweis in §2.1 betrifft die Behauchung: *p t k* werden
**ohne** starke Aspiration gesprochen. Das ist der einzige Punkt, an dem sich die
Standardaussprache ausdrücklich vom Deutschen abgrenzt.

**Nicht vorhanden** (§2.1): *h, w, th, pf, ts* sowie *ng* als eigener Laut. Ein
geschriebenes *ñ* ist ein Nasal wie in *señor*, nicht die deutsche *ng*-Verbindung.

### 4.2 Vokale (§2.2)

> „**a e i o u** — rein und klar, **immer voll ausgesprochen**. Kein Schwa, keine
> Reduktion. Ein *e* am Wortende ist ein volles *e*."

Das gilt für Ebene A. Auf Ebene B (§4.2) ist unbetontes *-a* am Wortende die
ausdrückliche Ausnahme, siehe §5.

### 4.3 Diphthonge (§2.3)

> „Alle Diphthonge werden **in einer Silbe** gesprochen, **mit deutlichem Übergang und
> ohne Verschleifung**."

Belegt: *ai* (*taiv*), *au* (*kaun*), *ei* (*grein*), *ui* (*luiv*), *eu* (*breun*).
*oi* ist regulär, aber unbelegt; *ou* ist **[NOCH ZU ENTSCHEIDEN]** und nicht zu
verwenden. Statusübersicht: `PHONOLOGIE.md` §4.

---

## 5. Ebene B — Natürliche Umgangsaussprache (§4.2)

§4.2 hält fest: „Im Alltag wird nicht so gesprochen, wie geschrieben wird. **Etwa 65 % der
Alltagsformen entsprechen unmittelbar der Schreibung; bei rund 35 % greifen
Reduktionen.**" Die Zahl beschreibt „ausschließlich das Verhältnis von Standardform zu
Alltagsform — sie hat nichts mit der Sprachgeschichte zu tun."

Die fünf in §4.2 genannten Erscheinungen:

| Erscheinung | Beispiel (§4.2) |
|---|---|
| Unbetontes **-a** am Wortende wird schwach | *sarla* → [sarlə] |
| Pluralmarker **-ñ-** nasaliert den Vokal davor | *sarlañan* → [sarlãan] |
| **xr-, xl-, xn-** am Wortanfang: *x* wird zum Hauch | *xra* → [ʰra] |
| Häufige Einsilber verlieren ihren Endkonsonanten vor Konsonant | *xa melam* → [xamelam] |
| Gleiche Vokale an der Wortgrenze verschmelzen | *vanda aul* → [vandaul] |

**Verbindlich bleibt die Standardaussprache** — §4.2 schließt: „Die Standardaussprache —
langsam, deutlich, jede Silbe voll — bleibt für Unterricht, Wörterbuch und feierliche Rede
verbindlich."

Zwei Hinweise zum Status dieser Tabelle:

- Sie beschreibt Tendenzen der gesprochenen Alltagssprache, nicht die Rechtschreibung. Ein
  Text wird nicht in Alltagsform geschrieben.
- Die fünf Zeilen sind **keine erschöpfende Liste**. Die Grammatik nennt keine
  Bedingungen, keine Häufigkeiten je Erscheinung und keine Wechselwirkung der Regeln
  untereinander. Wo sie schweigt, wird hier nichts ergänzt.

---

## 6. Keine IPA-Zuordnung

Die Grammatik 0.9.3 **legt keine IPA-Werte fest**. Was sie tatsächlich enthält:

- **§2.1:** Beschreibungen in Alltagssprache mit Vergleichen — „wie deutsch", „wie
  *tsch*", „wie in *Rose*", „wie französisch *jour*", „wie in *señor*", „hinten im
  Rachen", „deutlich gerollt".
- **§4.2:** fünf Transkriptionen in eckigen Klammern, die ausschließlich die
  **Reduktionserscheinungen** zeigen — [sarlə], [sarlãan], [ʰra], [xamelam], [vandaul].
  Sie verwenden IPA-nahe Zeichen (ə, Nasalierung, hochgestelltes h), sind aber keine
  systematische Transkription und decken nur diese fünf Fälle ab.
- **§26.2:** eine Einteilung der Zeichen in Schriftfamilien (NER, TAL, SOR, VEL, MOR, ISH,
  KAI, RUUN). Das ist Schriftsystematik, keine Phonetik — Manus und Grammatik sind
  getrennt zu halten.

**Nicht dokumentiert und hier nicht ergänzt:**

| Offene Frage | Was die Grammatik dazu sagt |
|---|---|
| IPA-Wert von **x** | nur „hinten im Rachen" (§2.1) — velar oder uvular, stimmlos oder anders, ist nicht festgelegt |
| IPA-Wert von **r** | nur „deutlich gerollt" (§2.1) — Zungenspitze oder Zäpfchen ist nicht festgelegt |
| IPA-Wert von **ç** | nur „wie *tsch*" (§2.1); im Inventar als **Affrikate** geführt |
| IPA-Wert von **ñ** | nur „wie in *señor*" (§2.1) |
| Genaue Vokalqualitäten von **a e i o u** | nur „rein und klar" (§2.2) |
| Vokallänge | nicht geregelt; §4.1 schließt nur Dehnungs- und Doppelschreibung aus |
| Silbengewicht/Quantität | nicht geregelt |

Das Audit vergibt für diese Lücke **keine eigene Befund-ID**; sie wird hier als
Beobachtung festgehalten. Eine IPA-Tabelle zu ergänzen wäre eine Sprachentscheidung und
ist den Sprachdesignern vorbehalten.

---

## 7. Betonung (§23)

### 7.1 Grundregel

> Normalerweise auf der **vorletzten Silbe**.

Beispiele aus §23: **VAL**-ru · **SAR**-la · mil-**NE**-ñeş · me-**LA**-men.

Die Beispiele zeigen, dass die Regel auf der **fertig flektierten** Form arbeitet und die
Betonung mit den Endungen wandert: *milne* (Auge, §24.4) → *milneñeş* (Dat. Pl., §9) trägt
den Akzent auf *-NE-*; *melamen* (wir gehen, Wurzel *mel-* mit Tempusvokal *-a-* und
Personendung *-men*, §15.1) trägt ihn auf *-LA-*. Die Betonungsregel greift damit nach der
Morphologie, nicht auf den nackten Stamm.

### 7.2 Die vier Ausnahmegruppen

| Ausnahmegruppe | Regel (§23) | Beispiel (§23) |
|---|---|---|
| Abstrakta auf **-uma**, Werkzeuge auf **-isto** | Betonung bleibt auf dem **Stamm** | **MEL**-uma, **TAL**-isto |
| Die **15 alten Kernwörter** (§24.1) | Betonung auf der **letzten** Silbe | *kaUN, breUN, taIV* |
| **Zusammensetzungen** (§21.3) | Betonung auf dem **ersten Glied** | **LUIV**-resto |
| Wörter mit **Vorsilbe** (§21.2) | Vorsilbe **unbetont** | şu-**NAR**-gat |

Weitere betroffene Wörter, die sich aus dem Wortschatz ergeben:

- **-uma** (§24.6, §21.1): *soruma, klaunuma, nestuma, salvuma, vaşnuma, mirnuma,
  şauluma, tarnuma, saivuma, virnuma* sowie *taluma* (Rede) und *meluma* (Reise) —
  Stammbetonung. Nicht betroffen sind Wörter, die zufällig auf *-ma* enden, ohne das
  Suffix zu tragen (*şonma* Stimme, *klerma* Freiheit, §24.3); für sie gilt die
  Grundregel.
- **-isto** (§21.1, §24.4): *melisto* (Fahrzeug), *talisto* (Instrument) — Stammbetonung.
  *vresto* (Buch) endet zwar auf *-sto*, trägt aber nicht das Suffix *-isto* und fällt
  daher unter die Grundregel.
- **Zusammensetzungen** (§21.3): *taivbreun* Schule, *aulmelna* Kanal, *luivresto*
  Kalender — Betonung auf dem ersten Glied.
- **Vorsilben** (§21.2): *şu-* (Passiv), *xa-* (Gegenteil), *re-* (wieder), *dra-* (ganz),
  *su-* (halb) — unbetont; Belege *şunargat, xaselvra, revandat, dramilkat, suluidra*.

### 7.3 Vorhersagbarkeit

§23 schließt mit: „**Ca. 85 % vorhersagbar.**" §4.1 nennt dieselbe Zahl. Die Grammatik
sagt nicht, welche 15 % nicht vorhersagbar sind, und nennt kein Verfahren, die Betonung
solcher Wörter zu ermitteln. Diese Lücke wird hier nicht geschlossen.

### 7.4 Betonung und Silbentrennung (L-09)

Die Betonungsregel zählt Silben, und eine **Silbentrennungsregel existiert nicht**
(Regellücke **L-09**, siehe `PHONOTAKTIK.md` §7). Für die Betonung ist das nach
`Orbis-Audit-0_1.md` §2.4 **folgenlos**: Ob *mela* als *me·la* oder *mel·a* zerlegt wird,
ändert nichts an der Silbenzahl und damit nichts an der vorletzten Silbe. Wirksam wird
L-09 erst in Orbis Manus (§26) und bei der Tastatureingabe (§26.8).

### 7.5 Beobachtungen ohne Befund-ID

Zwei Punkte hält diese Dokumentation fest, ohne sie zu entscheiden:

1. **Kernwörter in flektierten Formen.** Die drei Belege in §23 (*kaUN, breUN, taIV*) sind
   einsilbige Nominativformen; dort fallen „letzte Silbe" und jede andere Regel zusammen.
   Erst in flektierten Formen (*kaunei, kauneiş, eirdes*, §10.3) unterscheidet sich die
   Ausnahme von der Grundregel. Für solche Formen gibt §23 kein Beispiel. Was gilt, ist
   nicht entschieden.
2. **Zusammentreffen mehrerer Ausnahmen.** §23 regelt jede Gruppe für sich, aber nicht,
   welche Regel gewinnt, wenn zwei zutreffen — etwa bei einer Vorsilbe vor einem
   *-uma*-Abstraktum oder bei einer Zusammensetzung mit einem Kernwort als erstem Glied
   (*taivbreun*: Zusammensetzungsregel und Kernwortregel treffen beide zu). Belege für
   solche Fälle nennt die Grammatik nicht.

Beide Punkte sind Beobachtungen an der Regelformulierung, keine Befunde des Audits, und
werden hier weder gefüllt noch ausgelegt.

---

## 8. Querverweise

| Thema | Ort |
|---|---|
| Lautinventar und Klanggruppen | `PHONOLOGIE.md` (§2, §3) |
| Silbenformen, Anfangs- und Endgruppen, L-09 | `PHONOTAKTIK.md` (Abschnitt 5 dieser Datei) |
| Lautgesetze (Ebene C) und Wortherleitung | `PROTO_ORBIS.md` (§22, §4.3) |
| Schriftzeichen, Manus-Silbenformel | Grammatik §26 |
| Befund-IDs und Regelbasis | `Orbis-Audit-0_1.md` |
| Maschinenlesbare Fassung der Betonungsregel | `language/phonology/stress.json` |

---

*Quelle aller Regelaussagen: `Orbis-Grammatik-0.9.3.md` (READ ONLY). Bei Abweichung
zwischen dieser Dokumentation und der Grammatik gilt die Grammatik.*
