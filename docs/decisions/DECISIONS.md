# Entscheidungsregister (ADR)

Jede Entscheidung, die verändert **wie Orbis funktioniert** — nicht nur, wie es
dokumentiert oder gespeichert wird — braucht einen eigenen Eintrag mit stabiler ID
`ORB-ADR-nnnn`. Werkzeuge und Assistenzsysteme dürfen solche Entscheidungen nicht
treffen (ORBIS_CONSTITUTION Art. 16), sondern nur vorbereiten.

## Aufbau eines ADR

Jede Datei `ORB-ADR-nnnn-kurztitel.md` enthält: ID · Datum · Status · Problem ·
vorhandene Optionen · Entscheidung · Begründung · Auswirkungen · betroffene Regeln ·
betroffene Wörter · betroffene Tests · Version.

Status: `vorbereitet` (Optionen liegen vor, niemand hat entschieden) · `entschieden` ·
`abgelehnt` · `zurückgestellt` · `überholt`.

## Register

| ID | Titel | Befund | Status | Version |
|---|---|---|---|---|
| ORB-ADR-0001 | Architektur: maschinenlesbare Sprachdaten als Source of Truth | — | entschieden | tools-0.2 |
| ORB-ADR-0002 | Stellung des Genitivattributs | L-01 | vorbereitet | (0.9.4) |
| ORB-ADR-0003 | Relativsatzbau | L-02 | vorbereitet | (0.9.4) |
| ORB-ADR-0004 | Deklination der Fragewörter kem/kelt | L-03 | vorbereitet | (0.9.4) |
| ORB-ADR-0005 | Kasusformen und Personenbereich des Reflexivpronomens se | L-04 | vorbereitet | (0.9.4) |
| ORB-ADR-0006 | Agens im Passiv | L-05 | vorbereitet | (0.9.4) |
| ORB-ADR-0007 | Modalverb im Nebensatz | K-05 | vorbereitet | (0.9.4) |
| ORB-ADR-0008 | Silbifizierungsregel (blockiert Orbis Manus und Tastatur) | L-09 | vorbereitet | (0.9.4) |
| ORB-ADR-0009 | Formkollision velkran | W-02 | vorbereitet | (0.9.4) |
| ORB-ADR-0010 | Redaktionskorrekturen der Referenzgrammatik | K-01, K-03, K-04, U-01, U-10 | vorbereitet | (0.9.4) |
| ORB-ADR-0011 | Klangreform: Entlastung des Lautes x | — | vorbereitet | (0.9.4+) |

Die inhaltliche Aufbereitung der Punkte 0002–0010 mit Optionen, Beispielsätzen und
Folgekosten steht in `decisions/Entscheidungsvorlage-0_9_4.md`. Sobald die
Sprachdesigner entscheiden, wird je Punkt eine ADR-Datei angelegt und der Status
hier auf `entschieden` gesetzt.
