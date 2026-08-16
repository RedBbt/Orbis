# ORBIS — Testbericht 0.1

*Statistische Auswertung, Priorisierung und Gesamturteil des Stabilitätstests gegen `Orbis-Grammatik-0.9.3.md` (READ ONLY, unverändert). Grundlagen: `Orbis-Audit-0_1.md` (Regelbasis + Befund-IDs), `orbis_validator.py` + `Orbis-Validator-Bericht-0_1.md` (automatische Prüfung), `Orbis-Testkorpus-0_1.md` (150 Tests), `Orbis-Manus-Schreibtest-0_1.md` (Schrift), `Orbis-Testdaten.json` (strukturierte Daten).*

---

## PHASE 5 — STATISTIK

| Kennzahl | Wert |
|---|---|
| Tests insgesamt | **150** |
| [OK] | **130** |
| [TESTPROBLEM] | **1** (Test 104) |
| [REGELLÜCKE] | **14** (Tests 033, 035, 036, 039, 070, 074, 075, 076, 100, 101, 102, 137, 138, 149) |
| [REGELKONFLIKT] | **3** (Tests 060, 103, 105) |
| [REGELUNKLARHEIT] | **2** (Tests 051, 111) |

**Stabilitätsquote = 130 / 150 × 100 = 86,7 %**

Diese Zahl ist nur ein technischer Indikator; keine Regel wurde geändert, um sie zu erhöhen. Zwei Lesehilfen:

