# -*- coding: utf-8 -*-
"""tools.validator.morphology — Formenbildung und Formenerkennung
(§7-§16, §21). Regeldaten aus language/morphology/."""

import re, json, os
from .data import *
from . import data as _d

from .phonology import syllabify, phonotactics_verdict, check_geminates, check_phonemes

def decline_regular_noun(noun, case, number):
    """§8/§9: Stamm+Klassenkons.+Themavokal (+ñ+Echovokal) + Kasusmarker."""
    thema = noun[-1]
    if number == "sg":
        return noun + CASE_MARKERS[case]
    if case == "nom":
        return noun + "ñ"
    return noun + "ñ" + thema + CASE_MARKERS[case]

def decline_core_noun(word, case, number):
    """§10.3: Sg Bindevokal -e-, Pl -ei; Nom Sg endungslos."""
    if number == "sg":
        return word if case == "nom" else word + "e" + CASE_MARKERS[case]
    return word + "ei" + CASE_MARKERS[case]

def decline_tenpct_noun(word, case, number):
    """§10.1: Sg mit Bindevokal -e-. Plural ist in §10.1 NICHT geregelt."""
    if number == "sg":
        return word if case == "nom" else word + "e" + CASE_MARKERS[case]
    return None   # [REGELLÜCKE] Plural der 10%-Gruppe

ADJ_GENDER_CONS = {"M": "r", "F": "l", "N": "n"}

def fuse(a, b):
    """§21.4 Fugenregel: identische Konsonanten an der Fuge verschmelzen."""
    if a and b and a[-1] == b[0] and a[-1] in CONSONANTS:
        return a + b[1:]
    return a + b

def adj_attributive(stem, gender, case, number, grade=None):
    """§12.1/§12.3: Stamm (+vi/vax) + r/l/n + a + Marker, mit Fugenregel."""
    if grade:
        stem = fuse(stem, COMPARISON_INFIXES[grade])
    base = fuse(stem, ADJ_GENDER_CONS[gender] + "a")
    if number == "sg":
        return base + CASE_MARKERS[case]
    if case == "nom":
        return base + "ñ"
    return base + "ñ" + "a" + CASE_MARKERS[case]

def adj_predicative(stem, grade=None):
    return fuse(stem, COMPARISON_INFIXES[grade]) if grade else stem

def conj_regular(root, tense, person):
    """§14/§15: Wurzel + Tempusvokal + Personendung."""
    return root + TENSE_VOWELS[tense] + PERSON_ENDINGS[person]

def conj(root, tense, person):
    if root in IRREGULAR_VERBS:
        return IRREGULAR_VERBS[root][tense][person]
    return conj_regular(root, tense, person)

