# -*- coding: utf-8 -*-
"""Migrationsregression: die Werkzeugausgabe muss der eingefrorenen Baseline gleichen."""
import os, subprocess, sys, pytest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE = os.path.join(ROOT, "reports", "baseline")


def _lauf(*args):
    r = subprocess.run([sys.executable, "-m", "tools.validator", *args],
                       cwd=ROOT, capture_output=True, text=True)
    return r.stdout + r.stderr


@pytest.mark.parametrize("modus", ["lexicon", "examples", "manus", "tables"])
def test_ausgabe_identisch_zur_baseline(modus):
    erwartet = open(os.path.join(BASE, f"validator-{modus}.txt"), encoding="utf-8").read()
    assert _lauf("--" + modus) == erwartet


def test_korpuslauf_identisch():
    erwartet = open(os.path.join(BASE, "validator-corpus.txt"), encoding="utf-8").read()
    assert _lauf("--corpus", "Orbis-Testkorpus-0_1.md") == erwartet


def test_strict_bleibt_gruen():
    r = subprocess.run([sys.executable, "-m", "tools.validator", "--strict"],
                       cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout


def test_schemapruefung_bleibt_gruen():
    r = subprocess.run([sys.executable, "-m", "tools.validator", "--schema"],
                       cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout


def test_sim_l09_deckt_vier_strategien_ab():
    """Bewusste Werkzeugerweiterung: A-D statt urspruenglich zwei Varianten.
    Die alte Zweistrategien-Ausgabe ist unter
    reports/baseline/validator-sim-l09-2strategien-vor-erweiterung.txt archiviert."""
    out = _lauf("--sim-l09")
    for name in ("Strategie A", "Strategie B", "Strategie C", "Strategie D"):
        assert name in out
    assert "KEINE SPRACHREGEL" in out
    assert "77 der 281 Grundformen" in out