1. **Die 20 Nicht-OK-Tests gehen auf nur 11 unterschiedliche Probleme zurück** (L-01, L-02, L-03, L-04, L-05, L-08, K-04, K-05, U-02, U-03, W-01 — mehrere Tests prüfen dasselbe Problem in verschiedenen Kasus). *(Korrigiert: eine frühere Fassung dieses Absatzes zählte fälschlich „9".)* Kein einziges Problem ist ein Widerspruch im morphologischen Kern: **Kongruenz, Deklination (alle 45 Endungen + Kernwörter), Konjugation (6×3 + alle 8 unregelmäßigen), V2, Verbklammer im Hauptsatz, Negation, Passivbildung und Phonotaktik der Testsätze halten in allen 130 bildbaren Sätzen** — maschinell bestätigt (Validator-Bericht, Lauf D: 0 automatische Befunde).
2. Zusätzlich zu den 11 korpuswirksamen Problemen dokumentieren Audit und Berichte **19 weitere Befunde** (K-01, K-02, K-03 · L-06, L-07, L-09, L-10 · U-01, U-04 bis U-14), die keine Testsätze scheitern lassen, aber vor 1.0 entschieden oder redigiert werden sollten. Gesamtinventar: **30 Befunde + Phase-7-Wortschatzliste.**

Vergleich zum Chat-Testkorpus 0.1 (145/150 ✓): Die niedrigere Quote hier ist strengeres Messen, nicht schlechteres Orbis — der Chat-Entwurf wertete u. a. den ungeregelten Modal-Vollverbgebrauch (111) und den §25.1-Adverbsatz (39) als ✓, testete Reflexiv, Fragewortkasus und Modal-im-Nebensatz gar nicht und enthielt einen unentdeckten Kongruenzfehler (Satz 48 *loşna* statt *loşnla*).

---

## PHASE 6 — PRIORISIERUNG

P0 = verhindert grundlegende Kommunikation · P1 = wichtige Konstruktion fehlt · P2 = seltene/fortgeschrittene Konstruktion unklar · P3 = Dokumentations-/Formulierungsproblem · P4 = rein stilistisch.

**Es gibt keinen P0-Befund.**

### P1 — wichtige grammatische Konstruktionen (6)

| ID | Priorität | Testnummer | Problem | Betroffene §§ | Mögliche Lösungsrichtungen (KEINE Festlegung) |
|---|---|---|---|---|---|
| L-02 | P1 | 100, 101, 102, 149 | Relativsatzbau fehlt vollständig; fai „der/die/das" ohne Kasus/Kongruenz/Verbstellung; Homonymie mit fai „dass" | §13.4, §17.2, §20 | (a) fai indeklinabel + Nebensatz-Verbendstellung, Kasus aus dem Satzinneren; (b) fai dekliniert wie Pronomen (fai/fain/faiş/fais); (c) eigenes Relativpronomen, fai bleibt „dass"; (d) Partizipialkonstruktionen statt Relativsätzen |
| L-01 | P1 | 036, 039 (berührt: 037–045, 148) | Stellung des Genitivattributs ungeregelt; Stapelung Gen+Possessiv offen | §8, §13.3, §17 | (a) nachgestellt normieren (deckt alle Beispiele + §13.3-Analogie); (b) beide Stellungen mit Bedeutungs-/Stilunterschied; (c) vorangestellt (bräche sämtliche Beispiele) |
| L-05 | P1 | 137, 138 | Agens im Passiv nicht ausdrückbar | §16.3, §19 | (a) bestehende Präposition widmen (z. B. ven + Dat); (b) neue Agens-Präposition (Wortschatzänderung!); (c) Agens nur über Aktivsatz zulassen und das normieren |
| L-04 | P1 | 033, 035 (berührt: 022, 032, 034) | Reflexiv se ohne Kasusformen; Personenbereich unklar | §13.4 | (a) se indeklinabel für Akk+Dat der 3. Person, 1./2. über Personalpronomen (deutsches Modell); (b) se dekliniert (se/sen/seş/ses); (c) se für alle Personen |
| L-03 | P1 | 074, 075, 076 (berührt: 080) | kem/kelt nur in Grundform; wen/wem/wessen unbildbar | §18.2 | (a) pronominal deklinieren (kem/kemen/kemeş/kemes nach Kernwortmuster); (b) indeklinabel + Stellung/Präposition trägt den Kasus; (c) kelt-Sonderfall Nom=Akk wie dt. „was" |
| K-05 | P1 | 103, 105 | Modalverb im Nebensatz: §16.1 (Infinitiv am Satzende) und §17.2 (finites Verb am Ende) beanspruchen dieselbe Position; mit Negation zusätzlich xa-Position offen | §16.1 ↔ §17.2, §18.3 | (a) deutsches Muster: … Infinitiv + finites Modal (melex dolmat), xa vor dem Infinitivkomplex; (b) finit vor Infinitiv (dolmat melex); (c) Modalverben im Nebensatz umschreiben |

### P2 — fortgeschrittene Konstruktionen (9)

| ID | Priorität | Testnummer | Problem | Betroffene §§ | Mögliche Lösungsrichtungen |
|---|---|---|---|---|---|
| L-08 | P2 | 070 | Syntax der Kardinalzahlen (Kongruenz, Numerus, Artikel) | §24.8, §9 | (a) Zahl indeklinabel + Nomen im Plural; (b) Nomen im Singular nach Zahl; (c) Zahlkongruenz |
| L-06 | P2 | — (Grundformen in 088 ok) | Deklination der Demonstrativa (kilra…) und Indefinita (kelsu, xakaun…) | §13.4 | (a) adjektivisch nach §12.1 (Analogie kella→kellan §18.2); (b) indeklinabel; (c) pronominal |
| L-07 | P2 | — | Plural der 10-Prozent-Gruppe (velkran, soralm, prilm) unbildbar | §10.1, §9 | (a) Kernwortmuster -ei öffnen; (b) -e- + regulärer Plural (velkraneñ?); (c) als Abstrakta pluralunfähig erklären |
| U-02 | P2 | 051 | Partizip attributiv (das gefundene Buch) ungeregelt | §12, §14, §16.3 | (a) Partizip dekliniert wie Adjektiv (traivutna); (b) nur prädikativ/nominalisiert zulassen; (c) Relativsatz-Ersatzkonstruktion (hängt an L-02) |
| U-03 | P2 | 111 | Modalverb ohne Infinitiv (Ich mag das Wort) ungeregelt | §16.1 | (a) Vollverbgebrauch mit Akk zulassen; (b) verbieten, Umschreibung mit Vollverb + Infinitiv; (c) je Modalverb einzeln festlegen |
| U-04 | P2 | 071 (Anm.) | Pro-Drop: §18-Beispiele lassen Subjektpronomen in Fragen weg, Aussagesätze nie — Regel fehlt | §18, §13.1 | (a) Pro-Drop nur in Fragen zulassen; (b) generell zulassen (Endung trägt Person); (c) verbieten und §18-Beispiele als elliptisch markieren |
| U-08 | P2 | — | Deklinationsklasse von Komposita mit Kernwort-Kopf (taivbreun) | §21.3, §10 | (a) Kopf vererbt volle Flexion (taivbreun → taivbreunei); (b) Komposita immer regulär; (c) Einzelfallmarkierung im Wörterbuch |
| L-09 | P2 | Manus-Test (77/281 mehrdeutig) | Keine Silbifizierungs-Präferenzregel → Manus-/Tastatur-Mehrdeutigkeit | §5, §26 | (a) Onset-Maximierung + Diphthong-Vorrang normieren (löst fast alle Fälle); (b) Silbengrenze lexikalisch festschreiben; (c) freie Varianz erklären (Schrift bleibt mehrdeutig) |
| W-01 | P2 | 104 | Wortschatzlücken für Grundkommunikation: „sagen", „zeigen", „suchen", Existenzkonstruktion („es gibt") | §24 | (a) gezielte Neuwörter nach §22-Werkstatt (Designer-Entscheidung); (b) Bedeutungserweiterung vorhandener Wurzeln (tal- „sprechen/sagen") mit Wörterbuchvermerk |

### P3 — Dokumentation und Formulierung (14)

| ID | Priorität | Testnummer | Problem | Betroffene §§ | Mögliche Lösungsrichtungen |
|---|---|---|---|---|---|
| K-01 | P3 | Validator Lauf A/B; Tests 012, 041 u. a. (Vermerke) | §5.1-Silbenformenliste ohne VK/VKK/KKVKK, aber eingefrorener Wortschatz und grammatikeigene Beispiele brauchen sie (aul, eird, est, granz, trelm, vresn, skirm, prilm, prens-, dremn-, vlent- …) | §5.1 ↔ §5.3, §10.2, §15.2, §24, §25 | (a) Liste um VK/VKK/KKVKK ergänzen (reine Doku-Korrektur, kein Wort ändert sich); (b) betroffene Wörter ändern (bräche den Wortschatz-Freeze — nicht empfohlen); (c) VK/VKK/KKVKK als markierte historische Ausnahmen führen |
| K-02 | P3 | Validator; §18.2-Beleg | killa/dolla/kella(n) verletzen die Fugenregel §21.4 (l+l unverschmolzen) | §13.4, §18.2 ↔ §21.4 | (a) Pronomen als dokumentierte Ausnahme der Fugenregel; (b) Formen zu kila/dola/kela regularisieren; (c) Fugenregel auf Ableitung/Komposition beschränken (Endungen ausnehmen — dann aber mela/tala neu begründen) |
| K-03 | P3 | Validator | telnxelmmern (35) mit m+m gegen §21.4 | §24.8 ↔ §21.4 | (a) telnxelmern schreiben; (b) Zahlenkomposita von der Fugenregel ausnehmen |
| K-04 | P3 | 060 | §25.1 nutzt tolm adverbial statt tolmun (§12.4) | §12.4 ↔ §25.1 | (a) Beispielsatz auf tolmun korrigieren; (b) endungslose Adverbien bei Gradpartikel als Ausnahme regeln |
| U-01 | P3 | 121, 133 (Anm.) | §15.2-Formel („Ablautstamm + -e- + Endung") deckt es- (suppletiv, vo+Endung, vai-) und die Kontraktionspräsentia nu-/vur- nicht | §15.2 | Formulierung an die (vollständigen, korrekten) Tabellen anpassen |
| U-05 | P3 | 023 u. a. (Anm.) | Objektreihenfolge Dat vor Akk nur Beispielpraxis | §17 | Als Regel oder ausdrückliche Tendenz formulieren |
| U-06 | P3 | 054, 056 (Anm.) | Kasus nach kon/zil ungeregelt (Beispiele: Nominativ) | §12.3 | (a) Nominativ normieren; (b) Kasusübernahme vom Bezugswort |
| U-07 | P3 | 095 (Anm.) | „Konjunktionen systematisch aus Präpositionen + -i" stimmt nur für 4 von 7 (dremi ohne Basis, tund/fai ohne -i) | §20 | Formulierung abschwächen oder Herkunft von dremi/tund/fai dokumentieren |
| U-09 | P3 | 062, 067 (Anm.) | „Echovokal" nur über Tabellen definiert | §9 | Definition ausformulieren (Echovokal = Themavokal; Artikel/Adjektiv: a) |
| U-10 | P3 | Manus-Test | §26.8 „20 Konsonantentasten" — es sind 19 Konsonanten + 1 Vokalträger | §26.8 ↔ §26.2, §2.1 | Terminologie korrigieren („19 Konsonantentasten + 1 Vokalträgertaste") |
| L-10 | P3 | Manus-Test | Strichstärke für f s ş x v z j ç undefiniert (9 von 19 Konsonanten) | §26.9 | Reibelauten/Affrikate eine Stärke zuweisen (z. B. eigene vierte Stärke oder Zuordnung zu mittel/dick) |
| U-11 | P3 | — (§25.2) | Temporaler Dativ ohne Präposition (Vraş zaldreş) ungeregelt | §25.2 ↔ §8, §19 | (a) bloßen Zeit-Dativ als Regel aufnehmen; (b) Beispiel mit Präposition umformulieren |
| U-12 | P3 | — | Imperativ-Stütz-e prüft nur §5.3; Dremn!/Prens!/Vlent! hätten KKVKK-Form (hängt an K-01) | §14 ↔ §5.1 | Mit K-01 gemeinsam entscheiden |
| U-13 | P3 | 055, 057, 121 u. a. (Anm.) | Prädikativ steht in allen Beispielen vor dem Verb (Lo loşn est = V3) — Verhältnis zur V2-Regel ungesagt | §12.2 ↔ §17.1 | (a) Prädikativ+Kopula als eine Position definieren; (b) V2 strikt (Lo est loşn) und §12.2-Beispiele anpassen; (c) Kopulasätze ausdrücklich ausnehmen |

### P3/P4 — Rest

| ID | Priorität | Testnummer | Problem | Betroffene §§ | Mögliche Lösungsrichtungen |
|---|---|---|---|---|---|
| U-14 | P3 | 083, 122, 134 (Anm.) | §18.3-Beispiel „Vim xa num vna breun" lässt das Objekt unmarkiert (regelkonform: vnan breunen) | §18.3 ↔ §8, §10.3, §11 | (a) Beispiel korrigieren; (b) ungeschriebene Regel (unmarkiertes Objekt nach Negation?) explizit machen — wäre neu |
| P7-x | P3/P4 | Phase 7 | Wortschatzkollisionen und Verwechselbarkeiten (unten) | §24 | dokumentieren; nur bei echter Störung (velkran!) Designer-Entscheidung |

---

## PHASE 7 — DUPLIKATE UND WORTSCHATZKOLLISIONEN

Nur dokumentiert, nichts geändert. Maschinelle Basis: Homonym-Scan des Validators (Lauf A) + manuelle Durchsicht aller 281 Grundformen.

### 7.1 Echte Homonyme (identische Form, verschiedene Funktion)

| Form | Lesart 1 | Lesart 2 | Bewertung |
|---|---|---|---|
| **velkran** | Nom. „Freundschaft" (§10.1) | **Akk. von velkra „Freund"** | Härtester Fall: „Vim milkam velkran" ist doppeldeutig (ich sehe den Freund/die Freundschaft [artikellos]); Artikel disambiguiert (xran velkran vs. velkran), aber artikellose Kontexte kollidieren |
| **vran** | unbest. Artikel M Akk (§11) | „sehr" (§24.9) | „vran xarn" (sehr stark) vs. „vran valrun" (einen Mann) — Wortart trennt meist, formal aber identisch |
| **kaun** | Kernwort „Mensch" (§24.1) | Indefinit „man" (§13.4) | dokumentierte Doppelrolle; Artikel disambiguiert |
| **fai** | „dass" (§20) | Relativpronomen (§13.4) | verschärft L-02; solange Relativsätze ungeregelt sind, latent |
| **xa** | „nicht" (§18.3) | Vorsilbe „Gegenteil-" (§21.2) | frei vs. gebunden — unkritisch, aber im Schriftbild identisch anlautend (xakaun „niemand" vs. xa kaun „nicht der Mensch") |
| **mai** | „würde" (§16.2) | — (zufällig identisch mit Zukunftsvokal -ai-) | unkritisch, klanglich motiviert |

### 7.2 Extrem ähnliche Paare (Verwechslungsgefahr)

klaun (wahr) ~ kaun (Mensch) · **nest- (wollen) ~ nast- (essen)** · **tolm (langsam) ~ dolm- (müssen)** · **şaln (dunkel) ~ şlan (trotz)** · kalm (4) ~ kolm (wie) · xer (denn) ~ xerp (Feuer) · zil (wie) ~ zilv (schnell) · nel (1) ~ nul (bei) · luid (hell) ~ luiv (Sonne) · vesn (6) ~ vresn (schwach) · zirv (neu) ~ zirna (morgen) · granz (alt) ~ granza (gestern) · drel (unter) ~ dral (durch) · dremi (während) ~ dremn- (denken) · kelt (was) ~ kelte (etwas) ~ kelsu (jemand). — In flektierten Formen entstehen weitere Zusammenfälle (z. B. 1.-Sg.-Formen von nest-/nast- unterscheiden sich nur im Wurzelvokal: nestam/nastam).

### 7.3 Wortfamilien, deren Ableitung nicht zur Wurzel passt

- **dalvur „immer"** enthält formal dalv- „geben" — Beziehung nirgends erklärt; zugleich zeigt die Reihe **dalvur, xanur, kilur, dolur** ein offenkundig systematisches, aber **undokumentiertes Suffix -ur** (Adverbien).
- **granza „gestern" / zirna „morgen" / nunda „heute"** wirken abgeleitet (granz „alt"? zirv „neu"? nun „jetzt"?), ohne dokumentierte Bildungsregel.
- **dremi „während"** hat entgegen §20 keine Präpositionsbasis (U-07).
- **melvi/talvi** (§21.1, Suffix -vi) sind produktive Ableitungen, stehen aber in keiner Wortliste (§24.7 führt nur die 20 Grundadjektive).