# --- Erkennungs-Lexika (alle wohlgeformten Wortformen) --------------------
def _build_recognizers():
    noun_forms = {}   # form -> (lemma, klasse, kasus, numerus)
    for noun, kb in REGULAR_NOUNS.items():
        klasse = kb.split(" ", 1)[0]
        for case in CASES:
            for num in ("sg", "pl"):
                f = decline_regular_noun(noun, case, num)
                noun_forms.setdefault(f, []).append((noun, klasse, case, num))
    for noun, (g, _) in CORE_NOUNS.items():
        for case in CASES:
            for num in ("sg", "pl"):
                f = decline_core_noun(noun, case, num)
                noun_forms.setdefault(f, []).append((noun, "Kern-" + g, case, num))
    for noun, (g, _) in TENPCT_NOUNS.items():
        for case in CASES:
            f = decline_tenpct_noun(noun, case, "sg")
            noun_forms.setdefault(f, []).append((noun, "10%-" + g, case, "sg"))
    for noun, (g, _, note) in COMPOUND_NOUNS.items():
        # Kopf regulär -> regulär deklinieren; Kernwort-Kopf: beide Muster
        # sind unbelegt, §21.3 schweigt -> nur Nominativ als sicher führen.
        if "Kernwort" in note:
            noun_forms.setdefault(noun, []).append((noun, "Komp-" + g + "(?)", "nom", "sg"))
        else:
            for case in CASES:
                for num in ("sg", "pl"):
                    f = decline_regular_noun(noun, case, num)
                    noun_forms.setdefault(f, []).append((noun, "Komp-" + g, case, num))

    verb_forms = {}   # form -> beschreibung
    all_roots = dict(REGULAR_VERB_ROOTS); all_roots.update(MODAL_ROOTS)
    for root in all_roots:
        for t in TENSE_VOWELS:
            for p in PERSON_ENDINGS:
                verb_forms.setdefault(conj_regular(root, t, p), []).append((root, t, p))
        verb_forms.setdefault(fuse(root, "ex"), []).append((root, "inf", "-"))
        verb_forms.setdefault(fuse(root, "ut"), []).append((root, "part", "-"))
    for root, tbl in IRREGULAR_VERBS.items():
        for t in ("präs", "vgh", "fut"):
            for p, f in tbl[t].items():
                verb_forms.setdefault(f, []).append((root, t, p))
        verb_forms.setdefault(tbl["inf"], []).append((root, "inf", "-"))
        verb_forms.setdefault(fuse(root, "ut"), []).append((root, "part", "-"))

    adj_forms = {}    # form -> beschreibung
    for stem in ADJECTIVES:
        adj_forms.setdefault(stem, []).append((stem, "präd", "-", "-"))
        adj_forms.setdefault(fuse(stem, "un"), []).append((stem, "adverb", "-", "-"))
        for grade in (None, "komp", "sup"):
            if grade:
                adj_forms.setdefault(adj_predicative(stem, grade), []).append(
                    (stem, "präd-" + grade, "-", "-"))
            for g in ("M", "F", "N"):
                for case in CASES:
                    for num in ("sg", "pl"):
                        f = adj_attributive(stem, g, case, num, grade)
                        adj_forms.setdefault(f, []).append(
                            (stem, "attr" + ("-" + grade if grade else ""), g, case + "-" + num))
        # §12.5 Nominalisierung
        adj_forms.setdefault(fuse(stem, "ru"), []).append((stem, "nomin-M", "-", "-"))
        adj_forms.setdefault(fuse(stem, "la"), []).append((stem, "nomin-F", "-", "-"))
        adj_forms.setdefault(fuse(stem, "te"), []).append((stem, "nomin-N", "-", "-"))

    # welch- kongruiert laut §18.2-Beispiel adjektivisch ("Kellan sarlan").
    # Achtung: die belegte Form kella verletzt die Fugenregel §21.4 (kel+la
    # müsste kela ergeben) — der Erkenner folgt den BELEGTEN Formen, der
    # Geminaten-Check meldet den Konflikt separat.
    w_adj_forms = {}
    for stem_full, g in W_ADJ.items():
        for case in CASES:
            w_adj_forms.setdefault(stem_full + CASE_MARKERS[case], []).append(
                ("kel-", g, case, "sg"))
        w_adj_forms.setdefault(stem_full + "ñ", []).append(("kel-", g, "nom", "pl"))
        for case in ("akk", "dat", "gen"):
            w_adj_forms.setdefault(stem_full + "ña" + CASE_MARKERS[case], []).append(
                ("kel-", g, case, "pl"))

    # §12.5: Partizip + -te -> -ute (traivute)
    part_nom = {}
    for root in list(all_roots) + list(IRREGULAR_VERBS):
        part_nom[fuse(fuse(root, "ut"), "te")] = root

    # Ordnungszahlen §24.8: Zahl + -ost- + Geschlechtsendung (adjektivisch)
    ord_forms = {}
    for num_word in NUMBERS:
        for g in ("M", "F", "N"):
            for case in CASES:
                f = adj_attributive(fuse(num_word, ORDINAL_INFIX), g, case, "sg")
                ord_forms.setdefault(f, []).append((num_word, g, case))

    return noun_forms, verb_forms, adj_forms, w_adj_forms, part_nom, ord_forms

(NOUN_FORMS, VERB_FORMS, ADJ_FORMS, W_ADJ_FORMS, PART_NOM, ORD_FORMS) = _build_recognizers()

