# -*- coding: utf-8 -*-
"""Prueft die handgeschriebene Dokumentation gegen die Sprachdaten.

Die Kapitel unter docs/de und docs/en beschreiben die Grammatik. Sie duerfen
keine Formen enthalten, die den Regeln widersprechen, und keine offene Frage
stillschweigend schliessen.

Konventionen der Dokumentation, die dieser Test kennt:
  †  markiert ein absichtliches Gegenbeispiel (ungrammatisch)
  \\* markiert eine hypothetische oder ungrammatische Form
Beides wird von der Pruefung ausgenommen.
"""
import re, os, glob, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)

from tools.validator import syntax as sy, data as d, phonology as ph   # noqa: E402

ORBIS_ZEICHEN = set("ptkbdgçfsşxvzjmnñlraeiou")
KAPITEL = sorted(glob.glob(os.path.join(ROOT, "docs", "de", "*.md"))
                 + glob.glob(os.path.join(ROOT, "docs", "en", "*.md")))

# Belegte Formen, die selbst Gegenstand eines Befunds sind
BEFUND_FORMEN = {"kellan", "killa", "dolla", "kella", "telnxelmmern"}


def _ist_orbis_satz(s):
    kern = re.sub(r"[ ,.?!]", "", s.lower())
    return len(kern) > 6 and " " in s.strip() and all(c in ORBIS_ZEICHEN for c in kern)


def _beispielsaetze():
    """(satz, datei) fuer alle als korrekt praesentierten Orbis-Saetze."""
    raus = []
    for f in KAPITEL:
        for zeile in open(f, encoding="utf-8"):
            if "†" in zeile or "\\*" in zeile:      # Gegenbeispiel oder hypothetisch
                continue
            for m in re.finditer(r"\*\*([A-ZXVŞ][^*\n]{8,90}[.?!])\*\*"
                                 r"|\*([A-ZXVŞ][^*\n]{8,90}[.?!])\*", zeile):
                s = (m.group(1) or m.group(2)).strip()
                if _ist_orbis_satz(s):
                    raus.append((s, os.path.basename(f)))
    return raus


def test_dokumentation_existiert_zweisprachig():
    de = glob.glob(os.path.join(ROOT, "docs", "de", "*.md"))
    en = glob.glob(os.path.join(ROOT, "docs", "en", "*.md"))
    assert len(de) >= 18, f"nur {len(de)} deutsche Kapitel"
    assert len(en) >= 10, f"nur {len(en)} englische Kapitel"


def test_beispielsaetze_sind_regelkonform():
    """Jeder als korrekt gezeigte Orbis-Satz muss die Automatik bestehen."""
    fehler = []
    for satz, datei in _beispielsaetze():
        r = sy.check_sentence(satz)
        unbekannt = [u for u in r["unbekannt"] if u not in d.DERIVED_ADJ_VI]
        if unbekannt:
            continue          # deutsche/englische Saetze aus Orbis-Buchstaben — kein Befund
        if r["kongruenz"]:
            fehler.append(f"{datei}: {satz} — {r['kongruenz']}")
        if r["präp_kasus"]:
            fehler.append(f"{datei}: {satz} — {r['präp_kasus']}")
        for tok, gem in r["geminaten"]:
            if tok not in BEFUND_FORMEN:
                fehler.append(f"{datei}: {satz} — Geminate in {tok}")
    assert not fehler, "\n".join(fehler)


def test_keine_umschrift_von_sonderzeichen():
    """ş, ñ und ç duerfen in SPRACHLICHEN Angaben nicht durch sh/nn/ch ersetzt sein
    (TRANSLATION_POLICY §7). Ausgenommen ist die dokumentierte ASCII-Konvention fuer
    DATEINAMEN (veiş -> veish.json), die keine Sprachaussage ist."""
    fehler = []
    for f in KAPITEL:
        for nr, zeile in enumerate(open(f, encoding="utf-8"), 1):
            if re.search(r"[Dd]ateiname|\.json|ASCII", zeile):
                continue      # Dateinamenkonvention, keine Lautangabe
            if re.search(r"\bf,? s,? sh\b|Strichst[äa]rke.*\bsh\b", zeile):
                fehler.append(f"{os.path.basename(f)}:{nr}: 'sh' statt 'ş' in einer Lautangabe")
    assert not fehler, "\n".join(fehler)


def test_offene_befunde_werden_in_der_doku_benannt():
    """Kein Kapitel darf eine offene Frage als geloest darstellen."""
    text = "".join(open(f, encoding="utf-8").read() for f in KAPITEL)
    for befund in ("L-01", "L-02", "L-03", "L-04", "L-05", "L-07",
                   "L-08", "L-09", "L-10", "K-05"):
        assert befund in text, f"Befund {befund} wird in keinem Kapitel erwaehnt"


def test_experimentelles_bleibt_gekennzeichnet():
    """Wortspuren und Morphem-Ebene duerfen nur mit Warnung erscheinen."""
    for f in KAPITEL:
        t = open(f, encoding="utf-8").read()
        low = t.lower()
        if "wortspur" in low or "word trace" in low:
            assert ("experimentell" in low or "experimental" in low), \
                f"{os.path.basename(f)} nennt Wortspuren ohne EXPERIMENTAL-Kennzeichnung"