### 7.4 Übrige Prüfpunkte

- **Phonotaktikverstöße:** ausschließlich die K-01-Fälle (VK/VKK/KKVKK); darüber hinaus verstößt kein Wort gegen §5 (maschinell geprüft).
- **Geschlecht ↔ Endung:** 0 Treffer — jedes reguläre Nomen führt das Geschlecht seiner Endung (maschinell geprüft, inkl. §24.6-Abstrakta).
- **Verben in Beispielen vs. Wörterbuch:** narg- „machen" dient in §16.3 unmarkiert als „bauen"; mel- „gehen" in §25.2 als „führen (der Weg ging)" — tolerierbare Dehnungen, sollten im Wörterbuch als Nebenbedeutungen vermerkt werden. salv-/vaşn- (transitiv/intransitiv) sind seit 0.9.3 sauber getrennt: kein Befund.
- **Phantombeispiel:** §5.3 nutzt **frisk** als Coda-Beispiel — das Wort existiert im Wortschatz nicht (einziger fr-Beleg überhaupt). Doku-Randnotiz.
- **eu** ist nur durch breun belegt (§2.3 nennt es selbst „belegt und notwendig" — stimmt, aber einzelner Träger).

---

## ENTSCHEIDUNGSKRITERIUM — GESAMTURTEIL

### NOT READY

— für einen direkten Sprung auf 1.0, nach dem vereinbarten Kriterium: es liegen **mehrere P1-Probleme** vor (sechs: L-01 Genitivstellung, L-02 Relativsatz, L-03 Fragewortkasus, L-04 Reflexiv, L-05 Passiv-Agens, K-05 Modal im Nebensatz). Eine Sprache ohne Relativsätze, ohne „wen/wem/wessen" und ohne Passiv-Agens ist für 1.0 nicht vollständig genug — unabhängig davon, wie gut der Rest hält.

**Das Urteil ist ausdrücklich KEIN Stabilitätsbefund gegen den Kern.** Die Tests zeigen ebenso klar:

1. **Null P0.** Grundlegende Kommunikation (Aussage, Frage, Negation, drei Zeiten, Modalität im Hauptsatz, Passiv ohne Agens, Konditional) funktioniert durchgängig — 130/150 = 86,7 % ohne jede Beanstandung, maschinell gegengeprüft.
2. **Der bereits vollständig definierte reguläre Morphologiekern ist widerspruchsfrei.** Alle 45 Endungen, alle Kasus, beide Pluralsysteme, alle 8 unregelmäßigen Verben, Artikel- und Adjektivkongruenz: 0 Fehler in 130 Sätzen + der [TESTFORM]-Deklinationsmatrix. Präzisierung: „Kern" meint das, was 0.9.3 vollständig definiert — außerhalb davon fehlen Formen (Plural der 10-%-Gruppe L-07, Flexion der Demonstrativa/Indefinita L-06, kem/kelt L-03); das sind dokumentierte Lücken, keine Widersprüche. Die einzigen echten Regelkonflikte (K-01…K-05) sind Dokumentations- bzw. Endfeld-Probleme, kein struktureller Umbaubedarf.
3. **Alle sechs P1-Probleme sind additiv lösbar:** je eine klar umrissene Designentscheidung (eine neue Regel bzw. ein Absatz), keine kollidiert mit bestehenden Regeln, keine erfordert neue Wörter außer ggf. L-05/W-01.

**Empfohlener Weg** (deckt sich mit dem Plan aus 0.9.3 §28): Die 6 P1-Entscheidungen im Designer-Dialog treffen → als 0.9.4 nachtragen (zusammen mit den billigen P3-Redaktionsfixes K-01/K-03/K-04/U-01/U-10) → Regressionslauf dieses Testkorpus (Validator ist wiederverwendbar; die 20 offenen Tests müssten dann [OK] werden) → bei ≥ 95 % ohne neue Befunde: **1.0-RC ist realistisch.** Die P2-Befunde können nach 1.0 als dokumentierte offene Punkte weiterlaufen.

---

*Testbericht 0.1 — erstellt gegen Grammatik 0.9.3, ohne Änderung an der Referenz. Reproduktion: `python3 orbis_validator.py --all` und `--corpus Orbis-Testkorpus-0_1.md`.*
