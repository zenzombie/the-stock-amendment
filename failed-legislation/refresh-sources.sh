#!/usr/bin/env bash
set -euo pipefail

# Safe source refresh for failed-legislation bill files.
# - Deletes only bill source/derived files we intend to replace.
# - Preserves documentation files (summary.md, markdown-conversion-rules.md).

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "Refreshing failed-legislation sources in: $SCRIPT_DIR"

# Remove only replaceable bill artifacts.
rm -f -- \
  118th-congress-s1171-ethics-act-rs.xml \
  118th-congress-s2773-ban-congressional-stock-trading-act-is.xml \
  118th-congress-s1171-ethics-act-rs.txt \
  118th-congress-s2773-ban-congressional-stock-trading-act-is.txt \
  118th-congress-s1171-ethics-act-rs-clean.md \
  118th-congress-s2773-ban-congressional-stock-trading-act-is-clean.md

# Download authoritative XML source files.
curl -fL "https://www.govinfo.gov/content/pkg/BILLS-118s1171rs/xml/BILLS-118s1171rs.xml" \
  -o "118th-congress-s1171-ethics-act-rs.xml"

curl -fL "https://www.govinfo.gov/content/pkg/BILLS-118s2773is/xml/BILLS-118s2773is.xml" \
  -o "118th-congress-s2773-ban-congressional-stock-trading-act-is.xml"

# Rebuild clean Markdown from XML sources.
[[ -f "xml_to_markdown.py" ]] || { echo "ERROR: xml_to_markdown.py is missing."; exit 1; }
python3 "xml_to_markdown.py" \
  "118th-congress-s1171-ethics-act-rs.xml" \
  "118th-congress-s2773-ban-congressional-stock-trading-act-is.xml"

# Safety check: required docs must still exist.
[[ -f "summary.md" ]] || { echo "ERROR: summary.md is missing after refresh."; exit 1; }
[[ -f "markdown-conversion-rules.md" ]] || { echo "ERROR: markdown-conversion-rules.md is missing after refresh."; exit 1; }

echo "Done. Current files:"
ls -lh
