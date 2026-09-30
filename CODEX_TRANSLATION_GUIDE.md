# Codex Guide: Rebuild and Execute the GPU History Translation Workflow

> This document is an execution specification. Give it to Codex together with the original PDF. Codex must be able to start with no existing repository, no previous Markdown, and no previous translation files.

## 1. Mission and completion definition

Process the complete book *The History of the GPU – Steps to Invention* into:

1. independently reviewable source chapter PDFs;
2. cleaned, source-faithful English Markdown;
3. Chinese Markdown translated from the approved English Markdown;
4. extracted original figures shared by both editions;
5. manifests, glossaries, notes, logs, and QA reports that make every decision auditable.

A chapter is complete only when its boundaries, English structure, figures, captions, references, Chinese translation, and automated/manual QA have all passed. Do not mark a chapter complete merely because text extraction or machine translation finished.

This is a historical translation project, not an adaptation, summary, modernization, or textbook rewrite. Preserve the source's order, hierarchy, claims, examples, numbers, names, dates, citations, tables, quotations, figures, and captions.

### Copyright

The PDF, original text, and original images remain protected by their rights holders. Do not publish or distribute a complete translation, reproduced figures, or extracted PDFs unless the necessary translation, reproduction, and distribution rights have been confirmed. Keep the source PDF and extracted assets private unless authorized.

## 2. Non-negotiable rules

### Preserve source structure

- Do not invent headings because text is prominent, centered, repeated, or visually near a figure.
- Do not merge two source headings into one, split one heading into several, or change heading levels without evidence from the PDF.
- Preserve the order of headings, paragraphs, lists, quotations, tables, figures, captions, footnotes, and references.
- A page-audit marker such as `Printed page 12` is metadata, not a source heading. Put audit metadata in a blockquote, HTML comment, manifest, or notes file; never let it masquerade as prose.
- Do not silently remove a passage because it seems repetitive, historically doubtful, outdated, or incorrect. If the PDF truly repeats a passage, preserve it and record the issue. Remove only an extraction artifact after confirming it against the page image/text layer, and log the correction.

### Preserve figures and captions

- Retain every source figure that belongs to the chapter and retain its complete figure number and caption.
- Translate the caption in Chinese, but do not shorten it. For example, if the source caption is `The History of the GPU - Steps to Invention`, do not reduce it to `History of the GPU`.
- Do not add a heading such as `### The History of the GPU — Steps to Invention` unless that heading actually exists in the source.
- Do not edit, redraw, crop, overwrite, or translate pixels inside an extracted original image.
- English Markdown must not convert words inside a figure into ordinary English prose or an ordinary English table.
- If a Chinese reader needs a translation of text inside an image, retain the original image and put the translation only in a clearly marked translator's note, normally a blockquote beginning `> **译者注：**`. State explicitly that the table or list is a translation of text inside the image and is not part of the source正文.
- English and Chinese Markdown must reference the same extracted image file, not two independently modified copies.
- Center the image and its caption together where Markdown rendering permits:

```html
<div align="center">

![Fig. 1.1 A raster graphics display consists of quantized elements known as pixels](../images/chapter-01-fig-02.jpeg)

*Fig. 1.1 A raster graphics display consists of quantized elements known as pixels*

</div>
```

Chinese example:

```html
<div align="center">

![图 1.1　光栅图形显示器由称为像素的量化元素组成](../source/en/images/chapter-01-fig-02.jpeg)

*图 1.1　光栅图形显示器由称为像素的量化元素组成*

</div>
```

### Preserve facts and evidence

- Preserve all dates, numbers, units, frequencies, model numbers, chip names, processor names, API names, URLs, identifiers, and citation markers.
- Preserve full references in their original order. Never replace a reference with `[reference]`, a URL alone, or a shortened placeholder.
- Do not silently correct a disputed or apparently inaccurate historical claim. Translate what the author wrote. Record a possible issue in `notes/translation-notes.md`; add a translator's note only when useful and clearly label it.
- Keep official company, product, chip, interface, architecture, and organization names recognizable. Use a glossary rather than ad hoc changes.

### Mark all additions

Anything Codex adds that is not in the source—explanation, uncertainty, historical context, image-text translation, correction note, or extraction warning—must be explicitly marked as metadata, a problem-log entry, or a translator's note. It must never look like source prose.

