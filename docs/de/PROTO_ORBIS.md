# Orbis — Proto-Orbis und Lautgeschichte

*Beschreibt Orbis-Grammatik 0.9.3. Diese Datei ist Dokumentation, nicht die Referenz.*

---

## 1. Gegenstand

Dieses Kapitel beschreibt §22 der Grammatik: die sieben historischen Lautgesetze, ihre
Belege und die daraus abgeleitete Arbeitsanweisung für neue Wörter. Dazu kommt die
Statuseinstufung von Etymologien im Datenmodell dieses Repos und eine nüchterne Angabe,
für wie viele Lexeme überhaupt eine Herleitung dokumentiert ist.

**Proto-Orbis ist kein Textkorpus und keine sprechbare Sprache.** Es existiert in 0.9.3
ausschließlich als Menge rekonstruierter Vorformen einzelner Wörter, in der Grammatik
durchgehend mit Sternchen notiert (\*kau-nu, \*tal-iv, \*vir-na). Eine Proto-Grammatik,
ein Proto-Lexikon oder eine Proto-Phonologie gibt es nicht und werden hier nicht ergänzt.

---

## 2. Ebene C — rein diachron (§4.3)

§4.3 ordnet die Lautgesetze eindeutig ein:

> „Die sieben Lautgesetze in §22 erklären, **wie die heutigen Wortformen aus Proto-Orbis
> entstanden sind**. Sie sind Sprachgeschichte, **keine Aussprachehinweise und keine
> Rechtschreibabweichungen**. Ein Sprecher des heutigen Orbis wendet sie nicht an — er
> spricht *taiv*, nicht \*tal-iv."

§22 wiederholt das im ersten Satz: „Diese Gesetze sind **Sprachgeschichte** (§4.3), keine
modernen Aussprachehinweise."

Daraus folgen drei Abgrenzungen:

| Nicht zu verwechseln mit | Ort | Unterschied |
|---|---|---|
| Ebene A, Standardorthographie | §4.1 | Ebene A ist die geltende Schreibung; die Lautgesetze erzeugen sie nicht neu |
| Ebene B, Umgangsaussprache | §4.2 | Ebene B beschreibt heutige Reduktionen (*sarla* → [sarlə]); mit Sprachgeschichte hat sie „nichts zu tun" (§4.2) |
| Synchrone Regeln | §3.3, §5 | Für die Gültigkeitsprüfung eines Wortes sind die Lautgesetze **ohne Wirkung**; geprüft wird die moderne Form gegen §3.3 |

