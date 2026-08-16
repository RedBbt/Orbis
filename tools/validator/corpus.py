# -*- coding: utf-8 -*-
"""tools.validator.corpus — Beispiel- und Korpuspruefung.

Prueft die Belege der Referenzgrammatik und beliebige Korpusdateien.
Wortstellung und Semantik bleiben MANUELLE_PRUEFUNG."""

import re, json, os
from .data import *
from . import data as _d

from .syntax import check_sentence, tokenize

def run_examples():
    out = []
    for ref, s in GRAMMAR_EXAMPLES:
        rep = check_sentence(s)
        probs = []
        unk = [u for u in rep["unbekannt"] if u not in DERIVED_ADJ_VI]
        if unk: probs.append("unbekannte Formen: " + ", ".join(unk))
        for tok, msg in rep["phonotaktik"]: probs.append(f"{tok}: {msg}")
        for tok, gem in rep["geminaten"]:   probs.append(f"{tok}: Geminate {','.join(gem)}")
        for p, n, msg in rep["präp_kasus"]: probs.append(f"{p} {n}: {msg}")
        for a, b, msg in rep["kongruenz"]:  probs.append(f"NP {a} … {b}: {msg}")
        out.append((ref, s, probs))
    return out

def extract_corpus_sentences(path):
    """Zieht 'Orbis:'-Zeilen (Zeile nach 'Orbis:') aus einer Korpusdatei."""
    sents = []
    lines = open(path, encoding="utf-8").read().splitlines()
    cur_test = None
    for i, line in enumerate(lines):
        m = re.match(r"##\s*Test\s*(\d+)", line)
        if m: cur_test = int(m.group(1))
        if line.strip() == "Orbis:" and i + 1 < len(lines):
            nxt = lines[i + 1].strip()
            if nxt and not nxt.startswith("["):
                sents.append((cur_test, nxt))
        m2 = re.match(r"Orbis:\s*(.+)", line)
        if m2 and m2.group(1).strip():
            sents.append((cur_test, m2.group(1).strip()))
    return sents

def run_corpus(path):
    out = []
    for test_no, s in extract_corpus_sentences(path):
        s_clean = re.sub(r"\[.*?\]", "", s).strip()   # Marker im Satz ignorieren
        if not s_clean or s_clean.startswith("—"): continue
        rep = check_sentence(s_clean)
        probs = []
        unk = [u for u in rep["unbekannt"]
               if not (u.startswith("teststamm") or u in DERIVED_ADJ_VI)]
        if unk: probs.append("unbekannte Formen: " + ", ".join(unk))
        for tok, msg in rep["phonotaktik"]:
            if "VK" in msg: continue   # §5.1-Befund wird zentral berichtet
            probs.append(f"{tok}: {msg}")
        for tok, gem in rep["geminaten"]: probs.append(f"{tok}: Geminate {','.join(gem)}")
        for p, n, msg in rep["präp_kasus"]: probs.append(f"{p} {n}: {msg}")
        for a, b, msg in rep["kongruenz"]: probs.append(f"NP {a} … {b}: {msg}")
        vk = [tok for tok, msg in rep["phonotaktik"] if "VK" in msg]
        out.append((test_no, s_clean, probs, vk))
    return out

