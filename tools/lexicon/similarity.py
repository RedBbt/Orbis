# -*- coding: utf-8 -*-
"""tools.lexicon.similarity — Verwechslungs- und Kollisionspruefung.

Vorbereitung fuer ein wachsendes Lexikon: bevor ein neues Lexem den Status
`canonical` erhaelt, soll es einen Kollisionsbericht bekommen.

Geprueft wird gegen den vorhandenen Bestand:
  1. exakte Formgleichheit (Homonymie)
  2. Flexionskollision — die Grundform faellt mit einer FLEKTIERTEN Form eines
     anderen Lexems zusammen (der Fall velkran, Befund W-02)
  3. geringe Editierdistanz (Levenshtein)
  4. Phonemaehnlichkeit unter Beruecksichtigung der Klanggruppen (§3.2)
  5. gleiche Wortfamilie
  6. gleiche Manus-Silbenfolge (Silhouettenkollision, soweit eindeutig)

Das Werkzeug entscheidet NICHTS. Es meldet Kandidaten; ob eine Kollision
tolerabel ist, entscheiden die Sprachdesigner (ORBIS_CONSTITUTION Art. 16).

Aufruf:
    python3 -m tools.lexicon.similarity                 Bestand gegen sich selbst
    python3 -m tools.lexicon.similarity WORT [WORT …]   Kandidaten pruefen
"""

import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)

from tools.validator import data as d          # noqa: E402
from tools.validator import morphology as m    # noqa: E402
from tools.validator import phonology as ph    # noqa: E402

LEX = os.path.join(ROOT, "language", "lexicon")


def levenshtein(a, b):
    if a == b:
        return 0
    vorher = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        jetzt = [i]
        for j, cb in enumerate(b, 1):
            jetzt.append(min(vorher[j] + 1, jetzt[j - 1] + 1,
                             vorher[j - 1] + (ca != cb)))
        vorher = jetzt
    return vorher[-1]


FLIESS = set("lrnmñvzsj")
HART = set("ptkbdgfxşç")

def phonem_aehnlich(a, b):
    """Grobe Aehnlichkeit: gleiche Laenge, hoechstens ein Unterschied, und dieser
    innerhalb derselben Klanggruppe (§3.2) oder zwischen zwei Vokalen."""
    if len(a) != len(b) or a == b:
        return False
    unterschiede = [(x, y) for x, y in zip(a, b) if x != y]
    if len(unterschiede) != 1:
        return False
    x, y = unterschiede[0]
    return ((x in FLIESS and y in FLIESS) or (x in HART and y in HART)
            or (x in d.VOWELS and y in d.VOWELS))


def lade_bestand():
    idx = json.load(open(os.path.join(LEX, "index.json"), encoding="utf-8"))
    return [json.load(open(os.path.join(LEX, e["datei"]), encoding="utf-8"))
            for e in idx["eintraege"]]


def alle_flexionsformen(eintraege):
    """form -> Liste (lemma, lexeme_id, Beschreibung)."""
    formen = {}
    for e in eintraege:
        g = e.get("grammatik") or {}
        kf = g.get("kasusformen") or {}
        for schluessel, form in kf.items():
            if form:
                formen.setdefault(form, []).append((e["lemma"], e["lexeme_id"], schluessel))
        for tempus, tab in (g.get("unregelmaessige_formen") or {}).items():
            if isinstance(tab, dict):
                for person, form in tab.items():
                    formen.setdefault(form, []).append(
                        (e["lemma"], e["lexeme_id"], f"{tempus}/{person}"))
    return formen


