# Sadhana Journal CSL Style

Citation Style Language (`.csl`) file for **Sādhanā: Academy Proceedings in Engineering Sciences**, published by the Indian Academy of Sciences (IASc) in co-publication with Springer Nature.

- **ISSN (Print):** 0256-2499
- **ISSN (Electronic):** 0973-7677
- **Style Classification:** Numeric (in-text baseline numbers with square brackets)
- **Author:** Jatin Gera
- **GitHub Repository:** [https://github.com/jgera/Sadhana-Journal-Zotero-Style](https://github.com/jgera/Sadhana-Journal-Zotero-Style)
- **Official Documentation:** [IAS Sadhana Information for Authors](https://www.ias.ac.in/Journals/S%C4%81dhan%C4%81/Information_for_Authors) | [Springer Sadhana](https://www.springer.com/journal/12046)

---

## Files in this Repository

| File | Description |
| :--- | :--- |
| [`sadhana-journal.csl`](file:///d:/Playground/Sadhana%20Citation/sadhana-journal.csl) | The official CSL 1.0 style specification file. |
| [`install_style.py`](file:///d:/Playground/Sadhana%20Citation/install_style.py) | Robust cross-platform installer script (Windows, macOS, Linux). |
| [`install_style.bat`](file:///d:/Playground/Sadhana%20Citation/install_style.bat) | 1-click Windows installer batch script. |
| [`sample-references.bib`](file:///d:/Playground/Sadhana%20Citation/sample-references.bib) | Benchmark references matching all examples from the journal guide. |
| [`test-output.md`](file:///d:/Playground/Sadhana%20Citation/test-output.md) | Markdown document to test in-text citations and bibliography generation. |

---

## Style Features & Rules

1. **In-text Citations:**
   - Serial baseline numbers in square brackets: `[1]`, `[1, 2]`.
   - Sequential references are automatically compressed into ranges: `[1–3]`.
2. **Bibliography Layout:**
   - Sequential numbered list: `[1]`, `[2]`, ...
   - Hanging indent (`second-field-align="flush"`).
3. **Authors and Editors:**
   - Surname followed by initials with a space and **no periods** (e.g., `Ghosh R and Naryanan G`, `Davidson P A`, `Karimi H R`).
   - Conjoined with `and` before the last author (no Oxford comma).
   - For 7 or more authors, the first 6 authors are listed, followed directly by `et al.` without a comma (e.g., `Huang C, Karimi H R, Mei P, Yang D, Shi Q, Guo J et al. 2023`).
   - In edited books, editors are preceded by `(ed)` or `(eds)` (e.g., `(eds) Pawar P M, Ronge B P, ... and Reddy P V.`).
4. **Year of Publication:**
   - Appears immediately after author names without parentheses: `Author(s) YYYY Title.`
5. **Titles:**
   - Sentence case / as entered, plain text (no quotation marks, no italics).
6. **Journal Articles:**
   - Abbreviated journal title, volume, issue in parentheses without space, colon, space, page range: `IIEE Trans. Power Electron. 24(6): 1444–1452.` or `Renew. Sustain. Energy Rev. 13: 915–920.`
7. **Books and Book Chapters:**
   - Book: `Davidson P A 2017 Introduction to magnetohydrodynamics. 2nd ed. Cambridge University Press, Cambridge, UK.`
   - Chapter: `Vayadande K, Patil R, Patni A, Bhadane P, Pawar S, Ponnuru R et al. 2024 Traffic sign recognition system using YOLO: Societal system for safe driving. In: TechnoSocietal 2022 (eds) Pawar P M, Ronge B P, Gidde R R, Pawar M M, Misal N D, Budhewar A S, More V V and Reddy P V. Springer, London. pp. 157–166.`
8. **Theses:**
   - Title followed by comma, degree (defaulting to `Ph.D. thesis.`), university, city, page: `Samiwala E B 2022 History of lithium batteries, Ph.D. thesis. University of Delhi, Delhi. p. 75.`
9. **Conferences:**
   - `In: Conference Proceedings Name, pp. 1743–1751.`
10. **Software and Websites:**
    - Software: `Dwyer B, Nelson J, Hansen T, Treacy R and Carlson J 2024 Roboflow (Version 1.0) Software. https://roboflow.com.`
    - Website: `NIST standard reference data base number 69, accessed on 22 November 2016 (http://webbook.nist.gov/chemistry).`
    - Standalone URL: `https://goldbook.iupac.org/list_goldbook_unit_defs.html (accessed on 22 November 2016).`

---

## Installation & Usage Instructions

### 1. Zotero

#### Option A: Automated Installation (Recommended)
- **Windows (1-Click):** Double-click [`install_style.bat`](file:///d:/Playground/Sadhana%20Citation/install_style.bat).
- **Cross-Platform (Python):** Run `python install_style.py` from the command line.

The script automatically locates your active Zotero data directory (including custom directories defined in `prefs.js`), validates the CSL syntax, copies the style file, and informs you if a restart is needed.

#### Option B: Manual Installation via Zotero GUI
1. Open **Zotero**.
2. Go to **Edit** (Windows) or **Zotero** (Mac) > **Settings** (or `Ctrl + ,`).
3. Select the **Cite** tab > **Style Manager**.
4. Click **Add from File...** (or the `+` button in older versions).
5. Select [`sadhana-journal.csl`](file:///d:/Playground/Sadhana%20Citation/sadhana-journal.csl) and click **Open**.
6. In Microsoft Word or LibreOffice Writer:
   - Click **Zotero Document Preferences**.
   - Select **Sadhana: Academy Proceedings in Engineering Sciences**.

### 2. Mendeley Reference Manager
1. Open **Mendeley Reference Manager**.
2. Go to **View** > **Citation Styles** > **More Styles...**
3. Select the **Installed** tab or drag and drop [`sadhana-journal.csl`](file:///d:/Playground/Sadhana%20Citation/sadhana-journal.csl) into Mendeley.
4. In **Mendeley Cite** for Microsoft Word:
   - Go to the **Citation Style** tab > **Select another style** > choose **Sadhana**.

### 3. Pandoc & Quarto
In Pandoc CLI:
```bash
pandoc manuscript.md --citeproc --csl=sadhana-journal.csl --bibliography=references.bib -o manuscript.docx
```
In Quarto / Markdown YAML frontmatter:
```yaml
---
title: "My Research Paper"
bibliography: references.bib
csl: sadhana.csl
---
```

---

## Rendered Output Examples

```text
[1] Ghosh R and Naryanan G 2008 Control of three phase, four wire PWPM rectifier. IIEE Trans. Power Electron. 24(6): 1444–1452.

[2] Lei M, Shiyan L, Chuanwen J, Hongling L and Yan Z 2009 A review on the forecasting of wind speed and generated power. Renew. Sustain. Energy Rev. 13: 915–920.

[3] Huang C, Karimi H R, Mei P, Yang D, Shi Q, Guo J et al. 2023 Evolving long short-term memory neural network for wind speed forecasting. Inf. Sci. 632: 390–410.

[4] Davidson P A 2017 Introduction to magnetohydrodynamics. 2nd ed. Cambridge University Press, Cambridge, UK.

[5] Vayadande K, Patil R, Patni A, Bhadane P, Pawar S, Ponnuru R et al. 2024 Traffic sign recognition system using YOLO: Societal system for safe driving. In: TechnoSocietal 2022 (eds) Pawar P M, Ronge B P, Gidde R R, Pawar M M, Misal N D, Budhewar A S, More V V and Reddy P V. Springer, London. pp. 157–166.

[6] Varma G, Subramanian A, Namboodiri A, Chandraker M and Jawahar C V 2019 IDD: A dataset for exploring problems of autonomous navigation in unconstrained environments. In: Proceedings of the IEEE winter conference on applications of computer vision (WACV), pp. 1743–1751.

[7] Samiwala E B 2022 History of lithium batteries, Ph.D. thesis. University of Delhi, Delhi. p. 75.

[8] Dwyer B, Nelson J, Hansen T, Treacy R and Carlson J 2024 Roboflow (Version 1.0) Software. https://roboflow.com.

[9] NIST standard reference data base number 69, accessed on 22 November 2016 (http://webbook.nist.gov/chemistry).

[10] https://goldbook.iupac.org/list_goldbook_unit_defs.html (accessed on 22 November 2016).
```
