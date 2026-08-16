# Korpus

Sätze mit stabilen IDs (`ORB-SENT-nnnnnn`). Ein Satz kann **mehrere Rollen** haben —
Testkorpus und Lernkorpus sind nicht dasselbe.

| Verzeichnis | Rolle | Stand |
|---|---|---|
| `tests/` | Regressionskorpus: prüft die Grammatik | **150 Sätze** (Testkorpus 0.1) |
| `examples/` | Belege aus der Referenzgrammatik | **71 Sätze** (§-Beispiele) |
| `dialogues/` | zusammenhängende Gesprächssequenzen | leer — Phase H |
| `literary/` | literarische Texte | leer — nach 1.0 |
| `spoken/` | gesprochene Sprache, Aussprachebelege | leer — Phase I |

## Regeln

- **Orbis-Formen werden nie verändert**, um einen Satz „passend" zu machen.
- Ist ein Satz nach der geltenden Grammatik nicht eindeutig bildbar, trägt er
  `orbis: null`, einen Status (`open`/`conflict`/`unclear`/`testproblem`) und eine
  Befund-ID — es wird **keine Form erfunden**.
- Deutsch ist die semantische Quelle, Englisch wird daraus abgeleitet
  (`TRANSLATION_POLICY.md`).
- Schema: `sentence.schema.json`.
