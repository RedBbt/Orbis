# ORBIS — Validator-Bericht 0.1

*Ergebnis der automatischen Konsistenzprüfung (`orbis_validator.py`) gegen den gesamten Wortschatz und alle Beispielsätze der Grammatik 0.9.3 sowie gegen beide Testkorpora. Die Grammatik wurde nicht verändert.*

## 1. Was das Skript prüft — und was nicht

Automatisch geprüft (die 12 geforderten Prüfungen):

| Nr. | Prüfung | Status |
|---|---|---|
| 1 | Nur erlaubte Orbis-Laute (19 K + 5 V, §2) | automatisch |
| 2 | Anfangscluster gegen die 25er-Liste (§5.2) | automatisch (über Silbenzerlegung) |
| 3 | Endcluster gegen §5.3 a/b/c | automatisch (über Silbenzerlegung) |
| 4 | Reguläre Nomen tragen eine gültige der 45 Endungen (§7) | automatisch |
| 5 | Geschlecht der Nomen passt zur Endung | automatisch |
| 6 | 15 Kernwörter als Sonderklasse (eigene Deklination -e-/-ei) | automatisch |
| 7 | Artikelformen nach Geschlecht/Numerus/Kasus (§11) | automatisch (Formen + NP-Kongruenzheuristik) |
| 8 | Pluralformen nach §9 (Echovokal) bzw. §10.3 (-ei) | automatisch |
| 9 | Reguläre Verbformen = Wurzel + Tempusvokal + Personendung | automatisch |
| 10 | Die 8 unregelmäßigen Verben gesondert (belegte Tabellen) | automatisch |
| 11 | Präposition verlangt den festgelegten Kasus (§19) | teilautomatisch: Heuristik über den Folge-Artikel/-Pronomen; Distanzstellungen: MANUELLE_PRÜFUNG |
| 12 | Lexeme ohne widersprüchliche Bedeutungsverwendung | MANUELLE_PRÜFUNG (Homonym-Erkennung automatisch, Bewertung manuell — Phase 7 im Testbericht) |

Grundsätzlich MANUELLE_PRÜFUNG (nicht algorithmisch entscheidbar): V2-Stellung, Verbklammer, Nebensatz-Endstellung, Kongruenz über Distanz, Genitivattribut-Stellung, Semantik/Idiomatik. Zusätzlich implementiert, über die Aufgabenliste hinaus: Geminaten-Check (Fugenregel §21.4), strikte §5.1-Silbenformprüfung, NP-Kongruenzheuristik (meldet nur, wenn KEINE Lesartkombination passt).

## 2. Lauf A — Gesamter Wortschatz (281 Grundformen)

```
[§5.1-BEFUND] aul (Kernwort-N): nur mit Silbenform VK/VKK parsebar; §5.1 nennt diese Form nicht
[§5.1-BEFUND] eird (Kernwort-F): nur mit Silbenform VK/VKK parsebar; §5.1 nennt diese Form nicht
[§5.1-BEFUND] prilm (Nomen10%-F): nur mit Silbenform KKVKK parsebar; §5.1 nennt diese Form nicht
[§5.1-BEFUND] aulmelna (Nomen-Komp-N): nur mit Silbenform VK/VKK parsebar; §5.1 nennt diese Form nicht
[§5.1-BEFUND] dremn (Verbwurzel): nur mit Silbenform KKVKK parsebar; §5.1 nennt diese Form nicht
[§5.1-BEFUND] prens (Verbwurzel): nur mit Silbenform KKVKK parsebar; §5.1 nennt diese Form nicht
[§5.1-BEFUND] vlent (Verbwurzel): nur mit Silbenform KKVKK parsebar; §5.1 nennt diese Form nicht
[FEHLER] suvr (Modalwurzel): keine §5-konforme Silbenzerlegung
[§5.1-BEFUND] es (Verbwurzel-irr): nur mit Silbenform VK/VKK parsebar; §5.1 nennt diese Form nicht
[§5.1-BEFUND] granz (Adjektiv): nur mit Silbenform KKVKK parsebar; §5.1 nennt diese Form nicht
[§5.1-BEFUND] trelm (Adjektiv): nur mit Silbenform KKVKK parsebar; §5.1 nennt diese Form nicht
[§5.1-BEFUND] vresn (Adjektiv): nur mit Silbenform KKVKK parsebar; §5.1 nennt diese Form nicht
[GEMINATE] kella (Fragewort-adj): Doppelkonsonanz ll — kollidiert mit Fugenregel §21.4
[GEMINATE] killa (Demonstrativ): Doppelkonsonanz ll — kollidiert mit Fugenregel §21.4
[GEMINATE] dolla (Demonstrativ): Doppelkonsonanz ll — kollidiert mit Fugenregel §21.4
[GEMINATE] telnxelmmern (Zahl-Komp): Doppelkonsonanz mm — kollidiert mit Fugenregel §21.4
[§5.1-BEFUND] skirm (Partikel/Adverb): nur mit Silbenform KKVKK parsebar; §5.1 nennt diese Form nicht
[§5.1-BEFUND] ain (Partikel/Adverb): nur mit Silbenform VK/VKK parsebar; §5.1 nennt diese Form nicht
[§5.1-BEFUND] oñ (Pronomenform): nur mit Silbenform VK/VKK parsebar; §5.1 nennt diese Form nicht
[HOMONYM] kaun (Indefinit/Kernwort-M): Kernwort-M: Mensch | Indefinit: man (homonym: Mensch)
[HOMONYM] fai (Konj-sub/Relativ): Relativ: der/die/das | Konj-sub: dass
[HOMONYM] vran (Artikelform/Partikel/Adverb): Partikel/Adverb: sehr (homonym: vran = unbest. Artikel M Akk) | Artikelform: ('unbestimmt', 'M', 'akk')
```