## 3. Start from the original PDF

### Canonical input

Create exactly one canonical input path:

```text
source/original/book.pdf
```

If the user supplies several PDFs:

1. list all candidates;
2. calculate SHA-256 hashes and byte sizes;
3. inspect page counts, title metadata, text layer, and visible first/last pages;
4. determine whether they are duplicates, partial files, or different editions;
5. record the decision in `notes/source-inventory.json`;
6. select one canonical file and stop using the others unless explicitly authorized.

Never silently combine pages or assets from two files.

### Recommended initial tree

Create this before processing chapters:

```text
source/
  original/
    book.pdf
  en/
    raw/
    chapters/
    images/
translation/
glossary/
notes/
scripts/
work/
  text/
  renders/
  contactsheets/
  logs/
  qa/
dist/
```

`work/` contains reproducible intermediate files and must not be treated as edited source. `source/en/chapters/` and `translation/` contain human-reviewable deliverables. Do not overwrite a deliverable without checking whether it contains manual edits.

Create UTF-8 text files. On Windows, use an explicit UTF-8 environment when necessary:

```bash
PYTHONIOENCODING=utf-8 python scripts/inventory_pdf.py source/original/book.pdf
```

Required tools:

- Python 3;
- PyMuPDF: `python -m pip install pymupdf`;
- Poppler `pdftotext` if available, preferably for `-layout` extraction;
- a PDF viewer or page renderer for visual verification;
- a Markdown renderer or previewer;
- Git for checkpoints when the project is maintained as a repository.

If `pdftotext` is unavailable, use PyMuPDF extraction and record that fact. Do not stop treating extracted text as something requiring visual verification.

## 4. Inspect the PDF before translation

Run an inventory before cutting any chapter. Record:

- SHA-256 and file size;
- total PDF page count;
- PDF metadata;
- whether a text layer exists;
- page labels/printed-page labels;
- bookmark/TOC entries and their levels;
- first and last text lines of every candidate chapter page;
- contents, list of figures, list of tables, and index ranges;
- extraction warnings and pages needing visual review.

PyMuPDF page indices are zero-based. Human-facing PDF page numbers are one-based. Always use explicit names such as `pdf_page_1based` and `pymupdf_index_0based`; never pass an ambiguous `page` field between scripts.

A useful inventory skeleton:

```python
# scripts/inventory_pdf.py
import hashlib, json, sys
from pathlib import Path
import fitz

pdf = Path(sys.argv[1])
out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("notes/source-inventory.json")

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

doc = fitz.open(pdf)
page_labels = doc.get_page_labels() if hasattr(doc, "get_page_labels") else []
pages = []
for i, page in enumerate(doc):
    text = page.get_text("text")
    pages.append({
        "pymupdf_index_0based": i,
        "pdf_page_1based": i + 1,
        "printed_label": page.get_label() if hasattr(page, "get_label") else None,
        "text_chars": len(text),
        "first_lines": text.splitlines()[:3],
        "last_lines": text.splitlines()[-3:],
    })

result = {
    "path": str(pdf),
    "sha256": sha256(pdf),
    "bytes": pdf.stat().st_size,
    "pdf_pages": len(doc),
    "metadata": doc.metadata,
    "page_labels": page_labels,
    "toc": doc.get_toc(simple=True),
    "pages": pages,
}
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"wrote {out}; pages={len(doc)}; sha256={result['sha256']}")
```

Use bookmarks as boundary clues, not as unquestionable truth. Confirm each boundary with:

1. the bookmark title and level;
2. the first page's visible chapter heading;
3. the previous page's visible ending;
4. the last page's text and page image;
5. the Contents/List of Figures/List of Tables where relevant;
6. printed page labels, which can skip numbers.

### Known sanity-check for this edition

The complete source examined during preparation has 424 PDF pages and these approximate top-level ranges. Reconfirm them from the actual input before use:

| Unit | Complete PDF pages, 1-based | Printed-page indication |
|---|---:|---:|
| Foreword | 5–7 | v–vii |
| Preface | 8–14 | ix–xv |
| Contents and front lists | 15–28 | xvii–xxxi |
| Chapter 1 | 29–58 | begins at 1; inspect endpoint |
| Chapter 2 | 59–125 | begins at 31 |
| Chapter 3 | 126–173 | begins at 99 |
| Chapter 4 | 174–229 | begins at 147 |
| Chapter 5 | 230–291 | begins at 203 |
| Chapter 6 | 292–359 | begins at 265 |
| Chapter 7 | 360–372 | begins at 333 |
| Appendix A | 373–378 | begins at 347 |
| Appendix B | 379–417 | begins at 353 |
| Index | 418–424 | begins at 393 |

