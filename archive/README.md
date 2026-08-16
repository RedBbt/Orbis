# Archiv

Eingefrorene Vorfassungen. **Nie Quelle, nur Beleg.** Kein Werkzeug und kein Bericht
liest aus diesem Verzeichnis; keine Datei hier ist kanonisch.

| Datei | Was es ist | Ersetzt durch |
|---|---|---|
| `corpus/Orbis-Testkorpus-0.1.md` | Chat-Entwurf des Testkorpus (Punktversion). Enthält u. a. einen unentdeckten Kongruenzfehler in Satz 48 (*loşna* statt *loşnla*) und wertet mehrere ungeregelte Konstruktionen unmarkiert als korrekt. | `Orbis-Testkorpus-0_1.md` (kanonisch) bzw. `language/corpus/tests/testkorpus-0_1.json` |
| `orbis_validator-0_1-monolith.py` | Monolithische Vorfassung des Validators (Sprachdaten hartkodiert). Diente als Migrationsgrundlage; ihre Ausgabe ist die eingefrorene Baseline unter `reports/baseline/`. | Paket `tools/validator/` + Sprachdaten unter `language/` |

**Regel:** Wird eine archivierte Datei gebraucht, um etwas nachzuvollziehen, ist das in
Ordnung. Wird sie gebraucht, um eine Sprachfrage zu beantworten, ist das ein Fehler —
dafür gilt ausschließlich `Orbis-Grammatik-0.9.3.md` und die daraus migrierten Daten.
