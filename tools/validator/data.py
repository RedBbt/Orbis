# -*- coding: utf-8 -*-
"""tools.validator.data — Sprachdaten aus language/ laden.

Dies ist die EINZIGE Stelle, an der Sprachdaten in die Werkzeuge gelangen.
Keine Regel wird hier hartkodiert; alle Werte stammen aus den JSON-Dateien
unter language/, die ihrerseits 1:1 aus Orbis-Grammatik-0.9.3.md migriert
wurden (tools/migration/extract_language_data.py).

Weicht eine Datendatei von der Grammatik ab, gilt die Grammatik — die
Abweichung ist ein Befund, keine Korrekturgrundlage (CLAUDE.md, Regel 6).
"""

import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LANG = os.path.join(ROOT, "language")


def _load(*parts):
    with open(os.path.join(LANG, *parts), encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------- Phonologie
_ph = _load("phonology", "phonemes.json")
CONSONANTS = set(_ph["konsonanten"]["alle"])
VOWELS = set(_ph["vokale"]["alle"])

_di = _load("phonology", "diphthongs.json")
DIPHTHONGS = list(_di["im_validator_aktiv"])
DIPHTHONGS_BELEGT = [d["form"] for d in _di["diphthonge"] if d["status"] == "attested"]

_sh = _load("phonology", "syllable_shapes.json")
SYLLABLE_SHAPES_STRICT = set(_sh["in_grammatik_gelistet"])
_fehlend = set(_sh["faktisch_benoetigt_aber_nicht_gelistet"])
SYLLABLE_SHAPES_VK = SYLLABLE_SHAPES_STRICT | {"VK", "VKK"}
SYLLABLE_SHAPES_KKVKK = SYLLABLE_SHAPES_STRICT | {"KKVKK"}
SYLLABLE_SHAPES_EXTENDED = SYLLABLE_SHAPES_STRICT | _fehlend

ONSETS2 = set(_load("phonology", "onsets.json")["erlaubte_zweiergruppen"])

_cd = _load("phonology", "codas.json")["bedingungen"]
CODA_FIRST_OK = set(_cd["a_erster_laut"])
CODA_SECOND_S = _cd["b_zweiter_laut"]
CODA_PAIRS_C = set(_cd["c_feste_gruppen"])

# ---------------------------------------------------------------- Morphologie
_nc = _load("morphology", "noun_classes.json")
CLASS_CONS = _nc["klassenkonsonanten"]
THEMA_VOWELS = "".join(_nc["themavokale"])
ALL_45_ENDINGS = [e["endung"] for e in _nc["endungen"]]
GENDER_OF_CONS = {e["endung"][0]: e["genus"] for e in _nc["endungen"]}
SUBCLASS_OF_CONS = {e["endung"][0]: e["unterklasse"] for e in _nc["endungen"]}

_ca = _load("morphology", "cases.json")
CASE_MARKERS = {k["name"]: k["marker"] for k in _ca["kasus"]}
CASES = [k["name"] for k in _ca["kasus"]]

CORE_NOUNS = {w["lemma"]: (w["genus"], w["bedeutung_de"])
              for w in _load("morphology", "core_nouns.json")["woerter"]}
TENPCT_NOUNS = {w["lemma"]: (w["genus"], w["bedeutung_de"])
                for w in _load("morphology", "tenpct_nouns.json")["woerter"]}

ARTICLES = {f["form"]: (f["bestimmtheit"], f["genus"], f["kasus"], f["numerus"])
            for f in _load("morphology", "articles.json")["formen"]}

_pr = _load("morphology", "pronouns.json")
PRONOUNS = {p["form"]: (p["person"], p["kasus"]) for p in _pr["personalpronomen"]}
DEMONSTRATIVES = _pr["demonstrativa"]["formen"]
REFLEXIVE = set(_pr["reflexiv"]["formen"])
RELATIVE = set(_pr["relativ"]["formen"])
INDEFINITES = _pr["indefinita"]["formen"]

_ad = _load("morphology", "adjectives.json")
ADJECTIVES = {a["lemma"]: a["bedeutung_de"] for a in _ad["grundadjektive"]}
COMPARISON_INFIXES = {"komp": _ad["steigerung"]["komparativ_infix"],
                      "sup": _ad["steigerung"]["superlativ_infix"]}
ADJ_GENDER_CONS = {"M": "r", "F": "l", "N": "n"}

_vb = _load("morphology", "verbs.json")
PERSON_ENDINGS = _vb["personendungen"]
TENSE_VOWELS = _vb["tempusvokale"]
VERB_PREFIXES = list(_vb["vorsilben"])
REGULAR_VERB_ROOTS = {r["wurzel"]: r["bedeutung_de"] for r in _vb["regulaere_wurzeln"]}

MODAL_ROOTS = {r["wurzel"]: r["bedeutung_de"]
               for r in _load("morphology", "modals.json")["wurzeln"]}

_irr = _load("morphology", "irregular_verbs.json")["verben"]
IRREGULAR_VERBS = {root: {"inf": d["infinitiv"], "bedeutung": d["bedeutung_de"],
                          "präs": d["praesens"], "vgh": d["vergangenheit"],
                          "fut": d["zukunft"]}
                   for root, d in _irr.items()}

_nu = _load("morphology", "numbers.json")
NUMBERS = {z["lemma"]: z["wert"] for z in _nu["kardinalzahlen"]}
NUMBER_COMPOUNDS = {z["lemma"]: z["wert"] for z in _nu["komposita_belegt"]}
ORDINAL_INFIX = _nu["ordinalzahl_infix"]

DERIVED_ADJ_VI = {f["form"]: f["erlaeuterung_de"]
                  for f in _load("morphology", "derived_vi.json")["formen"]}

# ---------------------------------------------------------------- Syntax
PREPOSITIONS = {p["lemma"]: set(p["kasus"])
                for p in _load("syntax", "prepositions.json")["praepositionen"]}
_cj = _load("syntax", "conjunctions.json")
CONJ_COORD = {c["lemma"]: c["bedeutung_de"] for c in _cj["nebenordnend"]}
CONJ_SUB = {c["lemma"]: c["bedeutung_de"] for c in _cj["unterordnend"]}

# ---------------------------------------------------------------- Lexikon
_lex_extra = json.load(open(os.path.join(LANG, "lexicon", "index.json"), encoding="utf-8"))

def _regular_nouns():
    """Regulaere Nomen mit Klasse und Glosse aus den Lexikoneintraegen."""
    out = {}
    for e in _lex_extra["eintraege"]:
        if e["wortart"] != "nomen":
            continue
        entry = json.load(open(os.path.join(LANG, "lexicon", e["datei"]), encoding="utf-8"))
        if entry["grammatische_kategorie"] != "regulaer":
            continue
        out[entry["lemma"]] = f'{entry["grammatik"]["klasse"]} {entry["de"]["short"]}'
    return out

def _compound_nouns():
    out = {}
    for e in _lex_extra["eintraege"]:
        if e["wortart"] != "nomen":
            continue
        entry = json.load(open(os.path.join(LANG, "lexicon", e["datei"]), encoding="utf-8"))
        if entry["grammatische_kategorie"] != "kompositum":
            continue
        out[entry["lemma"]] = (entry["grammatik"]["genus"], entry["de"]["short"],
                               entry["grammatik"]["kompositionshinweis"])
    return out

REGULAR_NOUNS = _regular_nouns()
COMPOUND_NOUNS = _compound_nouns()

W_WORDS = {}
W_ADJ = {}
for _e in _lex_extra["eintraege"]:
    if _e["wortart"] != "pronomen":
        continue
    _entry = json.load(open(os.path.join(LANG, "lexicon", _e["datei"]), encoding="utf-8"))
    if _entry["grammatische_kategorie"] == "fragewort":
        W_WORDS[_entry["lemma"]] = _entry["de"]["short"]
    elif _entry["grammatische_kategorie"] == "fragewort-adjektivisch":
        W_ADJ[_entry["lemma"]] = _entry["de"]["short"].split("(")[1].rstrip(")")

PARTICLES = {}
for _e in _lex_extra["eintraege"]:
    if _e["wortart"] != "partikel":
        continue
    _entry = json.load(open(os.path.join(LANG, "lexicon", _e["datei"]), encoding="utf-8"))
    _gloss = _entry["de"]["short"]
    if "W-03" in _entry["qualitaet"]["offene_befunde"]:
        _gloss += (" (homonym: vran = unbest. Artikel M Akk)" if _entry["lemma"] == "vran" else "")
    PARTICLES[_entry["lemma"]] = _gloss

# ---------------------------------------------------------------- Korpus
GRAMMAR_EXAMPLES = [(s["fundstelle"], s["orbis"])
                    for s in _load("corpus", "examples", "grammatik-beispiele.json")["saetze"]]

# ---------------------------------------------------------------- Befunde
FINDINGS = {f["id"]: f for f in _load("findings", "findings.json")["findings"]}

# Konsistenzzusicherungen gegen die Grammatik (schlagen bei Datenschaden fehl)
assert len(CONSONANTS) == 19, "Grammatik §2.1: 19 Konsonanten"
assert len(VOWELS) == 5, "Grammatik §2.2: 5 Vokale"
assert len(ONSETS2) == 25, "Grammatik §5.2: 25 Anfangsgruppen"
assert len(ALL_45_ENDINGS) == 45, "Grammatik §7: 45 Endungen"
assert len(CORE_NOUNS) == 15, "Grammatik §10.2: 15 Kernwoerter"
assert len(IRREGULAR_VERBS) == 8, "Grammatik §15.2: 8 unregelmaessige Verben"
