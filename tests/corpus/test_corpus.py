# -*- coding: utf-8 -*-
"""Korpus-Regression: die Kennzahlen des Testkorpus 0.1 sind Baseline."""
import json, os, pytest
from tools.validator import corpus as c
from tools.validator import data as d

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
KORPUS = os.path.join(ROOT, "language", "corpus", "tests", "testkorpus-0_1.json")


@pytest.fixture(scope="module")
def korpus():
    with open(KORPUS, encoding="utf-8") as f:
        return json.load(f)


def test_genau_150_saetze(korpus):
    assert korpus["anzahl"] == 150
    assert len(korpus["saetze"]) == 150


def test_kennzahlen_unveraendert(korpus):
    """150 / 130 OK / 14 Luecke / 3 Konflikt / 2 Unklarheit / 1 Testproblem."""
    assert korpus["nach_status"] == {
        "canonical": 130, "open": 14, "conflict": 3, "unclear": 2, "testproblem": 1}
    assert korpus["stabilitaetsquote_prozent"] == 86.7


def test_ids_eindeutig_und_lueckenlos(korpus):
    ids = [s["id"] for s in korpus["saetze"]]
    assert len(set(ids)) == 150
    nummern = sorted(s["legacy_nummer"] for s in korpus["saetze"])
    assert nummern == list(range(1, 151))


def test_jeder_satz_hat_deutsch_und_englisch(korpus):
    for s in korpus["saetze"]:
        assert s["de"], s["id"]
        assert s["en"], s["id"]


def test_offene_saetze_ohne_orbis_form(korpus):
    """Saetze mit Befund duerfen keine erfundene Orbis-Form tragen."""
    for s in korpus["saetze"]:
        if s["status"] != "canonical":
            assert s["orbis"] is None, s["id"]
            assert s["qualitaet"]["befunde"], s["id"]


def test_kanonische_saetze_bestehen_die_automatik(korpus):
    for s in korpus["saetze"]:
        if s["status"] != "canonical":
            continue
        r = c.check_sentence(s["orbis"])
        unbekannt = [u for u in r["unbekannt"] if u not in d.DERIVED_ADJ_VI]
        assert not unbekannt, f"{s['id']}: unbekannte Formen {unbekannt}"
        assert not r["kongruenz"], f"{s['id']}: {r['kongruenz']}"
        assert not r["präp_kasus"], f"{s['id']}: {r['präp_kasus']}"


def test_grammatikbeispiele_bleiben_erkennbar():
    """Die 71 Belege der Grammatik duerfen keine unbekannten Formen enthalten."""
    for ref, satz, probleme in c.run_examples():
        harte = [p for p in probleme if "unbekannte Formen" in p]
        assert not harte, f"{ref}: {harte}"
