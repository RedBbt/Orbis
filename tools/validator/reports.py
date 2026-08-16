# -*- coding: utf-8 -*-
"""tools.validator.reports — Tabellen, Strict-Modus (CI-Baseline)
und die L-09-Berichtsausgabe."""

import re, json, os
from .data import *
from . import data as _d

from .phonology import phonotactics_verdict, syllabify
from .morphology import conj, decline_regular_noun
from .lexicon import run_lexicon
from .corpus import run_examples, run_corpus
from .manus import manus_report_data, fmt_parse, pref_syllabify

TESTSTEM = "pren"   # [TESTFORM]-Stamm, rein morphologischer Träger

def table_45():
    """Vollmatrix: 45 Endungen x 8 Formen (4 Kasus Sg + 4 Kasus Pl) = 360."""
    rows = []
    for g in ("M", "F", "N"):
        for sub in ("A", "B", "C"):
            c = CLASS_CONS[g][sub]
            for v in THEMA_VOWELS:
                lemma = TESTSTEM + c + v
                rows.append((g + "-" + sub, c + v, lemma,
                             decline_regular_noun(lemma, "akk", "sg"),
                             decline_regular_noun(lemma, "dat", "sg"),
                             decline_regular_noun(lemma, "gen", "sg"),
                             decline_regular_noun(lemma, "nom", "pl"),
                             decline_regular_noun(lemma, "akk", "pl"),
                             decline_regular_noun(lemma, "dat", "pl"),
                             decline_regular_noun(lemma, "gen", "pl")))
    return rows

def table_verb(root):
    rows = []
    for t in ("präs", "vgh", "fut"):
        for p in ("1sg", "2sg", "3sg", "1pl", "2pl", "3pl"):
            rows.append((t, p, conj(root, t, p)))
    return rows


BASELINE_PATH = "orbis_baseline.json"

def collect_findings(corpus_path=None):
    """Alle automatischen Befunde als stabile Signaturstrings."""
    sigs = set()
    for kind, w, cat, msg in run_lexicon():
        sigs.add(f"LEX|{kind}|{w}")
    for ref, s, probs in run_examples():
        for p in probs:
            sigs.add(f"EX|{ref}|{p.split(':')[0].strip()}|{p.split(':',1)[1].strip()[:40]}")
    if corpus_path:
        for test_no, s, probs, vk in run_corpus(corpus_path):
            for p in probs:
                sigs.add(f"KORPUS|Test{test_no}|{p[:60]}")
    # 360er-Matrix muss immer vollstaendig §5-konform sein
    for row in table_45():
        for f in row[2:]:
            if phonotactics_verdict(f)[0] != "ok":
                sigs.add(f"MATRIX|{f}|nicht §5-konform")
    return sigs

