# Somalia: law history in git

The law of Somalia as a git history: one file per provision, and the law that made each change as the commit's author, so `git blame` names the law behind every line.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `so/`.

**What is in it now (retrieved 2026-10-29 and 2026-10-30)**

| Folder | Law | Versions | Language |
| --- | --- | ---: | --- |
| `provisional-constitution/` | Provisional Constitution of the Federal Republic of Somalia, adopted 1 August 2012 | 1 | English version published by the Federal Parliament (later amendments, including 2024, are not in this text) |
| `codice-penale/` | Penal Code (Decreto legislativo 16 December 1962, n. 5), Italian text, articles 1 to 565 | 1 | The code as enacted, dated 3 April 1964 (six months after its publication in the Official Bulletin of 2 October 1963). **Text recognised by OCR, see below.** |

Source: the Federal Parliament of Somalia website (born-digital PDF). Parliament publishes acts as passed and no consolidated texts, so there is one version. The flag and emblem schedules are pictures and are not included.

This is a small build, not the whole statute book. Civil and commercial codes are not here. It has no dated history: each act is one "oldest version available" commit, dated from the source's own date and credited to the publisher. Texts are in the official language shown above; the English is a translation where marked, and the original governs.

Sources and terms are in `LICENSE`; how it was built is in `REPRODUCE.md`. Not legal advice; for anything that matters, read the original.

## About the Penal Code text: OCR, Italian, and its limits

The Penal Code was enacted in Italian (the code is a close adaptation of the Italian Rocco code) and the Italian text is what is here. The source is a scan of a printed edition of the code (page heads such as "Delitti contro l'amministrazione della giustizia"), whose decree note gives the Bollettino Ufficiale publication, held by Universita Roma Tre in its "Archivio Leggi della Somalia (1950-1989)" (https://arcadia.sba.uniroma3.it/handle/2307/17142), which is a third-party copy of the official text, not a Somali government site. The scan is low resolution (650 x 943 pixels a page) and its embedded text is unusable, so the pages were read with Tesseract 5.4 (Italian, enlarged three times). **The files are OCR text, not a typed copy, and they contain misreadings** (for example "pubplici", "precedenie", a damaged region in articles 2 and 3). Checked: random pages against the scan matched except for such slips. Known defects:

- Eight articles (186, 226, 309, 348, 420, 438, 451, 539) have no file of their own: OCR did not read their headings, so their text sits at the end of the article before them. Article 3 is inside article 2.
- Two pages were scanned upside down and were rotated; one page appears twice in the scan (article 173) and was used once.
- Article numbers were assigned in sequence and checked against the numbers OCR read; a few article numbers in the printed text are misread by OCR even where the file number is right.
- Headings (Libro, Titolo, Capo) and the index are left out. The Somali-language text of the code exists, but the copy found is a retyped translation with whole articles missing, so it is not used.
- The code has been amended in practice and its status differs across Somalia, Somaliland and Puntland; this is the text as enacted in 1962.

**Check the scan before relying on any wording.**
