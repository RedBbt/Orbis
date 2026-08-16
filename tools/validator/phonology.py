# -*- coding: utf-8 -*-
"""tools.validator.phonology — Lautstruktur (§2, §5).

Algorithmen unveraendert aus orbis_validator.py 0.1 uebernommen; die Regeldaten
stammen aus language/phonology/ (siehe data.py)."""

import re, json, os
from .data import *
from . import data as _d

def coda_pair_ok(pair):
    """§5.3: Zweiergruppe am Silbenende erlaubt?
    (a) erster Laut Fliesslaut/Nasal, (b) zweiter Laut s, (c) feste Gruppe."""
    return (pair[0] in CODA_FIRST_OK or pair[1] == CODA_SECOND_S
            or pair in CODA_PAIRS_C)


def check_phonemes(word):
    """Nur die 19 Konsonanten und 5 Vokale aus §2? Liefert Liste fremder Zeichen."""
    return [ch for ch in word if ch not in CONSONANTS and ch not in VOWELS]

# --- Geminaten-Check (Folge der Fugenregel §21.4) -------------------------
def check_geminates(word):
    """§21.4: identische Konsonanten verschmelzen an jeder Fuge. Da kein
    Morphem des Lexikons interne Geminaten hat, ist jede Doppelkonsonanz
    verdächtig. Befund, keine automatische Korrektur."""
    hits = []
    for i in range(len(word) - 1):
        if word[i] == word[i+1] and word[i] in CONSONANTS:
            hits.append(word[i] + word[i+1])
    return hits

# --- Silbenzerlegung (§5) -------------------------------------------------
def _nucleus_options(word, i):
    """Mögliche Nuklei ab Position i: Diphthong (2 Zeichen) vor Einzelvokal."""
    opts = []
    if word[i:i+2] in DIPHTHONGS:
        opts.append(word[i:i+2])
    if word[i] in VOWELS:
        opts.append(word[i])
    return opts

def syllabify(word, shapes=SYLLABLE_SHAPES_STRICT):
    """Alle §5-konformen Zerlegungen von word.
    Silbe = (Onset, Nukleus, Coda). shapes steuert, ob nur die wörtliche
    §5.1-Liste gilt (strikt) oder zusätzlich VK/VKK (erweitert)."""
    results = []

    def shape_of(onset, coda):
        return "K" * len(onset) + "V" + "K" * len(coda)

    def onset_ok(onset):
        if len(onset) == 0: return True
        if len(onset) == 1: return onset in CONSONANTS
        if len(onset) == 2: return onset in ONSETS2       # §5.2
        return False                                       # §5.2: nie >2

    def coda_ok(coda):
        if any(ch not in CONSONANTS for ch in coda): return False
        if len(coda) <= 1: return True
        if len(coda) == 2: return coda_pair_ok(coda)       # §5.3
        return False

    def rec(i, acc):
        if i == len(word):
            results.append(list(acc)); return
        for on_len in (0, 1, 2):
            onset = word[i:i+on_len]
            if len(onset) < on_len or not onset_ok(onset): continue
            j = i + on_len
            if j >= len(word): continue
            for nuc in _nucleus_options(word, j):
                k = j + len(nuc)
                for cd_len in (0, 1, 2):
                    coda = word[k:k+cd_len]
                    if len(coda) < cd_len or not coda_ok(coda): continue
                    if shape_of(onset, coda) not in shapes: continue
                    rec(k + cd_len, acc + [(onset, nuc, coda)])

    rec(0, [])
    # Duplikate entfernen, deterministisch sortieren
    uniq = sorted({tuple(r) for r in results})
    return [list(u) for u in uniq]

def phonotactics_verdict(word):
    """Strikte §5.1-Prüfung mit Zusatzbefund:
    'ok'         — nach wörtlicher §5.1-Liste parsebar
    'nur-VK'     — NUR mit den in §5.1 fehlenden Formen VK/VKK parsebar
    'nur-KKVKK'  — NUR mit der in §5.1 fehlenden Form KKVKK parsebar
    'verstoß'    — auch erweitert nicht parsebar"""
    bad = check_phonemes(word)
    if bad:
        return ("fremdzeichen", bad)
    if syllabify(word, SYLLABLE_SHAPES_STRICT):
        return ("ok", None)
    if syllabify(word, SYLLABLE_SHAPES_KKVKK):
        return ("nur-KKVKK", None)
    if syllabify(word, SYLLABLE_SHAPES_VK):
        return ("nur-VK", None)
    if syllabify(word, SYLLABLE_SHAPES_EXTENDED):
        return ("nur-VK+KKVKK", None)
    return ("verstoß", None)

