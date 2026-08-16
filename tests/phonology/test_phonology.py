# -*- coding: utf-8 -*-
"""Phonologie-Regression gegen Grammatik 0.9.3 §2 und §5."""
import pytest
from tools.validator import data as d
from tools.validator import phonology as ph


def test_19_konsonanten():
    assert len(d.CONSONANTS) == 19


def test_5_vokale():
    assert d.VOWELS == set("aeiou")


def test_keine_fremdlaute():
    for verboten in "hwyq":
        assert verboten not in d.CONSONANTS and verboten not in d.VOWELS


def test_25_anfangsgruppen():
    assert len(d.ONSETS2) == 25
    assert d.ONSETS2 <= {a + b for a in d.CONSONANTS for b in d.CONSONANTS}


def test_diphthonge_belegt():
    assert set(d.DIPHTHONGS_BELEGT) == {"ai", "au", "ei", "ui", "eu"}
    assert "oi" in d.DIPHTHONGS          # regulaer, unbelegt
    assert "ou" not in d.DIPHTHONGS      # offen, darf nicht verwendet werden


@pytest.mark.parametrize("paar,erwartet", [
    ("rn", True), ("lk", True), ("ks", True), ("şn", True), ("sn", True),
    ("st", True), ("sk", True), ("kt", False), ("pf", False), ("gd", False),
])
def test_coda_regel(paar, erwartet):
    assert ph.coda_pair_ok(paar) is erwartet


@pytest.mark.parametrize("wort", ["valru", "sarla", "milne", "kirva", "vresto", "narku"])
def test_lexikon_ist_51_konform(wort):
    assert ph.phonotactics_verdict(wort)[0] == "ok"


@pytest.mark.parametrize("wort", ["aul", "eird", "ain", "granz", "trelm", "vresn", "skirm"])
def test_k01_woerter_bleiben_sichtbar(wort):
    """K-01: Diese Formen brauchen VK/VKK bzw. KKVKK — der Befund darf nicht verschwinden."""
    assert ph.phonotactics_verdict(wort)[0].startswith("nur-")


def test_unsinn_wird_erkannt():
    assert ph.phonotactics_verdict("zzz")[0] == "verstoß"
    assert ph.check_phonemes("blorgh") == ["h"]


def test_kein_vokal_in_coda():
    for parse in ph.syllabify("kaun", d.SYLLABLE_SHAPES_EXTENDED):
        for _onset, _nuk, coda in parse:
            assert all(c in d.CONSONANTS for c in coda)