def classify_token(tok):
    """Alle regelkonformen Lesarten eines Tokens. Leere Liste = unbekannt."""
    readings = []
    if tok in ARTICLES:
        d, g, c, n = ARTICLES[tok]
        readings.append(("ART", f"{d}-{g}-{c}-{n}"))
    if tok in PRONOUNS:
        readings.append(("PRON", "-".join(PRONOUNS[tok])))
    if tok in DEMONSTRATIVES: readings.append(("DEM", DEMONSTRATIVES[tok]))
    if tok in REFLEXIVE:      readings.append(("REFL", "se (indeklinabel? §13.4 offen)"))
    if tok in RELATIVE:       readings.append(("REL/SUB", "fai (Relativ ODER dass)"))
    if tok in INDEFINITES:    readings.append(("INDEF", INDEFINITES[tok]))
    if tok in W_WORDS:        readings.append(("W", W_WORDS[tok]))
    if tok in PREPOSITIONS:   readings.append(("PRÄP", "+".join(sorted(PREPOSITIONS[tok]))))
    if tok in CONJ_COORD:     readings.append(("KONJ", CONJ_COORD[tok]))
    if tok in CONJ_SUB:       readings.append(("SUBKONJ", CONJ_SUB[tok]))
    if tok in NUMBERS:        readings.append(("ZAHL", str(NUMBERS[tok])))
    if tok in NUMBER_COMPOUNDS: readings.append(("ZAHL", str(NUMBER_COMPOUNDS[tok])))
    if tok in PARTICLES:      readings.append(("PART", PARTICLES[tok]))
    if tok in NOUN_FORMS:
        for lemma, klasse, case, num in NOUN_FORMS[tok]:
            readings.append(("NOMEN", f"{lemma} {klasse} {case} {num}"))
    if tok in ADJ_FORMS:
        for stem, art, g, cn in ADJ_FORMS[tok]:
            readings.append(("ADJ", f"{stem} {art} {g} {cn}"))
    if tok in W_ADJ_FORMS:
        for stem, g, case, num in W_ADJ_FORMS[tok]:
            readings.append(("W-ADJ", f"welch- {g} {case} {num}"))
    if tok in PART_NOM: readings.append(("PART-NOM", PART_NOM[tok] + "-ute"))
    if tok in ORD_FORMS:
        for num_word, g, case in ORD_FORMS[tok]:
            readings.append(("ORD", f"{num_word}-ost {g} {case}"))
    # Verbformen, auch mit Vorsilben (şu-, re-, dra-, su-) und Imperative
    def verb_readings(t, prefix=""):
        out = []
        if t in VERB_FORMS:
            for root, tense, per in VERB_FORMS[t]:
                out.append(("VERB", f"{prefix}{root}- {tense} {per}"))
        all_roots = set(REGULAR_VERB_ROOTS) | set(MODAL_ROOTS) | set(IRREGULAR_VERBS)
        if t in all_roots:
            out.append(("VERB", f"{prefix}{t}- Imperativ Sg (§14)"))
        for root in all_roots:
            if t == fuse(root, "eñ"):
                out.append(("VERB", f"{prefix}{root}- Imperativ Pl (§14)"))
            # Imperativ mit Stütz-e bei unzulässiger Endgruppe (§14: Suvre!)
            if t == root + "e" and not syllabify(root, SYLLABLE_SHAPES_EXTENDED):
                out.append(("VERB", f"{prefix}{root}- Imperativ Sg +e (§14)"))
        return out
    readings += verb_readings(tok)
    for pre in VERB_PREFIXES:
        if tok.startswith(pre):
            readings += verb_readings(tok[len(pre):], prefix=pre + "+")
    # xa-/su- als Adjektiv-Vorsilben (§21.2: xaselvra, suluidra)
    for pre in ("xa", "su"):
        if tok.startswith(pre) and tok[len(pre):] in ADJ_FORMS:
            for stem, art, g, cn in ADJ_FORMS[tok[len(pre):]]:
                readings.append(("ADJ", f"{pre}+{stem} {art} {g} {cn}"))
    return readings


def full_lexeme_inventory():
    """(form, kategorie, bedeutung) für alle Grundformen des Lexikons."""
    inv = []
    for w, (g, b) in CORE_NOUNS.items():   inv.append((w, "Kernwort-"+g, b))
    for w, (g, b) in TENPCT_NOUNS.items(): inv.append((w, "Nomen10%-"+g, b))
    for w, kb in REGULAR_NOUNS.items():
        k, b = kb.split(" ", 1);           inv.append((w, "Nomen-"+k, b))
    for w, (g, b, _) in COMPOUND_NOUNS.items(): inv.append((w, "Nomen-Komp-"+g, b))
    for w, b in REGULAR_VERB_ROOTS.items(): inv.append((w+"-", "Verbwurzel", b))
    for w, b in MODAL_ROOTS.items():        inv.append((w+"-", "Modalwurzel", b))
    for w, d in IRREGULAR_VERBS.items():    inv.append((w+"-", "Verbwurzel-irr", d["bedeutung"]))
    for w, b in ADJECTIVES.items():         inv.append((w, "Adjektiv", b))
    for w, b in W_WORDS.items():            inv.append((w, "Fragewort", b))
    for w, g in W_ADJ.items():              inv.append((w, "Fragewort-adj", "welch- "+g))
    for w, b in DEMONSTRATIVES.items():     inv.append((w, "Demonstrativ", b))
    for w, b in INDEFINITES.items():        inv.append((w, "Indefinit", b))
    for w in REFLEXIVE:                     inv.append((w, "Reflexiv", "sich"))
    for w in RELATIVE:                      inv.append((w, "Relativ", "der/die/das"))
    for w in PREPOSITIONS:                  inv.append((w, "Präposition", ""))
    for w, b in CONJ_COORD.items():         inv.append((w, "Konj-koord", b))
    for w, b in CONJ_SUB.items():           inv.append((w, "Konj-sub", b))
    for w, b in NUMBERS.items():            inv.append((w, "Zahl", str(b)))
    for w, b in NUMBER_COMPOUNDS.items():   inv.append((w, "Zahl-Komp", str(b)))
    for w, b in PARTICLES.items():          inv.append((w, "Partikel/Adverb", b))
    for w in PRONOUNS:                      inv.append((w, "Pronomenform", PRONOUNS[w][0]))
    for w in ARTICLES:                      inv.append((w, "Artikelform", str(ARTICLES[w][:3])))
    return inv
