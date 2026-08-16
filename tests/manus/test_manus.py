# -*- coding: utf-8 -*-
"""Manus-Zerlegung (§26) und L-09-Simulationen."""
import pytest
from tools.validator import manus as ma
from tools.validator import data as d


def test_281_grundformen_geprueft():
    assert len(ma.manus_report_data()) == 281


def test_77_mehrdeutig():
    daten = ma.manus_report_data()
    amb = [w for w, _cat, _p, verd in daten if "AMBIGUITÄT" in verd]
    assert len(amb) == 77


@pytest.mark.parametrize("wort", ["kra", "mel", "milk", "breun", "kaun", "virn", "moks"])
def test_tastaturbeispiele_eindeutig(wort):
    strict = ma.syllabify(wort, d.SYLLABLE_SHAPES_STRICT)
    ext = ma.syllabify(wort, d.SYLLABLE_SHAPES_EXTENDED)
    assert len(strict or ext) == 1


def test_mela_ist_mehrdeutig():
    """Das Kernbeispiel von L-09 muss sichtbar bleiben."""
    assert len(ma.syllabify("mela", d.SYLLABLE_SHAPES_STRICT)) == 2


def test_simulation_ist_keine_regel():
    """pref_syllabify liefert eine Kandidatenzerlegung, aendert aber keine Daten."""
    parse, fehler = ma.pref_syllabify("mela", "max")
    assert fehler is None and parse is not None
    assert len(ma.syllabify("mela", d.SYLLABLE_SHAPES_STRICT)) == 2   # unveraendert


def test_variante_a_loest_alle_ambiguitaeten():
    daten = ma.manus_report_data()
    ungeloest = []
    for w, _cat, _p, verd in daten:
        if "AMBIGUITÄT" not in verd:
            continue
        parse, fehler = ma.pref_syllabify(w, "max")
        if fehler or parse is None:
            ungeloest.append(w)
    assert ungeloest == []
