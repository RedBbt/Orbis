# Orbis — Orbis Magna, die feierliche Schrift

*Beschreibt Orbis-Grammatik 0.9.3. Diese Datei ist Dokumentation, nicht die Referenz.*

---

## 1. Gegenstand

Dieses Kapitel beschreibt §27 der Grammatik. §27 ist kurz; dieses Kapitel bleibt es
ebenfalls. Es wird nichts ergänzt, ausgeführt oder ausgestaltet.

Orbis besitzt seine Schrift „in zwei Stufen" (§1): **Orbis Manus** als Alltagsschrift
(§26, siehe `MANUS.md`) und **Orbis Magna** als feierliche Ausführung.

---

## 2. Was §27 festlegt

§27 bestimmt Magna nicht als zweite Schrift, sondern als **stilistische Schicht über
denselben Kernformen**:

> „Dieselben 20 Kernformen, dieselbe Silbenformel, dieselbe Sprache — feierlich
> ausgeführt."

Daraus folgt: Wer Manus lesen kann, liest auch Magna. Es gibt kein zusätzliches Zeichen,
keine zweite Silbenformel und keine abweichende Grammatik. Alle Aussagen aus §26.1–26.7
gelten unverändert weiter.

**Verwendungszweck (§27):** Zitate, Inschriften, Symbole, Kunst, Titel.

**Die fünf Bestimmungen (§27):**

| Nr. | Bestimmung | Art |
|---|---|---|
| 1 | Kreisförmige Anordnung, Text von innen nach außen in einer Spirale | Anordnung |
| 2 | Kernformen dürfen ausgeschmückt werden, solange die zwei Unterscheidungsmerkmale bleiben | Erlaubnis mit Grenze |
| 3 | Vokalpunkte dürfen zu Kreisen oder Rauten werden | Erlaubnis |
| 4 | **Coda-Zeichen dürfen nicht ausgeschmückt werden** | Verbot |
| 5 | Der Abschluss eines Textes bildet den äußeren Ring | Anordnung |

Bestimmung 2 verweist zurück auf §26.2 („Jede Kernform muss sich von jeder anderen in
mindestens zwei Merkmalen unterscheiden"): Die Ausschmückung darf den Merkmalsabstand nicht
aufbrauchen. Bestimmung 4 schützt die Coda, deren Lesbarkeit allein an Größe und Ort hängt
(§26.5–26.7) und die durch Ornament mit einem Beizeichen oder einem Abschlusszeichen
verwechselbar würde.

**Belege.** Die Grammatik zeigt keinen Text und kein Zeichen in Orbis Magna; §27 besteht
vollständig aus den zitierten Bestimmungen. Ein Beispiel kann hier deshalb nicht angeführt
werden. Die belegten Manus-Zerlegungen (*mel*, *kaun*, *breun*, *tel*, *moks*, *virn*,
*xerp*, *teln*; §26.5–26.6) gelten nach dem Wortlaut von §27 auch für Magna, weil dort
dieselbe Silbenformel gilt.

---

## 3. Was ausdrücklich offen ist

§27 schließt mit einer eigenen Offenmarkierung, die §30 unter den offenen Punkten des
Gesamtdokuments wiederholt („Spiralregeln von Orbis Magna"):

> **[NOCH ZU ENTSCHEIDEN]** Spiralrichtung, Zeilenumbruch, sehr lange Texte.

| Offener Punkt | Was ungeklärt ist |
|---|---|
| **Spiralrichtung** | §27 legt „von innen nach außen" fest, aber nicht den Drehsinn (im oder gegen den Uhrzeigersinn) |
| **Zeilenumbruch** | Wie eine Zeile in der Spirale endet und die nächste beginnt |
| **Sehr lange Texte** | Was geschieht, wenn ein Text den Ring sprengt (mehrere Spiralen, Fortsetzungszeichen, anderes Format) |

Das Audit führt Magna ausdrücklich als **offen, aber ohne Prüfbefund**
(`Orbis-Audit-0_1.md` §21): Die Spiralregeln sind kein Regelkonflikt und keine
Regellücke im Sinne der Befund-IDs, sondern ein von der Grammatik selbst als unentschieden
markierter Bereich. Es gibt deshalb keine Befund-ID K-xx / L-xx / U-xx für Magna.

**Diese Dokumentation entscheidet keinen dieser Punkte** und leitet auch keine Regel aus
§26 ab. Solange die Spiralregeln offen sind, gibt es kein prüfbares Magna-Layout; ein
Magna-Satz kann nicht auf Korrektheit geprüft werden.

---

## 4. Abgrenzung und Status

| Punkt | Feststellung |
|---|---|
| Zeicheninventar | identisch mit Manus: 20 Kernformen, 8 Familien (§26.2) |
| Silbenformel | identisch mit Manus (§26.1) |
| Sprache | identisch — Magna ist Ausführung, nicht Varietät |
| Eigene Regeln | nur die fünf Bestimmungen aus §27 |
| Versionierung | Orbis Manus steht bei 0.x ohne Freigabefassung; Magna hat keine eigene Fassung (`STATUS.md`) |
| Ablage im Repo | `script/magna/` — getrennt von `script/manus/` und von `language/` |

Magna hängt fachlich an Manus: Solange **[REGELLÜCKE L-09]** (keine Silbifizierungsregel)
und **[REGELLÜCKE L-10]** (Strichstärke) offen sind, sind auch die Magna-Silbenblöcke nicht
eindeutig bestimmt, denn sie benutzen dieselben Blöcke (siehe `MANUS.md` §10 und §11).
Eine Freigabe von Magna vor Manus ist damit nicht möglich.

---

## 5. Querverweise

| Thema | Ort |
|---|---|
| Kernformen, Silbenformel, Coda, Abschlusszeichen | `MANUS.md` (§26) |
| Stand der Tastaturplanung | `TASTATUR.md` (§26.8) |
| Offene Punkte des Gesamtdokuments | Grammatik §30 |
| Befundlage zu §26/§27 | `Orbis-Audit-0_1.md` (§21) |

---

*Quelle aller Regelaussagen: `Orbis-Grammatik-0.9.3.md` (READ ONLY). Bei Abweichung
zwischen dieser Dokumentation und der Grammatik gilt die Grammatik.*
