# -*- coding: utf-8 -*-
"""tools.validator.syntax — Satzpruefung (§17-§20).

Automatisch geprueft werden Lexik, Morphologie, Phonotaktik, NP-Kongruenz und
Praepositionskasus. Wortstellung und Semantik bleiben MANUELLE_PRUEFUNG."""

import re, json, os
from .data import *
from . import data as _d

from .phonology import phonotactics_verdict, check_geminates, syllabify
from .morphology import classify_token

def strip_punct(text):
    return re.sub(r"[.,;:!?„“\"»«…()\-—]", " ", text)

def tokenize(sentence):
    return [t.lower() for t in strip_punct(sentence).split() if t]

def check_sentence(sentence):
    """Automatisch prüfbar: Lexik/Morphologie je Token, Phonotaktik,
    Geminaten, Präposition->Kasus (Heuristik über Folge-Artikel/-Pronomen).
    NICHT automatisch entscheidbar (MANUELLE_PRÜFUNG): V2-Stellung,
    Verbklammer, Nebensatz-Endstellung, Kongruenz über Distanz, Semantik."""
    report = {"satz": sentence, "unbekannt": [], "phonotaktik": [],
              "geminaten": [], "präp_kasus": [], "kongruenz": [], "lesarten": {}}
    toks = tokenize(sentence)
    for tok in toks:
        r = classify_token(tok)
        report["lesarten"][tok] = r
        if not r:
            report["unbekannt"].append(tok)
        verdict, extra = phonotactics_verdict(tok)
        if verdict.startswith("nur-"):
            report["phonotaktik"].append((tok, f"nur mit {verdict[4:]} parsebar — §5.1 nennt diese Form nicht"))
        elif verdict == "verstoß":
            report["phonotaktik"].append((tok, "keine §5-konforme Zerlegung"))
        elif verdict == "fremdzeichen":
            report["phonotaktik"].append((tok, "fremde Zeichen: " + ",".join(extra)))
        gem = check_geminates(tok)
        if gem:
            report["geminaten"].append((tok, gem))
    # Heuristik: NP-Kongruenz Artikel (+Adjektive) + Nomen in Folge.
    # Konservativ: gemeldet wird nur, wenn KEINE Lesartkombination passt.
    def _g_of_klasse(klasse):
        for ch in klasse:
            if ch in "MFN": return ch
        return None
    def noun_triples(readings):
        out = set()
        for kind, desc in readings:
            if kind == "NOMEN":
                parts = desc.split()
                g = _g_of_klasse(parts[1])
                if g: out.add((g, parts[2], parts[3]))
        return out
    def adj_triples(readings):
        out = set(); is_adj = False
        for kind, desc in readings:
            if kind in ("ADJ", "W-ADJ") and ("attr" in desc or kind == "W-ADJ"):
                parts = desc.split()
                if kind == "ADJ":
                    g, cn = parts[2], parts[3]
                    if "-" in cn:
                        c, n = cn.split("-"); out.add((g, c, n)); is_adj = True
                else:
                    out.add((parts[1], parts[2], parts[3])); is_adj = True
        return out if is_adj else None
    i = 0
    while i < len(toks):
        r = report["lesarten"].get(toks[i], [])
        art_triples = {tuple(d.split("-")[1:4]) for k, d in r if k == "ART"}
        if art_triples:
            j = i + 1; adj_list = []; nset = None; last = None
            while j < len(toks) and j <= i + 3:
                rj = report["lesarten"].get(toks[j], [])
                nt = noun_triples(rj)
                if nt: nset = nt; last = toks[j]; break
                at = adj_triples(rj)
                if at: adj_list.append(at); j += 1; continue
                break
            if nset is not None:
                inter = art_triples & nset
                for at in adj_list: inter &= at
                if not inter:
                    report["kongruenz"].append(
                        (toks[i], last, "keine gemeinsame Genus/Kasus/Numerus-Lesart in der NP"))
        i += 1
    # Heuristik: Präposition + nächster Artikel/Pronomen-Kasus
    for i, tok in enumerate(toks):
        if tok in PREPOSITIONS:
            need = PREPOSITIONS[tok]
            for j in (i + 1, i + 2):
                if j >= len(toks): break
                nxt = toks[j]
                cases = set()
                if nxt in ARTICLES: cases = {ARTICLES[nxt][2]}
                elif nxt in PRONOUNS: cases = {PRONOUNS[nxt][1]}
                elif nxt in NOUN_FORMS:
                    cases = {c for (_, _, c, _) in NOUN_FORMS[nxt]}
                if cases:
                    if not (cases & need):
                        report["präp_kasus"].append(
                            (tok, nxt, f"verlangt {sorted(need)}, gefunden {sorted(cases)}"))
                    break
    return report

