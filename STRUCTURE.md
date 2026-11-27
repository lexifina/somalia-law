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
| `hirshabelle/...` | Hirshabelle State, a federal member state: `constitution/`, `acts/<year>/...` |

Laws and decrees taken from the Official Bulletin (Faafinta Rasmiga ah / Bollettino Ufficiale) sit in `acts/<year>/`
(laws, legislative decrees) and `subsidiary/<year>/<NNN>-<issuer>-<slug>/` (presidential and ministerial decrees),
named in the language the Bulletin printed them in (Somali from 1973, Italian or English before).

Each folder holds one file per article (`art-023.md` is Article 23; `art-012-bis.md` is Article 12 bis), a `README.md`
with the source and the article headings, or `text.md` when the text has no numbered articles. No folder holds more
than 1,000 entries.

## Dates

Each version is one commit, dated 12:00 Africa/Mogadishu on the day it took effect, which its `In-force:` trailer
repeats. `In-force-basis:` says where that day comes from:

- `faolex-entry-into-force`: the entry-into-force date in the FAOLEX record;
- `faolex-date-of-text`: the date of the law in the FAOLEX record, where the record gives no other entry-into-force
  day (or says the law applies from its signature or adoption);
- `promulgation-decree-date`: Somaliland laws, the day of the presidential decree putting the law into force, as
  the House of Representatives of Somaliland lists it;
- `promulgation-decree-in-text`, `adoption-date-in-text`, `in-force-date-on-cover`: a date printed in the text;
- Official Bulletin items: `in-force-date-in-text` (the day the entry-into-force article names),
  `signature-date-in-text` (in force on signature or immediately: the signature day in the Bulletin heading),
  `official-bulletin-date` (in force on publication: the issue date), `bulletin-date-plus-days` (a set number of
  days after publication, counted from the issue date). Items whose entry-into-force article cannot be read are held;
- the first two acts carry the trailers of the first build (see their commits).

FAOLEX's "date of text" is no longer used as an in-force day for new versions; FAOLEX records without an
entry-into-force day are held.

A text that comes into force a set time after publication in the Official Bulletin, without the publication day,
is held back, not guessed. Before 1970 (which git cannot store) a commit is dated 1 January 1970, one second after
the one before it; the real day is in the subject and the `In-force:` trailer. No date in this repository is the day
we downloaded anything.

## Sources and status

- Federal Parliament of Somalia, <https://parliament.gov.so> (official). Most of its law PDFs are scans (no text
  layer; Lexifina runs no OCR) or bills and unnumbered drafts without a date; those are held.
- FAOLEX (FAO), <https://faolex.fao.org>: secondary copies, marked `Source-status: secondary copy (...)`;
  `Text-source: publisher OCR` marks a text layer the publisher made from a scan.
- Universita Roma Tre, Centro Studi Somali, Archivio Leggi della Somalia
  (<https://arcadia.sba.uniroma3.it/handle/2307/6103>): the Italian Penal Code of the first build, and the Official
  Bulletin issues (1960-1989, 2013-2014) split into laws and decrees; secondary copies, `Text-source: publisher OCR`.
  Appointments, promotions, honours, land grants, licences and other individual measures are left out.
- House of Representatives of Somaliland, <https://somalilandparliament.net/acts> (official): Somaliland laws.
- Upper House of the Federal Parliament, <https://senate.gov.so>; Hirshabelle State Assembly,
  <https://hirshabelleparliament.so>; House of Representatives of Puntland State, <https://puntlandparliament.com>
  (official). Most Puntland and Hirshabelle laws are scans without a text layer and are held.
- Not used: somalilandlaw.com (its notice forbids reproduction without the owners' written permission); the
  Ministry of Justice and Refworld (they block automated access).
