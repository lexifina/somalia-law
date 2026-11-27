# Structure

| Folder | What it holds |
| --- | --- |
| `constitution/` | The Provisional Constitution of the Federal Republic of Somalia (2012), English text |
| `constitution-somali/` | The same Constitution in its Somali text (Dastuurka Ku-Meel Gaarka ah), as adopted |
| `codes/<code>/` | The codes: `penal-code/` (1962, Italian), `civil-code/` (1973), `labour-code/` (Law No. 36 of 2024), `maritime-code/` (1959) |
| `acts/<year>/<NNN>-<slug>/` | A federal (or, before 1991, national) law, by its year and number, e.g. `acts/1972/037-law-on-the-somali-territorial-sea-and-ports/`; a law whose number the source does not print has no number prefix |
| `subsidiary/<year>/<NNN>-<slug>/` | Decrees, regulations and guidelines made under a law |
| `historical/<slug>/` | Constitutions no longer in force, e.g. `historical/constitution-1960/` |
| `somaliland/...` | Somaliland, a separate jurisdiction: `constitution/`, `acts/<year>/...`, `subsidiary/<year>/...` |
| `puntland/...` | Puntland State, a federal member state: the same layout |

Each folder holds one file per article (`art-023.md` is Article 23; `art-012-bis.md` is Article 12 bis), a `README.md`
with the source and the article headings, or `text.md` when the text has no numbered articles. No folder holds more
than 1,000 entries.

## Dates

Each version is one commit, dated 12:00 Africa/Mogadishu on the day it took effect, which its `In-force:` trailer
repeats. `In-force-basis:` says where that day comes from:

- `faolex-entry-into-force`: the entry-into-force date in the FAOLEX record;
- `faolex-date-of-text`: the date of the law in the FAOLEX record, where the record gives no other entry-into-force
  day (or says the law applies from its signature or adoption);
- the first two acts carry the trailers of the first build (see their commits).

A text that comes into force a set time after publication in the Official Bulletin, without the publication day,
is held back, not guessed. Before 1970 (which git cannot store) a commit is dated 1 January 1970, one second after
the one before it; the real day is in the subject and the `In-force:` trailer. No date in this repository is the day
we downloaded anything.

## Sources and status

- Federal Parliament of Somalia, <https://parliament.gov.so> (official). Most of its law PDFs are scans (no text
  layer; Lexifina runs no OCR) or bills and unnumbered drafts without a date; those are held.
- FAOLEX (FAO), <https://faolex.fao.org>: secondary copies, marked `Source-status: secondary copy (...)`;
  `Text-source: publisher OCR` marks a text layer the publisher made from a scan.
- Universita Roma Tre, Archivio Leggi della Somalia: the Italian Penal Code of the first build.
- Not used: somalilandlaw.com (its notice forbids reproduction without the owners' written permission); the
  Ministry of Justice and Refworld (they block automated access).
