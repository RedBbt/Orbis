# -*- coding: utf-8 -*-
"""Lexikon-Integritaet und Schemapflichten."""
import json, os, glob, pytest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LEX = os.path.join(ROOT, "language", "lexicon")


@pytest.fixture(scope="module")
def eintraege():
    idx = json.load(open(os.path.join(LEX, "index.json"), encoding="utf-8"))
    return [json.load(open(os.path.join(LEX, e["datei"]), encoding="utf-8"))
            for e in idx["eintraege"]]


def test_281_grundformen(eintraege):
    """Baseline-Kennzahl der Migration."""
    assert len(eintraege) == 281


def test_ids_eindeutig(eintraege):
    ids = [e["lexeme_id"] for e in eintraege]
    assert len(set(ids)) == len(ids)


def test_jedes_lexem_hat_deutsche_bedeutung(eintraege):
    for e in eintraege:
        assert e["de"]["short"], e["lemma"]
        assert e["de"]["definition"], e["lemma"]


def test_canonical_hat_englische_glosse(eintraege):
    ohne = [e["lemma"] for e in eintraege
            if e["status"] == "canonical" and not e["en"]["short"]]
    assert ohne == [], ohne


def test_konzeptverweise_gueltig(eintraege):
    con = {c["concept_id"] for c in json.load(
        open(os.path.join(LEX, "concepts", "concepts.json"), encoding="utf-8"))["concepts"]}
    for e in eintraege:
        for cid in e["semantik"]["concept_ids"]:
            assert cid in con, f"{e['lemma']} -> {cid}"


def test_relationen_zeigen_auf_existierende_lexeme(eintraege):
    ids = {e["lexeme_id"] for e in eintraege}
    for e in eintraege:
        for rel in e["semantik"]["relationen"]:
            if rel["ziel"].startswith("ORB-LEX-"):
                assert rel["ziel"] in ids, f"{e['lemma']} -> {rel['ziel']}"


def test_77_manus_ambiguitaeten(eintraege):
    """L-09-Kennzahl darf sich durch Infrastrukturarbeit nicht aendern."""
    assert sum(1 for e in eintraege if e["manus"]["ambiguitaet"]) == 77


def test_antonyme_sind_symmetrisch(eintraege):
    by_id = {e["lexeme_id"]: e for e in eintraege}
    for e in eintraege:
        for rel in e["semantik"]["relationen"]:
            if rel["typ"] != "antonym":
                continue
            ziel = by_id[rel["ziel"]]
            rueck = [r for r in ziel["semantik"]["relationen"]
                     if r["typ"] == "antonym" and r["ziel"] == e["lexeme_id"]]
            assert rueck, f"{e['lemma']} -> {ziel['lemma']} ohne Rueckrelation"


def test_dateien_und_index_stimmen_ueberein():
    idx = json.load(open(os.path.join(LEX, "index.json"), encoding="utf-8"))
    dateien = {os.path.basename(p) for p in glob.glob(os.path.join(LEX, "entries", "*.json"))}
    referenziert = {os.path.basename(e["datei"]) for e in idx["eintraege"]}
    assert dateien == referenziert