Für Werkzeuge heißt das: Die Lautgesetze dürfen in keiner synchronen Prüfung angewendet
werden (`language/proto/sound_laws.json`: „Rein diachron (§4.3). Für synchrone Prüfungen
ohne Wirkung.").

Praktischen Nutzen hat Ebene C laut §4.3 nur an einer Stelle: „Ihr praktischer Nutzen ist
die Wortbildung: Wer ein neues Wort erfindet, kann es über Proto-Orbis herleiten und
erhält dadurch eine glaubwürdige Form." Siehe §4 dieses Kapitels.

---

## 3. Die sieben Lautgesetze (§22)

Alle Beispiele stammen wörtlich aus §22 bzw. §10; \* markiert die rekonstruierte
Vorform.

### Gesetz 1 — Endvokalschwund

Der auslautende Vokal der Proto-Form fällt weg.

| Proto-Form | Modern | Bedeutung | Fundstelle |
|---|---|---|---|
| \*kau-nu | **kaun** | Mensch | §22, §10.2 |
| \*vir-na | **virn** | Leben | §22, §10.2 |
| \*mok-sa | **moks** | Tod | §22, §10.2 |
| \*velkra-na | **velkran** | Freundschaft | §10.1 |
| \*soral-mu | **soralm** | Denkmal | §10.1 |

Dieses Gesetz erklärt zugleich, warum die betroffenen Wörter ihr Geschlecht am
**vorletzten** Konsonanten tragen: In *velkran* ist *-n-* der Klassenkonsonant (neutral),
in *soralm* das *-m-* (feminin), §10.1.

### Gesetz 2 — Diphthongierung durch Vokalverlust

Beim Ausfall eines Binnenvokals verschmelzen die verbleibenden Vokale zu einem Diphthong.

| Proto-Form | Modern | Bedeutung | Fundstelle |
|---|---|---|---|
| \*tal-iv | **taiv** | Sprache | §22, §10.2, §21.1 |
| \*luv-iv | **luiv** | Sonne | §22, §10.2 |
| \*veş-iv | **veiş** | Mutter | §22, §10.2 |

§21.1 hält ausdrücklich fest, dass *taiv* zur Wortfamilie von *tal-* (sprechen) gehört —
die Etymologie stiftet hier eine Bedeutungsverbindung, die der modernen Form nicht mehr
anzusehen ist.

### Gesetz 3 — Erweichung

> „Stimmlose Verschlusslaute zwischen Vokalen werden stimmhaft: **k → g, t → d, p → b**."

§22 nennt für dieses Gesetz **kein Beispielwort**. Ein Beleg fehlt damit in der Grammatik;
diese Dokumentation ergänzt keinen.

### Gesetz 4 — Assimilation

> „*n* gleicht sich dem folgenden Konsonanten an: **n+p → mp, n+k → ñk**."

Auch hier nennt §22 **kein Beispielwort**. Zu beachten: Die Regel beschreibt einen
historischen Vorgang, nicht die synchrone Fugenregel §21.4 (dort verschmelzen zwei
**identische** Konsonanten an der Morphemfuge, z. B. *mel + la* → *mela*). Beide dürfen
nicht vermengt werden.

### Gesetz 5 — Verlust vor Nasal

> „*k* fällt vor *n* aus."

| Proto-Form | Modern | Bedeutung | Fundstelle |
|---|---|---|---|
| \*milk-ne | **milne** | Auge, zur Wurzel \*milk- | §22 |

Der Beleg verbindet das Nomen *milne* (Auge, N-A, §24.4) mit dem Verbstamm *milk-* (sehen,
§24.5) — dieselbe Wurzel, durch das Gesetz getrennte Oberflächenformen.

### Gesetz 6 — Ablaut in häufigen Verben

> „\*mel- → **molet** statt \*melot."

Dieses Gesetz erklärt die acht unregelmäßigen Verben aus §15.2, die „in der Vergangenheit
eine ältere Vokalstufe bewahren": *est/vot*, *nut/novet*, *vurt/voret*, *melat/molet*,
*vandat/vendet*, *nargat/norget*, *zavat/zovet*, *dalvat/dolvet*. Beleg im laufenden Text:
*„Vra melru molet dral xrañan trelmrañan zaldreñen."* (§25.2).

### Gesetz 7 — Reduktion häufiger Wörter

Hochfrequente Funktionswörter werden gekürzt.

| Proto-Form | Modern | Bedeutung | Fundstelle |
|---|---|---|---|
| \*xa-ra | **xra** | bestimmter Artikel M Nom Sg (§11.1) | §22 |
| \*vima | **vim** | ich (§13.1) | §22 |
| \*şeta | **şet** | du (§13.1) | §22 |

Die Auswahl ist bezeichnend: Alle drei Belege sind Funktionswörter, keine Inhaltswörter.
Das deckt sich mit Richtlinie 5 (§3.4), nach der Einsilber „meist Funktionswörter oder
Kernwörter" sind.

### Übersicht

| Nr. | Name | Belege in §22 |
|---|---|---|
| 1 | Endvokalschwund | 3 (+2 in §10.1) |
| 2 | Diphthongierung durch Vokalverlust | 3 |
| 3 | Erweichung | **keine** |
| 4 | Assimilation | **keine** |
| 5 | Verlust vor Nasal | 1 |
| 6 | Ablaut in häufigen Verben | 1 (wirksam für die 8 Verben aus §15.2) |
| 7 | Reduktion häufiger Wörter | 3 |

Dass die Gesetze 3 und 4 unbelegt sind, ist eine Beobachtung an der Grammatik; das Audit
vergibt dafür **keine Befund-ID**, und diese Dokumentation erfindet keine Belege.

---

## 4. Arbeitsanweisung für neue Wörter (§22)

§22 schließt mit einer Regel für die Wortbildung:

> „**Regel für neue Wörter:** zuerst regelmäßig in Proto-Orbis bilden, dann Gesetze 1–7
> anwenden, dann gegen §3.3 prüfen und an §3.4 ausrichten."

Als Ablauf:

| Schritt | Handlung | Maßstab | Status |
|---|---|---|---|
| **1** | Proto-Form regelmäßig bilden | §22 | Werkzeug — erzeugt eine glaubwürdige Form (§4.3) |
| **2** | Lautgesetze 1–7 anwenden | §22 | Werkzeug |
| **3** | Ergebnis gegen die harten Sprachregeln prüfen | **§3.3** — Phoneminventar (§2), Silbenformen (§5.1), Anfangsgruppen (§5.2), Endgruppen (§5.3) | **verbindlich** — hier fällt die Entscheidung über Gültigkeit |
| **4** | Ergebnis an den Klangrichtlinien ausrichten | **§3.4**, nur lexikalischer Stamm (§3.5) | beschreibend — kein Wort wird durch Abweichung ungültig |

Wichtig für die Reihenfolge: Schritt 3 ist das **Sieb**, Schritt 4 die **Feile**. §3.3
sagt: „Alles andere ist Klang, nicht Gesetz." §3.4 sagt: „Ein Wort wird **nicht ungültig**,
weil es davon abweicht." Eine Proto-Herleitung rechtfertigt also keine Form, die §3.3
verletzt — die Herleitung ist Begründung, nicht Freibrief.

Zwei Vorbehalte für Schritt 3:

- Die Silbenformenliste §5.1 ist unvollständig (**[REGELKONFLIKT K-01]**). Wer nach dieser
  Anweisung ein Wort der Form VK, VKK oder KKVKK erzeugt, trifft auf den Konflikt und muss
  ihn als K-01 melden, nicht selbst auflösen. Siehe `PHONOTAKTIK.md` §3.
- Der Diphthong *ou* ist **[NOCH ZU ENTSCHEIDEN]** (§2.3, §30) und darf in einer neuen
  Form nicht auftreten; *oi* ist dagegen regulär und ausdrücklich für neue Wörter offen
  (§2.3). Siehe `PHONOLOGIE.md` §4.

**Diese Dokumentation bildet keine neuen Wörter.** Der Wortschatz ist ab 0.9.3 eingefroren
(§24): „Ein Wort wird nur noch geändert, wenn es gegen die Phonotaktik verstößt,
grammatisch inkonsistent ist, problematisch mit einem anderen Wort kollidiert oder eine
widersprüchliche Bedeutung trägt. Geschmacksfragen reichen nicht mehr." Neue Wörter
entstehen nur auf Auftrag der Sprachdesigner.

---

## 5. Statuswerte für Etymologien

Das Datenmodell des Repos (`language/lexicon/lexicon.schema.json`, Feld `etymologie`)
kennt vier Statuswerte. **Sie stehen nicht in der Grammatik** — sie sind eine
Buchführungskonvention dieses Repos, die §4.3 umsetzt und offenlegt, wie gut eine
Herleitung belegt ist. Sie ändern keine Sprachregel.

| Status | Bedeutung | Beispiel |
|---|---|---|
| **documented** | Die Grammatik nennt die Proto-Form ausdrücklich | *kaun* < \*kau-nu (§10.2, §22) |
| **reconstructed** | Proto-Form aus den Gesetzen §22 hergeleitet, aber nicht in der Grammatik verzeichnet | — |
| **provisional** | Vorläufige Herleitung, noch nicht bestätigt | — |
| **unknown** | Keine Herleitung bekannt; Vorgabe ohne Beleg | alle derzeit erfassten Einträge, siehe §6 |

Das Schema hält die Grundregel selbst fest: **„Keine Etymologie erfinden. Ohne Beleg
status=unknown."** Eine plausible Herleitung ist noch kein Beleg. Wer eine Etymologie von
`unknown` hochstuft, braucht entweder eine Fundstelle in der Grammatik (→ `documented`)
oder eine nachvollziehbare Ableitung über die Gesetze 1–7 (→ `reconstructed`), die als
solche gekennzeichnet bleibt.

---

## 6. Für die meisten Lexeme ist keine Herleitung dokumentiert

Die Grammatik nennt Proto-Formen nur an drei Stellen:

| Stelle | Umfang | Wörter |
|---|---|---|
| §10.1 (10-Prozent-Gruppe) | 3 | *velkran* < \*velkra-na · *soralm* < \*soral-mu · *prilm* < \*prila-mu |
| §10.2 (15 Kernwörter) | 15 | *kaun* < \*kau-nu · *veiş* < \*veş-iv · *draun* < \*drau-nu · *şirn* < \*şir-ni · *aul* < \*au-lu · *xerp* < \*xer-pa · *luiv* < \*luv-iv · *grein* < \*gre-ina · *nauş* < \*nau-şa · *virn* < \*vir-na · *moks* < \*mok-sa · *eird* < \*e-irda · *şaul* < \*şa-ulo · *taiv* < \*tal-iv · *breun* < \*breu-na |
| §22 (Gesetzesbelege) | 5 zusätzlich | *milne* < \*milk-ne · *xra* < \*xa-ra · *vim* < \*vima · *şet* < \*şeta · *molet* < Ablaut zu \*mel- |

Das sind **23 Lexeme** mit ausdrücklich verzeichneter Vorform. Dem stehen **281 erfasste
Grundformen** in `language/lexicon/entries/` gegenüber; im maschinenlesbaren Lexikon trägt
derzeit **jeder** dieser 281 Einträge `etymologie.status = "unknown"` (Stand dieser
Fassung, nachprüfbar über die Einträge selbst).

Für die große Mehrheit des Wortschatzes gilt damit: **Es ist keine Herleitung
dokumentiert.** Das ist kein Fehler und kein Befund des Audits, sondern der schlichte
Stand von 0.9.3. Zwei Konsequenzen:

1. **Nicht rückwärts rechnen.** Aus einer modernen Form eine Proto-Form abzuleiten und sie
   als Etymologie einzutragen, wäre eine Erfindung. Ohne Beleg bleibt der Status
   `unknown`.
2. **Wortfamilien sind nicht dasselbe wie Etymologie.** §21.1 dokumentiert produktive
   Wortfamilien (*mel-* → *melex, melru, mela, melna, melisto, melvi, meluma*; *tal-* →
   *talex, talru, tala, talna, talisto, talvi, taluma*). Das sind **synchrone**
   Ableitungen nach §21, keine Lautgeschichte. Nur wo §21.1 ausdrücklich historisch spricht
   — *taiv* als \*tal-iv, *melva* (Straße) als „alter Ableger von *mel-*" — berührt es
   Ebene C; für *melva* nennt die Grammatik allerdings **keine** Proto-Form.

---

## 7. Ausblick: Dialekte (§31)

§31 hält fest, dass künftige Dialekte „später ausschließlich aus Standard-Orbis abgeleitet"
werden, „durch weitere Lautgesetze nach dem Muster von §22: ein härterer, ein
weicher-melodischer und ein konservativer Dialekt". Diese Lautgesetze existieren **noch
nicht**; §31 sagt ausdrücklich „Noch nicht entwickelt". Auch diese Dokumentation beschreibt
ausschließlich Standard-Orbis (§1.).

---

## 8. Querverweise

| Thema | Ort |
|---|---|
| Lautinventar, §3.3 gegen §3.4/§3.5 | `PHONOLOGIE.md` (§2, §3) |
| Silbenformen, Anfangs-/Endgruppen, K-01 | `PHONOTAKTIK.md` (§5) |
| Ebene A und B, Betonung, fehlende IPA-Zuordnung | `AUSSPRACHE.md` (§4, §23) |
| Wortbildung, Vorsilben, Fugenregel (synchron) | Grammatik §21 |
| Unregelmäßige Verben (Gesetz 6) | Grammatik §15.2 |
| Datenmodell und Statuswerte | `language/lexicon/lexicon.schema.json`, `language/proto/sound_laws.json` |
| Befund-IDs und Regelbasis | `Orbis-Audit-0_1.md` |

---

*Quelle aller Regelaussagen: `Orbis-Grammatik-0.9.3.md` (READ ONLY). Bei Abweichung
zwischen dieser Dokumentation und der Grammatik gilt die Grammatik.*