**Auswertung:** 14 Formen sind nur mit Silbenformen parsebar, die §5.1 nicht führt (VK/VKK bzw. KKVKK) → Befund **K-01**. 4 Formen tragen eine Doppelkonsonanz gegen die Fugenregel §21.4 → Befunde **K-02** (killa/dolla/kella) und **K-03** (telnxelmmern). 3 echte Homonymien im Grundformbestand (kaun, fai, vran) → Phase 7. Der eine FEHLER (suvr) betrifft die **bloße Wurzel**, die als Wortform nie allein steht — §14 fängt genau diesen Fall mit dem Imperativ-Stütz-e ab (*Suvre!*); kein eigenständiger Befund. **Alle übrigen Prüfungen (Endungen, Genus, Unterklassen, Kernwort-Sonderklasse) laufen ohne einen einzigen Treffer durch: kein reguläres Nomen trägt eine falsche Endung, kein Geschlecht widerspricht seiner Endung.**

## 3. Lauf B — Alle Beispielsätze der Grammatik (71 Belege)

54 von 71 Belegen ohne Befund. Die 17 Treffer:

```
§12.2  Lo loşn est.
    -> est: nur mit VK parsebar — §5.1 nennt diese Form nicht
§12.2  Xna breun granz stanat.
    -> granz: nur mit KKVKK parsebar — §5.1 nennt diese Form nicht
§12.3  Ro vlaidvi est kon vim.
    -> est: nur mit VK parsebar — §5.1 nennt diese Form nicht
§12.3  Lo loşn est zil luiv.
    -> est: nur mit VK parsebar — §5.1 nennt diese Form nicht
§11.3  xlan eirden
    -> eirden: nur mit VK parsebar — §5.1 nennt diese Form nicht
§16.2  Tund vim vra vlaidra valru mai em, mai traivam vim xlan eirden.
    -> em: nur mit VK parsebar — §5.1 nennt diese Form nicht
    -> eirden: nur mit VK parsebar — §5.1 nennt diese Form nicht
§16.3  Xna breun şunargut est.
    -> est: nur mit VK parsebar — §5.1 nennt diese Form nicht
§18.2  Kellan sarlan milkoş?
    -> kellan: Geminate ll
§19  Vim em tel xlaş kavlaş.
    -> em: nur mit VK parsebar — §5.1 nennt diese Form nicht
§25.1  Vim xa valnam soñex, grali xla kirva vran luid est.
    -> est: nur mit VK parsebar — §5.1 nennt diese Form nicht
§25.1  Tund vim vra vlaidra valru mai em, mai traivam vim xlan eirden.
    -> em: nur mit VK parsebar — §5.1 nennt diese Form nicht
    -> eirden: nur mit VK parsebar — §5.1 nennt diese Form nicht
§25.1  Xna breun granz stanat, klas xla kavla zirv vurt.
    -> granz: nur mit KKVKK parsebar — §5.1 nennt diese Form nicht
§25.1  Xnan melnan traivamen viñ, tund xla luiv luid est.
    -> est: nur mit VK parsebar — §5.1 nennt diese Form nicht
§25.2  Vra melru molet dral xrañan trelmrañan zaldreñen.
    -> trelmrañan: nur mit KKVKK parsebar — §5.1 nennt diese Form nicht
§25.2  Ze ro dremnot: Kilna est xna traivute.
    -> est: nur mit VK parsebar — §5.1 nennt diese Form nicht
§25.2  Tel xraş navildoş milkot ro xlan luiven xlas eirdes.
    -> eirdes: nur mit VK parsebar — §5.1 nennt diese Form nicht
§24.8  xelmnel dramxelm telnxelmmern
    -> telnxelmmern: Geminate mm
```

