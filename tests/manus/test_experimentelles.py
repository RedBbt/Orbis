# -*- coding: utf-8 -*-
"""Sichert ab, dass Experimentelles nicht als kanonisch erscheint (ORBIS_CONSTITUTION Art. 20)."""
import json, os, glob

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_wortspuren_sind_als_experimentell_markiert():
    p = os.path.join(ROOT, "script", "traces", "spec.experimental.json")
    d = json.load(open(p, encoding="utf-8"))
    assert d["status"] == "EXPERIMENTAL"
    assert d["kanonisch"] is False
    assert "NICHT KANONISCH" in d["warnung"]


def test_wortspuren_tauchen_nicht_in_sprachdaten_auf():
    """Kein Lexem, keine Regel und kein Satz darf eine Wortspur als geltend fuehren."""
    verboten = ("wortspur", "trace-exp", "evidenzzeichen")
    for p in glob.glob(os.path.join(ROOT, "language", "**", "*.json"), recursive=True):
        text = open(p, encoding="utf-8").read().lower()
        for w in verboten:
            assert w not in text, f"{os.path.relpath(p, ROOT)} nennt '{w}'"


def test_manus_spec_nennt_19_konsonanten_plus_traeger():
    p = os.path.join(ROOT, "script", "manus", "spec", "manus-0_x.json")
    d = json.load(open(p, encoding="utf-8"))
    kf = d["kernformen"]
    assert kf["anzahl"] == 20
    assert kf["zusammensetzung"] == {"konsonanten": 19, "vokaltraeger": 1}
    assert kf["vokaltraeger"]["ist_konsonant"] is False
    assert "U-10" in d["offene_befunde"]


def test_manus_strichstaerke_bleibt_offen():
    """L-10 darf nicht stillschweigend geschlossen werden."""
    d = json.load(open(os.path.join(ROOT, "script", "manus", "spec", "manus-0_x.json"),
                       encoding="utf-8"))
    st = d["strichstaerke"]
    assert st["status"] == "open" and st["befund"] == "L-10"
    assert set(st["undefiniert"]) == set("f s ş x v z j ç".split())


def test_ou_bleibt_ungeschrieben():
    """§2.3 fuehrt ou als offen — er darf nirgends schreibbar erscheinen."""
    d = json.load(open(os.path.join(ROOT, "script", "manus", "spec", "manus-0_x.json"),
                       encoding="utf-8"))
    assert "ou" not in d["vokalzeichen"]["schreibbare_diphthonge"]


def test_keyboard_nennt_l09_als_blockade():
    p = os.path.join(ROOT, "keyboard", "README.md")
    text = open(p, encoding="utf-8").read()
    assert "L-09" in text and "blockiert" in text.lower() or "Blockade" in text