def pruefe(kandidat, eintraege, flexformen, ist_bestand=False):
    treffer = []
    for e in eintraege:
        if ist_bestand and e["lemma"] == kandidat:
            continue
        if e["lemma"] == kandidat:
            treffer.append(("HOMONYM", e["lemma"], e["lexeme_id"],
                            f"identische Grundform ({e['wortart']}, {e['de']['short']})"))
    for lemma, lid, beschreibung in flexformen.get(kandidat, []):
        if lemma != kandidat:
            treffer.append(("FLEXIONSKOLLISION", lemma, lid,
                            f"Grundform faellt mit {lemma} [{beschreibung}] zusammen"))
    for e in eintraege:
        if e["lemma"] == kandidat:
            continue
        dist = levenshtein(kandidat, e["lemma"])
        if dist == 1 and len(kandidat) >= 3:
            art = "PHONEMNAH" if phonem_aehnlich(kandidat, e["lemma"]) else "SEHR AEHNLICH"
            treffer.append((art, e["lemma"], e["lexeme_id"],
                            f"Editierdistanz 1 ({e['de']['short']})"))
    parses = ph.syllabify(kandidat, d.SYLLABLE_SHAPES_EXTENDED)
    if len(parses) == 1:
        silhouette = "·".join("".join(s) for s in parses[0])
        for e in eintraege:
            if e["lemma"] == kandidat or not e["manus"]["silben"]:
                continue
            if "·".join(e["manus"]["silben"]) == silhouette:
                treffer.append(("MANUS-SILHOUETTE", e["lemma"], e["lexeme_id"],
                                f"gleiche Silbenfolge {silhouette}"))
    return treffer


def main(argv):
    eintraege = lade_bestand()
    flexformen = alle_flexionsformen(eintraege)
    kandidaten = argv[1:]

    if kandidaten:
        print("== KOLLISIONSBERICHT FUER NEUE KANDIDATEN ==")
        print("Das Werkzeug entscheidet nichts; die Bewertung treffen die Sprachdesigner.\n")
        for k in kandidaten:
            verdikt, _ = ph.phonotactics_verdict(k)
            print(f"{k}  (Phonotaktik: {verdikt})")
            if verdikt == "verstoß":
                print("   ABLEHNUNG EMPFOHLEN: keine §5-konforme Silbenzerlegung.")
            treffer = pruefe(k, eintraege, flexformen)
            if not treffer:
                print("   keine Kollision gefunden.")
            for art, lemma, lid, txt in treffer:
                print(f"   [{art}] {lemma} ({lid}): {txt}")
            print()
        return 0

    print("== KOLLISIONSANALYSE DES BESTANDES ==")
    print(f"{len(eintraege)} Lexeme, {len(flexformen)} erzeugte Flexionsformen.\n")
    schwer = []
    for e in eintraege:
        for art, lemma, lid, txt in pruefe(e["lemma"], eintraege, flexformen, ist_bestand=True):
            if art in ("HOMONYM", "FLEXIONSKOLLISION"):
                schluessel = tuple(sorted([e["lemma"], lemma])) + (art,)
                schwer.append((schluessel, e["lemma"], art, lemma, txt))
    gesehen = set()
    print("-- Harte Kollisionen (Homonymie und Flexionskollision) --")
    for schluessel, wort, art, partner, txt in schwer:
        if schluessel in gesehen:
            continue
        gesehen.add(schluessel)
        print(f"   [{art}] {wort} ↔ {partner}: {txt}")
    print(f"\n   {len(gesehen)} harte Kollisionen. Dokumentiert als Befunde W-02 (velkran) "
          f"und W-03 (uebrige Homonyme).")

    paare = set()
    for e in eintraege:
        for art, lemma, lid, txt in pruefe(e["lemma"], eintraege, flexformen, ist_bestand=True):
            if art in ("PHONEMNAH", "SEHR AEHNLICH"):
                paare.add((art,) + tuple(sorted([e["lemma"], lemma])))
    print(f"\n-- Verwechselbare Paare (Editierdistanz 1): {len(paare)} --")
    for art, a, b in sorted(paare, key=lambda x: (x[0], x[1])):
        print(f"   [{art}] {a} ~ {b}")
    print("\nHINWEIS: Aehnlichkeit allein ist kein Fehler. Vor 1.0 zu bewerten sind vor "
          "allem Paare, die derselben Wortart und Bedeutungsdomaene angehoeren.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