**Auswertung:** Sämtliche Treffer gehen auf genau drei bekannte Befunde zurück: K-01 (est/em/eirden/granz/trelmrañan — die Grammatik verletzt in den eigenen Beispielen ihre eigene Silbenformenliste), K-02 (kellan) und K-03 (telnxelmmern). **Kein Beispielsatz enthält eine unbekannte Wortform oder einen morphologischen Widerspruch zum kodierten Regelwerk** — mit einer Ausnahme, die manuell gefunden wurde und maschinell nicht erkennbar ist: §18.3 „Vim xa num **vna breun**“ lässt das Objekt unmarkiert (regelkonform wäre *vnan breunen*) → Befund **U-14** im Testbericht.

## 4. Lauf C — Chat-Testkorpus 0.1 (Gegenprobe)

145 Orbis-Sätze extrahiert, 144 ohne Befund. Treffer:

```
Satz 48: Xla loşna sarla talat.
    -> NP xla…sarla: keine gemeinsame Genus/Kasus/Numerus-Lesart in der NP
```

**Auswertung:** Der Chat-Entwurf enthält einen echten, dort unentdeckten Kongruenzfehler: Satz 48 *Xla loşna sarla talat* — *loşna* ist die **Neutrum**-Form (loşn+na mit Fusion), die Feminin-Form lautet *loşnla*. Der Satz war im Chat-Korpus mit ✓ bewertet. In der Prüffassung korrigiert (Test 048). Zusätzlich manuell gefunden, maschinell nicht greifbar: Satz 39 übernimmt den §25.1-Adverbkonflikt (K-04), Satz 111 wertet den ungeregelten Modal-Vollverbgebrauch als ✓ (U-03).

## 5. Lauf D — Prüffassung Testkorpus 0.1 (150 Tests)

**130 von 130 bildbaren Orbis-Sätzen ohne automatischen Befund** (die 20 als Lücke/Konflikt/Unklarheit/Testproblem markierten Tests enthalten definitionsgemäß keinen prüfbaren Satz). 
Kein Satz enthält eine unbekannte Wortform, einen Phonotaktikverstoß (jenseits K-01), eine Geminate, einen Präpositionskasus-Fehler oder eine NP-Inkongruenz.

Zusätzlich wurden die 360 [TESTFORM]-Deklinationsformen des Anhangs (45 Endungen × 8 Formen, volle Kasus-/Numerus-Matrix) maschinell erzeugt und §5-geprüft: alle konform.

## 6. Selbstvalidierung des Validators

Der Erkenner wurde gegen Positiv- und Negativproben getestet: absichtliche Genusfehler (*xlan narkun* → gemeldet), Kasusfehler nach Präposition (*tel xlas kavlan* → gemeldet), Unsinnswörter (*blorg, zzz* → gemeldet) und alle 71 Grammatikbelege (keine falsch-positiven Kongruenz- oder Lexikmeldungen). Grenzen: Wortstellung und Semantik bleiben MANUELLE_PRÜFUNG; die NP-Heuristik prüft nur zusammenhängende Artikel-Adjektiv-Nomen-Folgen.

*Reproduktion: `python3 orbis_validator.py --all` bzw. `--corpus Orbis-Testkorpus-0_1.md`.*