These are validation clues, not permission to hardcode blindly. The printed page numbering contains intentional gaps. In particular, do not derive printed pages using one constant offset from PDF pages. Store both systems in the manifest.

For each unit write a record similar to:

```json
{
  "id": "02-chapter-1",
  "kind": "chapter",
  "title_source": "Introduction",
  "pdf_page_start_1based": 29,
  "pdf_page_end_1based": 58,
  "printed_page_start": "1",
  "printed_page_end": "30",
  "boundary_status": "verified",
  "boundary_evidence": ["toc", "page-labels", "first-page-heading", "last-page-review"]
}
```

If evidence conflicts, set `boundary_status` to `needs-review`; do not proceed as if the conflict did not exist.

## 5. Extract independent chapter PDFs

For each verified range, create one PDF in `source/en/raw/`, for example:

```text
source/en/raw/02-introduction.pdf
```

PyMuPDF uses zero-based slicing. A safe extraction function:

```python
import fitz
from pathlib import Path

def extract_range(src, dest, start_pdf_1based, end_pdf_1based):
    if start_pdf_1based < 1 or end_pdf_1based < start_pdf_1based:
        raise ValueError("invalid inclusive 1-based range")
    source = fitz.open(src)
    if end_pdf_1based > len(source):
        raise ValueError("range exceeds source PDF")
    output = fitz.open()
    output.insert_pdf(
        source,
        from_page=start_pdf_1based - 1,
        to_page=end_pdf_1based - 1,
    )
    expected = end_pdf_1based - start_pdf_1based + 1
    if len(output) != expected:
        raise AssertionError((len(output), expected))
    Path(dest).parent.mkdir(parents=True, exist_ok=True)
    output.save(dest)
    output.close()
    source.close()
```

After extraction:

- reopen the chapter PDF;
- verify its page count equals `end - start + 1`;
- compare first and last page text to the complete PDF;
- record SHA-256, page count, source range, and verification time in the manifest;
- visually inspect the first and last pages;
- never call an incomplete extraction complete.

## 6. Extract working text, then reconstruct English Markdown

Create reproducible working text, not final Markdown:

```bash
pdftotext -layout -f 29 -l 58 source/original/book.pdf work/text/02-introduction.layout.txt
```

Also extract with PyMuPDF when possible. Compare both outputs around headings, columns, figure captions, tables, footnotes, ligatures, hyphenated line breaks, and references. Render suspicious pages to images.

Clean-up operations may include:

- joining a line broken only by PDF line wrapping;
- joining a word split by a line-end hyphen only when the page image proves it is one word;
- normalizing ligatures such as `ﬁ` after checking names and URLs;
- removing repeated running headers/footers and page numbers from prose;
- preserving intentional hyphens, em dashes, bullet lists, numbered lists, quotations, table cells, and footnotes;
- retaining meaningful capitalization and punctuation.

Never use a global regex that can delete legitimate content. Keep a change log for nontrivial repairs.

### English file metadata

Each English chapter should begin with a metadata block similar to:

```markdown
> Source: *The History of the GPU – Steps to Invention*  
> Printed pages: 1–30  
> PDF pages in the complete source: 29–58  
> Raw chapter PDF: [`../raw/02-introduction.pdf`](../raw/02-introduction.pdf)
```

This block is project metadata, not part of the book's prose. Use the exact verified printed range; do not copy an old range merely because it appears in an earlier note.

### Heading decisions

Determine heading levels from the original page, bookmarks, contents, and repeated structural evidence. Preserve the source's wording. Do not convert a figure caption into a heading. Do not create a heading from a book title printed below a cover image. If uncertainty remains, record it in the issue log and pause the structural decision.

### Tables, quotations, lists, notes, and references

- Reconstruct a source table as a Markdown table only when the table is actually a table in the source layout.
- Do not make an English table from text printed inside a raster figure.
- Preserve list nesting and item order.
- Use Markdown blockquotes for source quotations when that represents the source structure; do not confuse them with translator notes.
- Keep footnotes or endnotes associated with the correct marker and explain any unavoidable Markdown representation in notes.
- Preserve all references, not merely those most relevant to the current paragraph.

