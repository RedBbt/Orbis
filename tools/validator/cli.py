# -*- coding: utf-8 -*-
"""tools.validator.cli — Kommandozeile des Orbis-Validators.

Das Werkzeug ist ein HILFSMITTEL. Pruefungen, die semantische oder syntaktische
Interpretation verlangen, werden als MANUELLE_PRUEFUNG gekennzeichnet und nicht
algorithmisch entschieden.

Aufrufe:
  --lexicon           Wortschatz pruefen (§24)
  --examples          Beispielsaetze der Grammatik pruefen
  --corpus DATEI      "Orbis:"-Zeilen einer Korpusdatei pruefen
  --tables            45-Endungen-Matrix (45 x 8) + Verbparadigmen
  --manus             Manus-Silbenzerlegung des Wortschatzes
  --json DATEI        Korpuspruefung als JSON ausgeben
  --all               Gesamtlauf (Lexikon, Beispiele, Manus)
  --strict            Befunde gegen orbis_baseline.json; Exit 1 bei NEUEN Befunden
  --update-baseline   Baseline neu schreiben
  --sim-l09           Silbifizierungs-Simulation (Entscheidungswerkzeug, KEINE Regel)
  --schema            Schemapruefung der Sprachdaten (IDs, Pflichtfelder, Relationen)
  --ids               nur ID-Eindeutigkeit und Referenzen pruefen
  --translations      Uebersetzungsfelder pruefen (TRANSLATION_POLICY)
  --relations         semantische Relationen auf gueltige Ziele pruefen
"""

import sys, json

from .data import GRAMMAR_EXAMPLES, IRREGULAR_VERBS
from .lexicon import run_lexicon
from .corpus import run_examples, run_corpus
from .manus import manus_report_data, fmt_parse
from .reports import (TESTSTEM, table_45, table_verb, run_strict, run_sim_l09)


def main(argv):
    args = argv[1:]
    if not args:
        print(__doc__)
        return 0

    if "--lexicon" in args or "--all" in args:
        print("== LEXIKONPRÜFUNG (Prüfungen 1–6) ==")
        for kind, w, cat, msg in run_lexicon():
            print(f"[{kind}] {w} ({cat}): {msg}")
        print()

    if "--examples" in args or "--all" in args:
        print("== BEISPIELSÄTZE DER GRAMMATIK ==")
        ok = 0
        for ref, s, probs in run_examples():
            if probs:
                print(f"{ref}  {s}")
                for p in probs:
                    print(f"    -> {p}")
            else:
                ok += 1
        print(f"({ok} von {len(GRAMMAR_EXAMPLES)} Beispielen ohne Befund)")
        print()

    if "--corpus" in args:
        path = args[args.index("--corpus") + 1]
        print(f"== KORPUSPRÜFUNG {path} ==")
        ok = 0
        n = 0
        for test_no, s, probs, vk in run_corpus(path):
            n += 1
            if probs:
                print(f"Test {test_no}: {s}")
                for p in probs:
                    print(f"    -> {p}")
            else:
                ok += 1
        print(f"({ok} von {n} Orbis-Sätzen ohne automatischen Befund)")
        print("MANUELLE_PRÜFUNG: V2/Verbklammer/Endstellung, Kongruenz über Distanz, "
              "Genitiv-Stellung, Semantik — nicht algorithmisch entschieden.")
        print()

    if "--tables" in args:
        print("== 45 ENDUNGEN — [TESTFORM]-Stamm '" + TESTSTEM + "-' ==")
        print("| Klasse | Endung | Nom Sg | Akk Sg | Dat Sg | Gen Sg | Nom Pl | Akk Pl | Dat Pl | Gen Pl |")
        print("|---|---|---|---|---|---|---|---|---|---|")
        for kl, end, nom, akk, dat, gen, npl, apl, dpl, gpl in table_45():
            print(f"| {kl} | -{end} | {nom} | {akk} | {dat} | {gen} | {npl} | {apl} | {dpl} | {gpl} |")
        print()
        print("== REGELMÄSSIGES VERB milk- (6 Personen × 3 Zeiten) ==")
        for t, p, f in table_verb("milk"):
            print(f"{t:5} {p:4} {f}")
        print()
        for root in IRREGULAR_VERBS:
            print(f"== UNREGELMÄSSIG {IRREGULAR_VERBS[root]['inf']} "
                  f"({IRREGULAR_VERBS[root]['bedeutung']}) ==")
            for t, p, f in table_verb(root):
                print(f"{t:5} {p:4} {f}")
            print()

    if "--manus" in args or "--all" in args:
        print("== MANUS-SILBENZERLEGUNG (§26) ==")
        amb = 0
        tot = 0
        for w, cat, parses, verdict in manus_report_data():
            tot += 1
            if "AMBIGUITÄT" in verdict or "NICHT" in verdict:
                if "AMBIGUITÄT" in verdict:
                    amb += 1
                print(f"{w} ({cat}): {verdict}")
                for p in parses[:6]:
                    print("    " + fmt_parse(p))
        print(f"({amb} von {tot} Grundformen mehrdeutig zerlegbar)")
        print()

    if "--strict" in args or "--update-baseline" in args:
        return run_strict(update="--update-baseline" in args)

    if "--sim-l09" in args:
        return run_sim_l09()

    if any(a in args for a in ("--schema", "--ids", "--translations", "--relations")):
        from .schema import run_schema
        return run_schema(args)

    if "--json" in args:
        path = args[args.index("--json") + 1]
        data = []
        for test_no, s, probs, vk in run_corpus(path):
            data.append({"test": test_no, "orbis": s,
                         "auto_befunde": probs, "vk_woerter": vk})
        print(json.dumps(data, ensure_ascii=False, indent=1))

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