def run_strict(update=False, corpus_path="Orbis-Testkorpus-0_1.md"):
    import os
    current = collect_findings(corpus_path if os.path.exists(corpus_path) else None)
    if update:
        json.dump(sorted(current), open(BASELINE_PATH, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print(f"Baseline geschrieben: {len(current)} bekannte Befunde -> {BASELINE_PATH}")
        return 0
    try:
        baseline = set(json.load(open(BASELINE_PATH, encoding="utf-8")))
    except FileNotFoundError:
        print(f"FEHLER: {BASELINE_PATH} fehlt. Mit --update-baseline erzeugen.")
        return 1
    new = sorted(current - baseline)
    fixed = sorted(baseline - current)
    print(f"Strict-Lauf: {len(current)} Befunde aktuell, {len(baseline)} in der Baseline.")
    if fixed:
        print(f"{len(fixed)} Baseline-Befunde nicht mehr vorhanden (behoben?):")
        for s in fixed: print("  -", s)
    if new:
        print(f"NEUE BEFUNDE ({len(new)}) — nicht in der Baseline:")
        for s in new: print("  -", s)
        return 1
    print("Keine neuen Befunde. OK.")
    return 0


STRATEGIEN = [
    ("A", "onsetmax", "Onset-Maximierung ohne Diphthong-Vorrang"),
    ("B", "diphthong", "nur Diphthong-Vorrang (Minimal-Onset)"),
    ("C", "max", "Onset-Maximierung + Diphthong-Vorrang"),
    ("D", "lexikalisch", "lexikalisch gespeicherte Silbengrenzen"),
]


def _strategie(wort, modus):
    """Liefert (parse, fehler). Strategie D greift auf gespeicherte Grenzen zurueck;
    da §5 keine festlegt, ist der Speicher leer und D faellt aus."""
    if modus == "lexikalisch":
        from .manus import LEXIKALISCHE_SILBENGRENZEN
        if wort in LEXIKALISCHE_SILBENGRENZEN:
            return LEXIKALISCHE_SILBENGRENZEN[wort], None
        return None, "keine lexikalische Silbengrenze hinterlegt (§5 definiert keine)"
    if modus == "diphthong":
        return pref_syllabify(wort, "min")
    return pref_syllabify(wort, modus)


def run_sim_l09():
    print("== L-09-SIMULATION (KEINE SPRACHREGEL) ==")
    print("Vier Kandidatenstrategien fuer die fehlende Silbifizierungsregel.")
    print("Ergebnis ist ein Bericht — die Grammatik 0.9.3 bleibt unveraendert.\n")
    daten = manus_report_data()
    gesamt = len(daten)
    ambig = [w for w, _c, _p, verd in daten if "AMBIGUITÄT" in verd]
    ergebnisse = {}
    for name, modus, beschreibung in STRATEGIEN:
        geloest, fehlgeschlagen, aufloesungen = 0, [], {}
        for wort, _cat, _parses, verd in daten:
            parse, fehler = _strategie(wort, modus)
            if parse:
                geloest += 1
                aufloesungen[wort] = "·".join("".join(sil) for sil in parse)
            else:
                fehlgeschlagen.append((wort, fehler))
        ergebnisse[name] = (geloest, fehlgeschlagen, aufloesungen, beschreibung)
        print(f"Strategie {name} — {beschreibung}")
        print(f"   eindeutig zerlegt: {geloest}/{gesamt}"
              f" | davon vormals mehrdeutig: "
              f"{sum(1 for w in ambig if w in aufloesungen)}/{len(ambig)}")
        print(f"   Fehlschlaege: {len(fehlgeschlagen)}")
        for wort, fehler in fehlgeschlagen[:6]:
            print(f"      {wort}: {fehler}")
        if len(fehlgeschlagen) > 6:
            print(f"      … und {len(fehlgeschlagen) - 6} weitere")
        print()

    print("== WO DIE STRATEGIEN VERSCHIEDEN ENTSCHEIDEN ==")
    print("(nur hier ist die Wahl ueberhaupt sichtbar; Designerentscheidung noetig)\n")
    unterschiede = []
    for wort, _cat, _parses, _verd in daten:
        formen = {}
        for name, _modus, _b in STRATEGIEN:
            a = ergebnisse[name][2].get(wort)
            if a:
                formen.setdefault(a, []).append(name)
        if len(formen) > 1:
            unterschiede.append((wort, formen))
    for wort, formen in unterschiede:
        teile = "   |   ".join(f"{'/'.join(namen)}: {form}" for form, namen in formen.items())
        print(f"   {wort}:  {teile}")
    print(f"\n{len(unterschiede)} Formen mit abweichender Zerlegung.")
    print(f"{len(ambig)} der {gesamt} Grundformen sind ohne Regel mehrdeutig (Befund L-09).")
    print("\nHINWEIS: Dieses Werkzeug entscheidet nichts. Die Aufnahme einer "
          "Silbifizierungsregel in die Grammatik ist eine Designerentscheidung "
          "(siehe decisions/Entscheidungsvorlage-0_9_4.md, E7).")
    return 0
