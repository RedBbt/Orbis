# -*- coding: utf-8 -*-
"""tools.validator.manus — Manus-Silbenzerlegung (§26) und
L-09-Simulationen. Die Simulationen sind Analysewerkzeuge, KEINE Sprachregeln."""

import re, json, os
from .data import *
from . import data as _d

from .phonology import syllabify, coda_pair_ok
from .morphology import full_lexeme_inventory

def manus_report_data():
    """Silbenzerlegung des Grundwortschatzes nach §26.1.
    Liefert (wort, kategorie, parses, verdikt)."""
    data = []
    for form, cat, _ in full_lexeme_inventory():
        w = form.rstrip("-")
        strict = syllabify(w, SYLLABLE_SHAPES_STRICT)
        ext = syllabify(w, SYLLABLE_SHAPES_EXTENDED)
        parses = strict if strict else ext
        if not parses:
            verdict = "NICHT ZERLEGBAR"
        elif len(parses) == 1:
            verdict = "eindeutig" + ("" if strict else " (nur mit VK/VKK)")
        else:
            verdict = f"[MANUS-AMBIGUITÄT] {len(parses)} Zerlegungen" + \
                      ("" if strict else " (nur mit VK/VKK)")
        data.append((w, cat, parses, verdict))
    return data

def fmt_parse(p):
    return "·".join("".join(s) for s in p) + "  (" + \
           " ".join(f"[{o}|{n}|{c}]" for o, n, c in p) + ")"



# --- L-09: deterministische Silbifizierung (SIMULATION) -------------------
LEXIKALISCHE_SILBENGRENZEN = {}   # Strategie D: bewusst leer (§5 kennt keine)


def pref_syllabify(word, mode="max"):
    """Deterministische Zerlegung nach Kandidatenregel:
    1. Diphthong-Vorrang: an jeder Vokalstelle wird der laengste Nukleus
       (Diphthong vor Einzelvokal) gewaehlt.
    2. Onset-Zuweisung fuer jede Konsonantengruppe zwischen zwei Nuklei:
       mode='max' -> maximal zulaessiger Onset der Folgesilbe (2 wenn in
       §5.2-Liste, sonst 1); mode='min' -> genau 1 Konsonant als Onset,
       Rest als Coda.
    Wortinitiale Gruppe = ganz Onset, wortfinale Gruppe = ganz Coda.
    Liefert (parse, fehler): parse als [(onset,nukleus,coda), ...] oder None."""
    # Kette in Nuklei und Konsonantengruppen zerlegen (Diphthong-Vorrang)
    diphthong_vorrang = mode in ("max", "min", "maxdi", "mindi")
    units = []; i = 0
    while i < len(word):
        if word[i] in VOWELS:
            if diphthong_vorrang and word[i:i+2] in DIPHTHONGS:
                units.append(("V", word[i:i+2])); i += 2
            else:
                units.append(("V", word[i])); i += 1
        elif word[i] in CONSONANTS:
            j = i
            while j < len(word) and word[j] in CONSONANTS: j += 1
            units.append(("K", word[i:j])); i = j
        else:
            return None, f"fremdes Zeichen {word[i]!r}"
    sylls = []; onset = ""
    for idx, (kind, seg) in enumerate(units):
        if kind == "K":
            if idx == 0:
                onset = seg
                if len(onset) > 2 or (len(onset) == 2 and onset not in ONSETS2):
                    return None, f"Anlautgruppe {onset!r} unzulaessig"
            elif idx == len(units) - 1:
                if not sylls: return None, "keine Silbe vor Endgruppe"
                if len(seg) > 2: return None, f"Endgruppe {seg!r} zu lang"
                if len(seg) == 2 and not coda_pair_ok(seg):
                    return None, f"Endgruppe {seg!r} unzulaessig (§5.3)"
                o, n, c = sylls[-1]
                if c: return None, "Coda-Kollision"
                sylls[-1] = (o, n, seg)
            else:
                take = 0
                if mode in ("max", "maxdi", "onsetmax"):
                    if len(seg) >= 2 and seg[-2:] in ONSETS2: take = 2
                    elif seg[-1] in CONSONANTS: take = 1
                else:
                    take = 1
                coda = seg[:len(seg) - take]; onset = seg[len(seg) - take:]
                if len(coda) > 2: return None, f"Restcoda {coda!r} zu lang"
                if len(coda) == 2 and not coda_pair_ok(coda):
                    return None, f"Restcoda {coda!r} unzulaessig (§5.3)"
                if coda:
                    o, n, c = sylls[-1]
                    if c: return None, "Coda-Kollision"
                    sylls[-1] = (o, n, coda)
        else:
            sylls.append((onset, seg, "")); onset = ""
    if onset and not sylls:
        return None, "kein Nukleus"
    return sylls, None

