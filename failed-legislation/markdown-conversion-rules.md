# Markdown Conversion Rules for Bill Text Files

This document defines the canonical rules for converting bill text files (TXT) into clean, TOC-friendly Markdown while preserving legal text content.

## 1) Source and Version Rules

1. Use the most advanced available bill version.
1. Version priority:
1. `ENR` (if available)
1. `ES` / `EAS` (if available)
1. `RS` / `RH` (reported versions)
1. `IS` / `IH` (introduced versions)
1. Prefer official GovInfo bill text sources.
1. Keep the source version code in the output filename.

## 2) Input File Rules

1. Input TXT should be plain bill text from official sources.
1. If source contains markup tags (for example `<DELETED>...</DELETED>`), treat those as editorial/markup metadata, not final legal text.
1. Never mix commentary or analysis into the converted bill Markdown file.

## 3) Final-Text Selection Rules

1. Keep only operative final text.
1. For reported documents with strike/insert markup:
1. Remove all deleted blocks (`<DELETED>...</DELETED>`).
1. Keep replacement text that remains after deleted content.
1. Start content at the first operative section heading (typically `SECTION 1. SHORT TITLE.`).
1. Remove trailing publication artifacts (calendar blocks, `<all>`, repeated cover pages, footer metadata).

## 4) Markdown Structure Rules

1. Preserve paragraph content and legal wording.
1. Convert hierarchy anchors into Markdown headings to enable TOC generation.
1. Heading mapping:
1. `SECTION X. ...` -> H1 (`#`)
1. `SEC. X. ...` -> H2 (`##`)
1. `Subchapter ...` line -> H3 (`###`)
1. `Sec. 131xx. ...` line -> H4 (`####`)
1. Do not invent new legal headings not present in source text.
1. Keep subsection markers like `(a)`, `(1)`, `(A)`, `(i)` as body text unless a separate deeper-heading mode is explicitly requested.

## 5) Quote and Marker Normalization Rules

1. Normalize congressional quote markers for Markdown readability:
1. Replace double-backtick opener and double-apostrophe closer with standard double quote (`"`).
1. Remove stray leading quote characters at start-of-line when they are formatting artifacts.
1. Keep normal inline quoted phrases intact.
1. Keep single-apostrophe marks in words/terms unless they are clearly malformed artifacts.

## 6) Newline and Wrapping Rules

1. Join soft-wrapped lines so single sentences are not split across lines.
1. Preserve real structural breaks:
1. Blank lines
1. Markdown headings
1. Start lines for legal list items (for example lines beginning with `(a)`, `(1)`, `(A)`, `(i)`)
1. Do not merge separate list-item lines into one line.
1. Collapse accidental double/multiple spaces created during joins to single spaces.

## 7) Content Integrity Rules

1. Formatting-only conversion must not change substantive legal meaning.
1. No paraphrasing.
1. No summarization in the converted bill file.
1. No added commentary, context, or cross-bill comparisons in the converted bill file.

## 8) Filename Rules

1. Converted files should include:
1. bill identifier
1. version code
1. `-clean.md` suffix
1. Example pattern:
1. `118th-congress-s1171-ethics-act-rs-clean.md`
1. `118th-congress-s2773-ban-congressional-stock-trading-act-is-clean.md`

## 9) Validation Checklist

Before finalizing, verify all items below:

1. No `<DELETED>` blocks remain.
1. No source artifact lines remain (for example `<all>`, repeated calendar/footer blocks).
1. TOC-visible heading hierarchy exists (H1/H2/H3/H4 as applicable).
1. No stray leading quote characters at line starts.
1. Representative wrapped sentences are now single-line sentences.
1. Legal list item structure is still readable and not merged incorrectly.
1. File contains only bill text (no analysis/commentary).

## 10) Optional Modes (Only When Requested)

1. Deep TOC mode: promote `(a)`, `(1)`, `(A)`, `(i)` to deeper heading levels.
1. Strict-fidelity mode: preserve all original line breaks and indentation except required Markdown heading conversion.
1. Citation mode: keep source/version metadata header above the operative text.

## 11) Reset and Cleanup Safety Rules

1. Never run broad deletion commands (`rm *.md`, `rm *`) in `failed-legislation` without an allowlist.
1. Source refresh operations should delete only bill-source file extensions targeted for replacement.
1. Preserve documentation and analysis artifacts unless explicitly requested to remove them:
1. `failed-legislation/summary.md`
1. `failed-legislation/markdown-conversion-rules.md`
1. Safe pattern for reset:
1. Remove only old source files (for example `*.txt`) when switching to XML-first flow.
1. Download new source files.
1. Regenerate derived markdown outputs.
1. Re-verify that summary/rules files still exist after cleanup.
