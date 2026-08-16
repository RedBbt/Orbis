# -*- coding: utf-8 -*-
"""tools.validator.lexicon — Wortschatzpruefung (Pruefungen 1-6, 12).

Prueft Phoneminventar, Silbenformen, Fugen, Endungen, Genus und Sonderklassen
des gesamten Lexikons. Bedeutungskonflikte sind MANUELLE_PRUEFUNG."""

import re, json, os
from .data import *
from . import data as _d

from .phonology import phonotactics_verdict, check_geminates, check_phonemes, syllabify
from .morphology import full_lexeme_inventory

def run_lexicon():
    """Prüfung 1–6 über das gesamte Lexikon."""
    out = []
    inv = full_lexeme_inventory()
    seen = {}
    for form, cat, meaning in inv:
        w = form.rstrip("-")
        verdict, extra = phonotactics_verdict(w)
        if verdict == "fremdzeichen":
            out.append(("FEHLER", w, cat, "fremde Zeichen: " + ",".join(extra)))
        elif verdict == "verstoß":
            out.append(("FEHLER", w, cat, "keine §5-konforme Silbenzerlegung"))
        elif verdict.startswith("nur-"):
            fehlend = verdict[4:].replace("VK", "VK/VKK", 1) if verdict == "nur-VK" else verdict[4:]
            out.append(("§5.1-BEFUND", w, cat,
                        f"nur mit Silbenform {fehlend} parsebar; §5.1 nennt diese Form nicht"))
        gem = check_geminates(w)
        if gem:
            out.append(("GEMINATE", w, cat,
                        "Doppelkonsonanz " + ",".join(gem) + " — kollidiert mit Fugenregel §21.4"))
        seen.setdefault(w, []).append((cat, meaning))
    # Prüfung 4+5: Nomenendung und Geschlecht
    for noun, kb in REGULAR_NOUNS.items():
        klasse = kb.split(" ", 1)[0]
        g, sub = klasse.split("-")
        end = noun[-2:]
        if end[0] not in GENDER_OF_CONS or end[1] not in THEMA_VOWELS:
            out.append(("ENDUNG", noun, "Nomen", f"Endung '{end}' nicht unter den 45 (§7)"))
        else:
            if GENDER_OF_CONS[end[0]] != g:
                out.append(("GENUS", noun, "Nomen",
                            f"Endung '{end}' → {GENDER_OF_CONS[end[0]]}, geführt als {g}"))
            if SUBCLASS_OF_CONS[end[0]] != sub:
                out.append(("UNTERKLASSE", noun, "Nomen",
                            f"Endung '{end}' → {SUBCLASS_OF_CONS[end[0]]}, geführt als {sub}"))
    # Prüfung 6: Kernwörter als Sonderklasse (kein 45er-Ausgang nötig, -e-/-ei)
    for w in CORE_NOUNS:
        if w[-2:] in [c + v for c in GENDER_OF_CONS for v in THEMA_VOWELS]:
            out.append(("HINWEIS", w, "Kernwort",
                        f"Auslaut '{w[-2:]}' sieht aus wie reguläre Endung — Sonderklasse nur im Wörterbuch erkennbar"))
    # Homonyme im Grundformbestand
    for w, cats in seen.items():
        kinds = {c for c, _ in cats}
        if len(cats) > 1 and len(kinds) > 1:
            out.append(("HOMONYM", w, "/".join(sorted(kinds)),
                        " | ".join(f"{c}: {m}" for c, m in cats)))
    return out