## 7. Extract and map figures correctly

Do not assume that the number of image objects equals the number of numbered figures. A page can contain decorative logos, masks, repeated resources, thumbnails, or multiple objects forming one visual figure. In one previously inspected chapter, 20 unique objects yielded 19 numbered figures because a 67×67 object was decorative. Treat that as a warning, not as an automatic size filter.

For every chapter:

1. enumerate embedded image objects page by page;
2. deduplicate by xref, while recording every page where an xref occurs;
3. extract original bytes without recompression when possible;
4. record xref, PDF page, dimensions, extension, colorspace, object order, and page rectangle/position;
5. extract nearby text and candidate captions;
6. render pages and, if useful, create a contact sheet in `work/contactsheets/`;
7. compare against the source page, Contents, List of Figures, and body references;
8. assign a formal figure number only after human review;
9. record excluded decorative objects and the reason in the image manifest.

A manifest entry should include at least:

```json
{
  "file": "chapter-01-fig-02.jpeg",
  "chapter_id": "02-chapter-1",
  "source_pdf_page_1based": 29,
  "pymupdf_index_0based": 28,
  "xref": 123,
  "width": 640,
  "height": 480,
  "extension": "jpeg",
  "formal_figure": "1.1",
  "mapping_status": "verified",
  "mapping_evidence": ["caption", "page-position", "visual-review"],
  "excluded": false
}
```

Do not map `chapter-01-fig-01` to Fig. 1.1 merely because it was extracted first. The filename is an asset identifier, not evidence of a figure number.

Use the complete caption as the primary displayed text. The alt text should also be meaningful, but it must not replace the visible caption.

## 8. Translate only after English structure is approved

The Chinese file is translated from the reviewed English Markdown, while the PDF remains the authority for ambiguous layout and figures. The Chinese file must preserve:

- the same chapter and section heading count and hierarchy;
- paragraph and list order;
- table shape and row/column order;
- quotations and footnote markers;
- figure location and figure number;
- complete translated captions;
- reference count and order;
- dates, numbers, units, models, names, URLs, and identifiers.

Do not use machine translation as a final pass without human technical and structural review. If automated translation is used as a draft, compare every paragraph to the English source and then to the PDF for names, numbers, captions, and references.

### Terminology and names

Create and update:

```text
glossary/gpu-terms.md
glossary/companies-and-products.md
glossary/people.md
```

Each entry should record the English form, preferred Chinese rendering, abbreviation, context, and any rejected alternatives. Examples:

| English | Preferred Chinese | Note |
|---|---|---|
| GPU (graphics processing unit) | 图形处理器（GPU） | Preserve GPU after first expansion |
| graphics controller | 图形控制器 | Do not automatically replace with GPU |
| graphics accelerator | 图形加速器 | Context-dependent |
| coherent cache | 一致性缓存 | Review plural/possessive context |
| inter-processor communication | 处理器间通信 | Preserve GPU context |
| rasterization | 光栅化 | |
| framebuffer | 帧缓冲区 | |
| shader | 着色器 | |
| transform and lighting (T&L) | 变换与光照（T&L） | |
| fixed-function | 固定功能 | |
| parallel processor | 并行处理器 | |
| API | 应用程序编程接口（API） | Preserve common abbreviation |

Retain official English names for products, chips, interfaces, standards, organizations, and companies unless a documented project decision says otherwise. Do not translate model identifiers. Keep personal-name rendering consistent and record uncertain transliterations.

Do not perform blind global replacement: a term can change meaning by context. Review every occurrence after a glossary update.

### Translator's notes

Use this pattern:

```markdown
> **译者注：** 这里的说明是译者补充，不属于原文正文。
```

For image-internal text:

```markdown
> **译者注：** 原图中的文字未被修改。下表仅是对图片内文字的翻译，不属于原文正文；原图仍按原样保留。
>
> | 原图项目 | 译文 |
> |---|---|
> | ... | ... |
```

Never hide a translator's note in a normal paragraph or unmarked table.

## 9. Per-chapter state machine and files

Maintain `notes/chapter-status.json` or an equivalent table. Recommended states:

