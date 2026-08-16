#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_findings.py — Migration Phase 3/28: Befundregister aufbauen.

Uebertraegt die im Audit (Orbis-Audit-0_1.md §A) und in den Berichten
dokumentierten Befunde 1:1 in ein maschinenlesbares Register.
Keine neuen Befunde, keine Bewertungsaenderung, keine Loesungen.
"""

import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "language", "findings", "findings.json")

# (id, typ, prio, titel_de, beschreibung_de, description_en, paragraphen,
#  betroffene_woerter, betroffene_saetze)
F = [
 ("K-01","conflict","P3",
  "Silbenformenliste deckt den eigenen Wortschatz nicht",
  "§5.1 listet nur V, KV, KVK, KKV, KKVK, KVKK. Der eingefrorene Wortschatz und die "
  "Beispielsaetze der Grammatik benoetigen zusaetzlich VK/VKK und KKVKK. §5.3 nennt granz "
  "und prens sogar selbst als Coda-Beispiele.",
  "§5.1 lists only V, KV, KVK, KKV, KKVK, KVKK. The frozen lexicon and the grammar's own "
  "example sentences additionally require VK/VKK and KKVKK.",
  ["§5.1","§5.3","§10.2","§15.2","§24","§25"],
  ["aul","eird","ain","oñ","es","granz","trelm","vresn","skirm","prilm","prens","dremn","vlent"],
  ["012","041"]),
 ("K-02","conflict","P3",
  "Pronomenformen verletzen die Fugenregel",
  "killa, dolla und kella(n) enthalten eine unverschmolzene l+l-Fuge, obwohl §21.4 "
  "ausdruecklich auch fuer Endungen gilt (vgl. mel+la → mela).",
  "killa, dolla and kella(n) keep an unmerged l+l boundary although §21.4 explicitly "
  "covers endings as well.",
  ["§13.4","§18.2","§21.4"], ["killa","dolla","kella"], []),
 ("K-03","conflict","P3",
  "Zahlkompositum verletzt die Fugenregel",
  "telnxelmmern (35) traegt eine m+m-Fuge; nach §21.4 muesste es telnxelmern lauten.",
  "telnxelmmern (35) keeps an m+m boundary; §21.4 would require telnxelmern.",
  ["§24.8","§21.4"], ["telnxelmmern"], []),
 ("K-04","conflict","P3",
  "Beispielsatz widerspricht der Adverbregel",
  "§12.4 verlangt Adverbien auf -un. Der Referenzsatz in §25.1 verwendet tolm adverbial "
  "ohne -un.",
  "§12.4 requires adverbs in -un, but the reference sentence in §25.1 uses tolm adverbially "
  "without -un.",
  ["§12.4","§25.1"], ["tolm","tolmun"], ["060"]),
 ("K-05","conflict","P1",
  "Modalverb im Nebensatz: zwei Regeln beanspruchen das Satzende",
  "§16.1 verlangt den Vollverb-Infinitiv am Satzende, §17.2 das finite Verb am Nebensatzende. "
  "Kein Beispiel entscheidet die Reihenfolge; mit Negation kommt die xa-Position hinzu.",
  "§16.1 places the infinitive at the end of the clause while §17.2 places the finite verb "
  "there; no example resolves the order.",
  ["§16.1","§17.2","§18.3"], [], ["103","105"]),
 ("L-01","gap","P1",
  "Stellung des Genitivattributs nicht festgelegt",
  "§8 definiert den Genitiv nur morphologisch, §17 schweigt zur Attributstellung. Alle "
  "Beispiele stellen nach; §13.3 regelt nur das Possessiv. Offen ist auch die Stapelung "
  "Genitiv + Possessiv.",
  "The position of the genitive attribute is undefined; all examples postpose it, but no rule "
  "states this, and stacking with a possessive is unresolved.",
  ["§8","§13.3","§17"], [], ["036","039"]),
 ("L-02","gap","P1",
  "Relativsatzbau fehlt vollstaendig",
  "fai ist als Relativpronomen gelistet, aber Kasus, Kongruenz und Verbstellung des "
  "Relativsatzes sind nirgends definiert. Zusaetzlich Homonymie mit fai 'dass'.",
  "fai is listed as a relative pronoun, but case, agreement and clause structure are "
  "undefined; it is also homonymous with the complementiser fai.",
  ["§13.4","§17.2","§20"], ["fai"], ["100","101","102","149"]),
 ("L-03","gap","P1",
  "Deklination der Fragewoerter kem/kelt undefiniert",
  "§18.2 listet nur Grundformen. 'Wen', 'wem', 'wessen' sind nicht bildbar; auch "
  "Indeklinabilitaet ist nicht festgelegt.",
  "§18.2 lists base forms only; accusative, dative and genitive of kem/kelt cannot be formed.",
  ["§18.2"], ["kem","kelt"], ["074","075","076"]),
 ("L-04","gap","P1",
  "Reflexivpronomen se ohne Kasusformen",
  "se ist gelistet, hat aber keine Kasusformen; der Personenbereich (nur 3. Person?) ist "
  "ebenfalls offen.",
  "se is listed without case forms, and its person range is undefined.",
  ["§13.4"], ["se"], ["033","035"]),
 ("L-05","gap","P1",
  "Agens im Passiv nicht ausdrueckbar",
  "§16.3 regelt nur die Vorsilbe şu-. Wie 'vom Mann gebaut' ausgedrueckt wird, ist nicht "
  "definiert; keine Praeposition ist dafuer ausgewiesen.",
  "§16.3 only defines the passive prefix şu-; there is no way to express the agent.",
  ["§16.3","§19"], [], ["137","138"]),
 ("L-06","gap","P2",
  "Deklination der Demonstrativa und Indefinita undefiniert",
  "§13.4 listet nur Grundformen von kilra/dolra usw. und kelsu/xakaun/kelte/xakelte.",
  "§13.4 lists base forms of demonstratives and indefinites only.",
  ["§13.4"], ["kilra","killa","kilna","dolra","dolla","dolna","kelsu","xakaun","kelte","xakelte"],
  ["088"]),
 ("L-07","gap","P2",
  "Plural der 10-Prozent-Gruppe nicht bildbar",
  "§10.1 regelt nur den Singular. Der regulaere Plural ist mangels Themavokal unanwendbar, "
  "der Kernwortplural -ei ist den 15 Kernwoertern vorbehalten.",
  "§10.1 covers the singular only; neither plural system applies to velkran, soralm, prilm.",
  ["§10.1","§9"], ["velkran","soralm","prilm"], []),
 ("L-08","gap","P2",
  "Syntax der Kardinalzahlen undefiniert",
  "Weder Kongruenz noch Numerus/Kasus des gezaehlten Nomens sind geregelt; kein Beispiel "
  "verwendet eine Kardinalzahl attributiv.",
  "Neither agreement nor the number/case of the counted noun is defined.",
  ["§24.8","§9"], [], ["070"]),
 ("L-09","gap","P2",
  "Keine Silbifizierungs-Praeferenzregel",
  "§5 legt erlaubte Silbenformen fest, aber nicht, wie eine Lautkette zerlegt wird. 77 von "
  "281 Grundformen sind dadurch mehrdeutig zerlegbar. Fuer Orbis Manus und eine kuenftige "
  "Tastatur ist der Befund blockierend (Keyboard-P1).",
  "§5 defines permitted syllable shapes but no parsing preference; 77 of 281 base forms are "
  "ambiguous, which blocks a deterministic Manus composer.",
  ["§5","§26"], ["mela","kavla","drovna","vresto","melisto","talisto","nestuma","luivresto",
                 "velkra","zaldre"], []),
 ("L-10","gap","P3",
  "Strichstaerkenregel deckt nicht alle Konsonanten",
  "§26.9 definiert duenn/mittel/dick fuer Vokale, Fliesslaute/Nasale und Verschlusslaute. "
  "Fuer die acht Reibelaute f s ş x v z j und die Affrikate ç fehlt jede Zuordnung.",
  "§26.9 leaves stroke weight undefined for the eight fricatives and the affricate.",
  ["§26.9"], [], []),
 ("U-01","unclear","P3",
  "§15.2-Formel deckt die eigenen Tabellen nicht",
  "Die Beschreibung 'Ablautstamm + Bindevokal -e- + Personendung' passt nicht auf esex "
  "(suppletiv, vo+Endung ohne -e-, Futurstamm vai-) und nicht auf die kontrahierten "
  "Praesensstaemme nu-/vur-. Die Formen selbst sind vollstaendig belegt.",
  "The stated formula does not cover the suppletive esex nor the contracted present stems "
  "of nuvex and vurnex; the tables themselves are complete.",
  ["§15.2"], ["esex","nuvex","vurnex"], ["121","133"]),
 ("U-02","unclear","P2",
  "Partizip als attributives Adjektiv ungeregelt",
  "§14 definiert das Partizip, §16.3 nutzt es praedikativ, §12.5 nominalisiert es. Ob es "
  "attributiv dekliniert werden darf, sagt keine Regel.",
  "No rule states whether the participle may be declined attributively.",
  ["§12","§14","§16.3"], [], ["051"]),
 ("U-03","unclear","P2",
  "Modalverb ohne Infinitiv ungeregelt",
  "§16.1 beschreibt Modalverben nur in der Klammerkonstruktion. Ob sie als Vollverb mit "
  "direktem Objekt stehen duerfen, ist offen.",
  "§16.1 describes modals only in the bracket construction; full-verb use is undefined.",
  ["§16.1"], ["suvr","nest","valn","dolm","vlek","tirn"], ["111"]),
 ("U-04","unclear","P2",
  "Subjektauslassung nur Beispielpraxis",
  "Die §18-Beispiele lassen das Subjektpronomen in Fragen weg, alle Aussagesatzbeispiele "
  "behalten es. Eine Regel fehlt.",
  "Pro-drop appears in question examples only; no rule governs it.",
  ["§18","§13.1"], [], ["071"]),
 ("U-05","unclear","P3",
  "Objektreihenfolge Dativ vor Akkusativ nur Praxis",
  "Alle Doppelobjekt-Beispiele zeigen Dativ vor Akkusativ; geregelt ist die Reihenfolge nicht.",
  "All ditransitive examples show dative before accusative, but the order is not stated.",
  ["§17"], [], ["023","025","026","064","120","146"]),
 ("U-06","unclear","P3",
  "Kasus nach kon/zil nicht festgelegt",
  "Beide Vergleichsbeispiele zeigen den Nominativ; eine Regel fehlt.",
  "Both comparison examples use the nominative, but no rule states the case.",
  ["§12.3"], ["kon","zil"], ["054","056"]),
 ("U-07","unclear","P3",
  "Ableitungsbehauptung bei Konjunktionen trifft nicht zu",
  "§20 behauptet, die unterordnenden Konjunktionen seien systematisch aus Praepositionen mit "
  "Suffix -i abgeleitet. Fuer dremi, tund und fai gilt das nicht.",
  "§20 claims subordinators derive from prepositions plus -i; this fails for dremi, tund, fai.",
  ["§20"], ["dremi","tund","fai"], ["095"]),
 ("U-08","unclear","P2",
  "Deklination von Komposita mit Kernwort-Kopf",
  "§21.3 vererbt Geschlecht und Klasse vom letzten Glied. Kernwoerter haben aber keine Klasse; "
  "taivbreun bleibt dadurch ungeregelt.",
  "§21.3 inherits gender and class from the head, but core nouns have no class, leaving "
  "taivbreun undefined.",
  ["§21.3","§10"], ["taivbreun"], []),
 ("U-09","unclear","P3",
  "Begriff Echovokal nicht definiert",
  "Aus den Tabellen ergibt sich: Echovokal = Themavokal des Nomens, bei Artikel und Adjektiv "
  "immer a. Als Regel formuliert ist das nirgends.",
  "The term echo vowel is only implied by the tables, never defined.",
  ["§9"], [], ["062","067"]),
 ("U-10","unclear","P3",
  "§26.8 nennt faelschlich 20 Konsonantentasten",
  "Orbis hat 19 Konsonanten; die 20. Kernform ist der Vokaltraeger (§26.2) und kein Konsonant. "
  "Korrekt waere '19 Konsonantentasten + 1 Vokaltraegertaste'.",
  "§26.8 says 20 consonant keys; Orbis has 19 consonants plus one vowel carrier.",
  ["§26.8","§26.2","§2.1"], [], []),
 ("U-11","unclear","P3",
  "Temporaler Dativ ohne Praeposition",
  "§25.2 verwendet Vraş zaldreş als blosse Dativ-Zeitangabe. Diese Konstruktion ist in §8, §17 "
  "und §19 nicht vorgesehen.",
  "§25.2 uses a bare dative as a temporal adjunct, a construction not provided for elsewhere.",
  ["§25.2","§8","§19"], [], []),
 ("U-12","unclear","P3",
  "Imperativ-Stuetz-e prueft nur §5.3",
  "Die Wurzeln dremn-, prens-, vlent- haben §5.3-konforme Codas, ihre Imperative haetten aber "
  "die Silbenform KKVKK, die §5.1 nicht fuehrt (haengt an K-01).",
  "The supporting -e is triggered by §5.3 only; the KKVKK shape issue of K-01 remains.",
  ["§14","§5.1","§5.3"], ["dremn","prens","vlent"], []),
 ("U-13","unclear","P3",
  "Praedikativstellung reibt sich an der V2-Regel",
  "Alle Beispiele stellen das Praedikativ vor das Verb (Lo loşn est = Verb an Position 3). Ob "
  "Praedikativ und Kopula als eine Position zaehlen, ist ungesagt.",
  "All examples place the predicative before the copula, leaving its relation to V2 unstated.",
  ["§12.2","§17.1"], [], ["055","057","121"]),
 ("U-14","unclear","P3",
  "Negationsbeispiel laesst das Objekt unmarkiert",
  "§18.3 schreibt 'Vim xa num vna breun'. Regelkonform nach §8/§10.3/§11 waere vnan breunen.",
  "The §18.3 example leaves the object unmarked where §8/§10.3/§11 would require inflection.",
  ["§18.3","§8","§10.3","§11"], ["breun"], ["083","122","134"]),
 ("W-01","lexical_gap","P2",
  "Wortschatzluecken fuer Grundkommunikation",
  "Es fehlen gaengige Grundverben und Konstruktionen, u. a. 'sagen', 'zeigen', 'suchen' sowie "
  "eine Existenzkonstruktion ('es gibt').",
  "Basic vocabulary is missing, including verbs for say, show, search and an existential "
  "construction.",
  ["§24"], [], ["104"]),
 ("W-02","lexical_collision","P2",
  "Formkollision velkran",
  "velkran 'Freundschaft' (Nominativ, 10-Prozent-Gruppe) ist formgleich mit dem Akkusativ von "
  "velkra 'Freund'. Beide gehoeren zum selben semantischen Feld; artikellose Kontexte sind "
  "mehrdeutig. Der Wortschatz-Freeze erlaubt Aenderungen bei echten Kollisionen.",
  "velkran 'friendship' is formally identical to the accusative of velkra 'friend'.",
  ["§10.1","§24.2"], ["velkran","velkra"], []),
 ("W-03","lexical_collision","P3",
  "Weitere Homonyme und Verwechselbarkeiten",
  "vran (unbestimmter Artikel M Akk / 'sehr'), kaun (Kernwort 'Mensch' / Indefinit 'man'), "
  "fai ('dass' / Relativpronomen, siehe L-02), xa ('nicht' / Gegenteilsvorsilbe). Dazu "
  "aehnliche Paare wie nest-/nast-, tolm/dolm-, şaln/şlan, kalm/kolm, xer/xerp.",
  "Further homonyms and near-homonyms are documented; none is resolved automatically.",
  ["§11","§13.4","§18.3","§20","§21.2","§24"],
  ["vran","kaun","fai","xa","nest","nast","tolm","dolm","şaln","şlan","kalm","kolm","xer","xerp"],
  []),
]

TYP_LABEL = {"conflict": "REGELKONFLIKT", "gap": "REGELLUECKE", "unclear": "REGELUNKLARHEIT",
             "lexical_gap": "WORTSCHATZLUECKE", "lexical_collision": "WORTSCHATZKOLLISION"}

def main():
    findings = []
    for (fid, typ, prio, titel, besch, desc_en, paras, woerter, saetze) in F:
        findings.append({
            "id": fid,
            "global_id": "ORB-FIND-" + fid,
            "typ": typ,
            "typ_label_de": TYP_LABEL[typ],
            "prioritaet": prio,
            "status": "open",
            "titel_de": titel,
            "description_de": besch,
            "description_en": desc_en,
            "affected_rules": paras,
            "affected_words": woerter,
            "affected_sentences": ["ORB-SENT-" + s.zfill(6) for s in saetze],
            "introduced_version": "grammar-0.9.3",
            "resolved_version": None,
            "decision_id": None,
            "quelle": "Orbis-Audit-0_1.md §A / Orbis-Testbericht-0_1.md",
        })
    payload = {
        "quelle": "Orbis-Audit-0_1.md, Orbis-Testbericht-0_1.md",
        "erzeugt_von": "tools/migration/build_findings.py",
        "hinweis": "Register bestehender Befunde. Keine Loesungen, keine Bewertungsaenderung. "
                   "Status-Werte: open / accepted / resolved / deferred / wont_fix.",
        "status_werte": ["open", "accepted", "resolved", "deferred", "wont_fix"],
        "anzahl": len(findings),
        "nach_prioritaet": {p: sum(1 for f in findings if f["prioritaet"] == p)
                            for p in ("P0", "P1", "P2", "P3", "P4")},
        "nach_typ": {t: sum(1 for f in findings if f["typ"] == t) for t in TYP_LABEL},
        "findings": findings,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"{len(findings)} Befunde -> language/findings/findings.json")
    print("  nach Prioritaet:", payload["nach_prioritaet"])
    print("  nach Typ:", payload["nach_typ"])
    return 0

if __name__ == "__main__":
    sys.exit(main())
