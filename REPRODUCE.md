# How this repository was made (Somalia)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Federal Parliament of Somalia: Provisional Constitution 2012 (English) | <https://parliament.gov.so/wp-content/uploads/2024/12/Provisional-Constitution-2012.pdf> | 2026-10-29 | no licence stated |
| Università Roma Tre, Archivio Leggi della Somalia (1950-1989): Codice Penale (scan of the Bollettino Ufficiale) | <https://arcadia.sba.uniroma3.it/handle/2307/17142> | 2026-10-30 | Laws are not protected by copyright: Somali Democratic Republic Copyright Law No. 66 of 7 Sept 1977, Art. 5 (laws and government regulations) |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `provisional-constitution` | Provisional Constitution of the Federal Republic of Somalia (2012) | 1 | 2012-08-01 to 2012-08-01 |
| `codice-penale` | Codice penale della Repubblica Somala (Somali Penal Code), 1962, Italian text | 1 | 1964-04-03 to 1964-04-03 |

The build made 2 commits:

| Commits | Kind |
| ---: | --- |
| 2 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 1 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 1 laws in the record.
- 3 tags.

## Dates

Each commit is dated at noon (Africa/Mogadishu) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: The Provisional Constitution carries "Adopted August 1, 2012" on its cover; that date is used as its in-force date. https://parliament.gov.so/wp-content/uploads/2024/12/Provisional-Constitution-2012.pdf

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `5f62db0236b4efd554b365daacdd4fdf50f111cf6b44c72b803608c041305be8` (493675 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

2 versions of 2 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- English is built: the PDF is the English version of the Provisional Constitution; the parliament site also holds a Somali text, not used.
- One version dated 2012-08-01, the adoption date on the cover. Later amendments are not published as a consolidated text on the source.
- Chapter and Title headings are kept at the start of the article that follows them; line wraps are joined into paragraphs.
- Penal Code: the Italian text of the code as enacted by Decreto legislativo 16 December 1962 n. 5, read by OCR (tesseract 5.4, ita, 3x enlargement) from the Roma Tre archive's scan of the Official Bulletin (208 pages, 650x943 px). The Somali version on the same archive is a retyped translation with whole articles missing and was not used.
- Penal Code version dated 1964-04-03: the decree enters into force six months after publication, and the Bulletin footnote gives the publication as 2 October 1963 (Suppl. 1 to no. 10); 3 April 1964 is the date commonly given for entry into force. The 1963 Bulletin is the only dated source read.
- Penal Code: article numbers were assigned in sequence and matched against the numbers the OCR read (several are misread); 8 of 565 articles have no heading read by OCR and are included in the text of the article before them: 186, 226, 309, 348, 420, 438, 451, 539. Headings (Libro, Titolo, Capo, Sezione) are left out.
- Penal Code: pages scanned twice or out of order were repaired where a heading repeated (art. 173); two pages scanned upside down (pp. 15 and 116 of the scan) were rotated before OCR; running heads, rule lines and footnote markers were removed.
- Penal Code: the Italian text of the code as enacted by Decreto legislativo 16 December 1962 n. 5, read by OCR (tesseract 5.4, ita, 3x enlargement) from the Roma Tre archive's scan of a printed edition of the code (208 pages, 650x943 px). The Somali version on the same archive is a retyped translation with whole articles missing and was not used.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code wrote the parser; it did not write or alter any legal text. 0 model calls at data-build time.
- OCR with tesseract 5.4 (ita) of 208 page images of the Penal Code; no model-generated text. Article boundaries and numbers found by a script.