```text
discovered
boundaries-verified
raw-pdf-verified
text-extracted
english-reconstructed
figures-mapped
english-qa-passed
translation-drafted
translation-qa-passed
bilingual-qa-passed
complete
```

A chapter can advance only when its current state's evidence is recorded. Use one issue log such as `notes/translation-notes.md` with fields:

```text
ID:
Chapter/page:
Type: boundary | extraction | figure | terminology | historical | translation | QA
Evidence:
Decision:
Status: open | resolved | deferred
```

Block completion for unresolved boundary conflicts, missing references, unknown figure mappings, missing images, unexplained duplicate passages, or any number/name mismatch.

## 10. Automated QA

QA scripts report problems; they must not silently rewrite edited Markdown. Run them after each repair.

### File and link checks

Check that:

- all expected raw chapter PDFs exist;
- recorded PDF page counts equal inclusive ranges;
- every Markdown link resolves;
- every image target exists;
- English and Chinese image references point to the same extracted asset;
- no source file links to a temporary `work/` file;
- no output contains unresolved placeholders such as `TODO`, `TBD`, `[IMAGE]`, or `???` unless whitelisted.

### Structure checks

Compare English and Chinese chapter pairs for:

- heading sequence and levels;
- paragraph/block count within justified tolerances;
- ordered list and table counts;
- figure number sequence;
- reference count and order;
- balanced `<div align="center">` and `</div>` tags;
- matching figure positions.

Chinese punctuation and paragraph wrapping may differ, so do not demand identical character counts.

### Figure checks

Extract figure numbers from captions, not filenames. Check:

- no missing or duplicated formal figure number;
- figure numbers agree with the chapter's List of Figures and body references;
- every formal figure has one complete English caption and one Chinese caption;
- all image files in links exist;
- excluded objects have a documented reason;
- no image has been edited or replaced by a generated approximation.

### Duplicate-text checks

Normalize whitespace and compare long paragraph windows or hashes. Detect:

- accidental duplicated paragraphs;
- repeated page extraction blocks;
- duplicated chapter openings;
- duplicated references.

Maintain a whitelist for intentional repetitions such as running titles, contents entries, or a source passage that is genuinely repeated. Do not delete a duplicate automatically; inspect the PDF first.

### Numeric and named-entity checks

Extract and compare English/Chinese occurrences of:

- years;
- decimal numbers and percentages;
- frequencies and units;
- processor/chip/model identifiers;
- figure/table/reference numbers;
- URLs and DOI-like identifiers;
- common company and product names.

Differences require review, not automatic normalization.

## 11. Manual QA

For every chapter, perform two separate comparisons:

### PDF → English

Review page by page, especially:

- first and last pages;
- every page with a heading;
- page breaks inside paragraphs;
- every figure and caption;
- every table, quotation, footnote, and reference;
- pages with columns or unusual layout;
- ligatures, superscripts, symbols, and URLs.

### English → Chinese

Review block by block for:

- no omitted or repeated material;
- faithful meaning and scope;
- consistent terminology and names;
- exact numbers, units, years, models, and citation markers;
- translated captions with unchanged figure numbers;
- translator notes clearly marked;
- no invented headings;
- no unmarked additions.

Render Markdown and inspect the actual appearance of centered figures, captions, tables, blockquotes, and footnotes. A file that is valid Markdown can still be structurally wrong.

## 12. Idempotency, checkpoints, and recovery

Before running a script:

1. read the current manifest and status;
2. check whether the output exists;
3. compare source hash and parameters;
4. refuse to overwrite an edited deliverable without an explicit backup/approval;
5. write a log of command, inputs, outputs, and status.

Keep Git checkpoints at sensible boundaries:

- initial structure and inventory;
- chapter boundary manifest;
- each raw-PDF batch;
- English reconstruction for a chapter;
- verified figure mapping;
- Chinese translation and QA for a chapter;
- whole-book consistency pass.

Do not commit the copyrighted PDF or large extracted assets unless authorized and intentionally configured. Use `.gitignore` for private source and reproducible `work/` artifacts as appropriate, but do not ignore manifests, logs, or issue decisions needed to reproduce the work.

If a command fails:

- preserve stdout/stderr in `work/logs/`;
- do not mark the state complete;
- fix the narrow cause;
- rerun from the last verified state;
- compare hashes and counts before accepting regenerated output.

