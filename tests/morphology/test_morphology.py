# -*- coding: utf-8 -*-
"""Morphologie-Regression: §7-§16."""
import pytest
from tools.validator import data as d
from tools.validator import morphology as m
from tools.validator import phonology as ph


def test_45_endungen_vollstaendig():
    assert len(d.ALL_45_ENDINGS) == 45
    assert len(set(d.ALL_45_ENDINGS)) == 45


def test_genus_folgt_endung():
    for endung in d.ALL_45_ENDINGS:
        assert d.GENDER_OF_CONS[endung[0]] in ("M", "F", "N")


def test_360er_matrix_phonotaktisch_sauber():
    """45 Endungen x 8 Formen; alle muessen §5-konform sein."""
    from tools.validator.reports import table_45
    n = 0
    for zeile in table_45():
        for form in zeile[2:]:
            assert ph.phonotactics_verdict(form)[0] == "ok", form
            n += 1
    assert n == 360


@pytest.mark.parametrize("kasus,erwartet", [
    ("nom", "valru"), ("akk", "valrun"), ("dat", "valruş"), ("gen", "valrus")])
def test_regulaere_deklination_singular(kasus, erwartet):
    assert m.decline_regular_noun("valru", kasus, "sg") == erwartet


def test_regulaerer_plural_mit_echovokal():
    assert m.decline_regular_noun("valru", "nom", "pl") == "valruñ"
    assert m.decline_regular_noun("valru", "akk", "pl") == "valruñun"
    assert m.decline_regular_noun("sarla", "akk", "pl") == "sarlañan"
    assert m.decline_regular_noun("milne", "dat", "pl") == "milneñeş"


def test_kernwortdeklination():
    """§10.3: Bindevokal immer -e-, Plural -ei; aulan/eirdas sind falsch."""
    assert m.decline_core_noun("aul", "nom", "sg") == "aul"
    assert m.decline_core_noun("aul", "akk", "sg") == "aulen"
    assert m.decline_core_noun("şirn", "dat", "pl") == "şirneiş"
    assert m.decline_core_noun("aul", "akk", "sg") != "aulan"


def test_alle_15_kernwoerter():
    assert len(d.CORE_NOUNS) == 15


def test_10prozent_plural_bleibt_offen():
    """L-07 darf nicht stillschweigend geschlossen werden."""
    assert m.decline_tenpct_noun("velkran", "nom", "pl") is None


def test_artikel_kein_unbestimmter_plural():
    """§11.2"""
    unbestimmt_pl = [f for f, (best, _g, _k, num) in d.ARTICLES.items()
                     if best == "unbestimmt" and num == "pl"]
    assert unbestimmt_pl == []


def test_artikel_zeigt_nur_genus():
    """§11.3: immer A-Reihe r/l/n."""
    for form, (_best, genus, _kasus, _num) in d.ARTICLES.items():
        assert form[1] == {"M": "r", "F": "l", "N": "n"}[genus]


def test_regelmaessige_konjugation_6x3():
    formen = {(t, p): m.conj("milk", t, p) for t in d.TENSE_VOWELS for p in d.PERSON_ENDINGS}
    assert len(formen) == 18
    assert formen[("präs", "1sg")] == "milkam"
    assert formen[("vgh", "3sg")] == "milkot"
    assert formen[("fut", "2pl")] == "milkaişen"


def test_acht_unregelmaessige_verben_vollstaendig():
    assert len(d.IRREGULAR_VERBS) == 8
    for root, tab in d.IRREGULAR_VERBS.items():
        for tempus in ("präs", "vgh", "fut"):
            assert len(tab[tempus]) == 6, f"{root} {tempus}"


@pytest.mark.parametrize("root,tempus,person,erwartet", [
    ("es", "präs", "3sg", "est"), ("es", "vgh", "3sg", "vot"), ("es", "fut", "2pl", "vaişen"),
    ("nuv", "präs", "1pl", "numen"), ("vurn", "präs", "3sg", "vurt"),
    ("mel", "vgh", "1sg", "molem"), ("dalv", "vgh", "3pl", "dolveten"),
])
def test_belegte_unregelmaessige_formen(root, tempus, person, erwartet):
    assert m.conj(root, tempus, person) == erwartet


def test_fugenregel():
    """§21.4: identische Konsonanten verschmelzen."""
    assert m.fuse("mel", "la") == "mela"
    assert m.fuse("şaln", "na") == "şalna"
    assert m.fuse("girn", "la") == "girnla"     # n != l, keine Fusion


def test_adjektivkongruenz():
    assert m.adj_attributive("vlaid", "M", "nom", "sg") == "vlaidra"
    assert m.adj_attributive("vlaid", "F", "akk", "sg") == "vlaidlan"
    assert m.adj_attributive("loşn", "F", "nom", "sg") == "loşnla"
    assert m.adj_attributive("şaln", "N", "nom", "sg") == "şalna"


def test_steigerung():
    assert m.adj_predicative("vlaid", "komp") == "vlaidvi"
    assert m.adj_predicative("selv", "komp") == "selvi"      # Fuge v+v
    assert m.adj_attributive("vlaid", "M", "nom", "sg", "sup") == "vlaidvaxra"