Known operational hazards:

- Windows console encoding can fail on ligatures such as `ﬁ`; use UTF-8 output.
- PyMuPDF ranges use zero-based page indices.
- shell one-liners containing nested quotes/newlines are fragile; prefer checked `.py` scripts or heredocs.
- an image object's extraction order is not figure order.
- contact sheets are for review only, not final assets.

## 13. Whole-book consistency and final assembly

After all chapters pass individually, run a whole-book pass for:

- terminology and personal-name consistency;
- company/product/chip naming;
- abbreviation expansion policy;
- heading hierarchy and chapter titles;
- figure and table numbering;
- cross-references;
- reference formatting;
- translator-note style;
- metadata and printed-page conventions;
- broken links and temporary paths;
- duplicate passages across chapter boundaries;
- Markdown rendering.

Keep chapter files as the canonical editing sources. If a merged output is needed, generate it from the verified chapter manifest in order; do not manually concatenate random working files. Put merged English and Chinese products in `dist/` and record the source chapter hashes used to build them.

Before merging, make explicit project decisions for:

- whether front matter, contents, lists, and index are translated;
- whether printed-page audit markers remain in the public Markdown;
- how the index is represented in Markdown;
- whether references retain original English titles or receive Chinese titles in notes;
- whether figures are distributed at all under the applicable rights.

Codex must not invent these policy decisions during the final assembly.

## 14. Per-chapter completion checklist

Do not mark `complete` until every item is true:

- [ ] canonical source hash recorded;
- [ ] chapter boundary confirmed by bookmarks, labels, visible headings, and first/last page review;
- [ ] independent raw PDF exists and has the expected page count;
- [ ] working text extracted and anomalies logged;
- [ ] English Markdown metadata is present and accurate;
- [ ] source headings and hierarchy verified;
- [ ] paragraphs, lists, quotations, tables, footnotes, and references preserved;
- [ ] all figures identified and mapped with evidence;
- [ ] decorative/excluded image objects documented;
- [ ] complete English captions present;
- [ ] original image files untouched;
- [ ] English image links resolve;
- [ ] English PDF-to-Markdown review passed;
- [ ] Chinese translation follows approved English structure;
- [ ] Chinese captions are complete translations;
- [ ] English and Chinese reuse identical image assets;
- [ ] all translator additions are marked `译者注` or metadata;
- [ ] terminology and names added to/reconciled with glossaries;
- [ ] numeric/entity checks passed or exceptions logged;
- [ ] duplicate-text check passed;
- [ ] Markdown/link/HTML checks passed;
- [ ] Chinese English-to-translation review passed;
- [ ] status and issue log updated;
- [ ] checkpoint created if Git is being used.

## 15. Final-book checklist

- [ ] exactly one canonical PDF and hash are recorded;
- [ ] all PDF pages are accounted for by the unit manifest;
- [ ] all expected chapters, appendices, front matter, and index have an explicit status;
- [ ] no chapter boundary overlaps or leaves unexplained gaps;
- [ ] all formal figures and tables are accounted for;
- [ ] no image-internal translation was inserted into English source prose;
- [ ] no source heading was invented or silently merged;
- [ ] all references remain complete and ordered;
- [ ] all chapters pass automated QA;
- [ ] all chapters pass manual PDF→English and English→Chinese review;
- [ ] whole-book glossary consistency pass is complete;
- [ ] no stale or contradictory notes are carried forward;
- [ ] no temporary paths or placeholders remain in deliverables;
- [ ] merged outputs, if any, are reproducibly generated from verified chapters;
- [ ] copyright and distribution permissions are documented before release.

## 16. Codex operating loop

At the beginning of every session, Codex should:

1. read `notes/source-inventory.json`, chapter status, glossaries, and open issues;
2. select the lowest-numbered unit that is not blocked;
3. inspect its current state and never redo verified manual work without reason;
4. perform only the next state transition;
5. run the relevant automated checks;
6. perform or schedule the required visual/manual review;
7. update the manifest, status, logs, and issue notes;
8. create a checkpoint;
9. report exact files changed, checks run, unresolved issues, and the next safe state.

When evidence is insufficient, stop that item and record the evidence needed. Do not guess a heading, page boundary, figure mapping, name, number, or historical fact merely to keep the pipeline moving.
