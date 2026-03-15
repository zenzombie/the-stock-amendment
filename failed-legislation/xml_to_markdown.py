#!/usr/bin/env python3
import argparse
import re
import xml.etree.ElementTree as ET
from pathlib import Path

BLOCK_TAGS = {
    "subsection",
    "paragraph",
    "subparagraph",
    "clause",
    "subclause",
    "item",
    "subitem",
}


def norm_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def local_name(tag: str) -> str:
    if "}" in tag:
        return tag.split("}", 1)[1]
    return tag


def child_text(elem: ET.Element, name: str) -> str:
    for c in elem:
        if local_name(c.tag) == name:
            return norm_ws("".join(c.itertext()))
    return ""


def is_deleted(elem: ET.Element) -> bool:
    return elem.attrib.get("changed") == "deleted"


def has_added_content(body: ET.Element) -> bool:
    for e in body.iter():
        if local_name(e.tag) == "section" and e.attrib.get("changed") == "added":
            return True
    return False


def choose_legis_body(root: ET.Element) -> ET.Element:
    bodies = [e for e in root if local_name(e.tag) == "legis-body"]
    if not bodies:
        raise ValueError("No legis-body found in XML.")

    for b in bodies:
        if has_added_content(b):
            return b
    return bodies[0]


def text_with_quotes(elem: ET.Element) -> str:
    parts = []

    def walk(n: ET.Element):
        if n.text:
            parts.append(n.text)
        for c in n:
            lname = local_name(c.tag)
            if lname == "quote":
                q = norm_ws("".join(c.itertext()))
                if q:
                    parts.append(f'"{q}"')
            else:
                walk(c)
            if c.tail:
                parts.append(c.tail)

    walk(elem)
    return norm_ws("".join(parts))


def list_prefix(depth: int) -> str:
    return f"{'  ' * depth}- "


def emit_block_line(node: ET.Element, lines: list[str], depth: int = 0):
    if is_deleted(node):
        return

    enum = child_text(node, "enum")
    header = child_text(node, "header")

    text_parts = []
    for c in node:
        if local_name(c.tag) == "text":
            t = text_with_quotes(c)
            if t:
                text_parts.append(t)
    text = norm_ws(" ".join(text_parts))

    lhs = enum if enum else ""
    if header and text:
        line = f"{lhs} {header}.--{text}".strip()
    elif header:
        line = f"{lhs} {header}".strip()
    elif text:
        line = f"{lhs} {text}".strip()
    else:
        line = lhs.strip()

    if line:
        if depth == 0 and lines and lines[-1] != "":
            lines.append("")
        lines.append(f"{list_prefix(depth)}{line}")

    for c in node:
        lname = local_name(c.tag)
        if lname in BLOCK_TAGS:
            emit_block_line(c, lines, depth + 1)
        elif lname == "quoted-block":
            emit_quoted_block(c, lines, depth + 1)
        elif lname == "toc":
            for te in c:
                if local_name(te.tag) == "toc-entry":
                    t = norm_ws("".join(te.itertext()))
                    if t:
                        lines.append(f"{list_prefix(depth + 1)}{t}")


def emit_usc_subchapter(subchapter: ET.Element, lines: list[str]):
    if is_deleted(subchapter):
        return

    enum = child_text(subchapter, "enum")
    header = child_text(subchapter, "header")
    if enum and header:
        lines.append(f"### Subchapter {enum}--{header}")
    elif header:
        lines.append(f"### {header}")

    for sec in subchapter:
        if local_name(sec.tag) != "section" or is_deleted(sec):
            continue
        sec_enum = child_text(sec, "enum")
        sec_header = child_text(sec, "header")
        if sec_enum and sec_header:
            lines.append(f"#### Sec. {sec_enum} {sec_header}")
        elif sec_header:
            lines.append(f"#### {sec_header}")

        for c in sec:
            lname = local_name(c.tag)
            if lname == "text":
                t = text_with_quotes(c)
                if t:
                    lines.append(t)
            elif lname in BLOCK_TAGS:
                emit_block_line(c, lines)
            elif lname == "quoted-block":
                emit_quoted_block(c, lines)


def emit_quoted_block(qb: ET.Element, lines: list[str], depth: int = 0):
    if is_deleted(qb):
        return

    emitted_any = False
    for c in qb:
        lname = local_name(c.tag)
        if lname == "subchapter":
            emit_usc_subchapter(c, lines)
            emitted_any = True
        elif lname == "toc":
            for te in c:
                if local_name(te.tag) == "toc-entry":
                    t = norm_ws("".join(te.itertext()))
                    if t:
                        lines.append(f"{list_prefix(depth)}{t}")
            emitted_any = True
        elif lname in BLOCK_TAGS:
            emit_block_line(c, lines, depth)
            emitted_any = True
        elif lname == "section":
            if is_deleted(c):
                continue
            enum = child_text(c, "enum")
            header = child_text(c, "header")
            if enum and header:
                lines.append(f"#### Sec. {enum} {header}")
            elif header:
                lines.append(f"#### {header}")
            for gc in c:
                gname = local_name(gc.tag)
                if gname == "text":
                    t = text_with_quotes(gc)
                    if t:
                        lines.append(t)
                elif gname in BLOCK_TAGS:
                    emit_block_line(gc, lines, depth)
            emitted_any = True

    if not emitted_any:
        t = norm_ws("".join(qb.itertext()))
        if t:
            lines.append(t)


def section_to_markdown(section: ET.Element, lines: list[str]):
    if is_deleted(section):
        return

    enum = child_text(section, "enum")
    header = child_text(section, "header")
    if enum and header:
        lines.append(f"# SECTION {enum} {header.upper()}.")
    elif header:
        lines.append(f"# {header}")
    lines.append("")

    for c in section:
        lname = local_name(c.tag)
        if lname == "text":
            t = text_with_quotes(c)
            if t:
                lines.append(t)
                lines.append("")
        elif lname == "subsection":
            enum2 = child_text(c, "enum")
            header2 = child_text(c, "header")
            text_parts = []
            for gc in c:
                if local_name(gc.tag) == "text":
                    tt = text_with_quotes(gc)
                    if tt:
                        text_parts.append(tt)
            intro = norm_ws(" ".join(text_parts))
            if enum2 and header2 and intro:
                lines.append(f"{enum2} {header2}.--{intro}")
            elif enum2 and intro:
                lines.append(f"{enum2} {intro}")
            elif intro:
                lines.append(intro)
            lines.append("")

            for gc in c:
                gname = local_name(gc.tag)
                if gname in BLOCK_TAGS:
                    emit_block_line(gc, lines)
                elif gname == "quoted-block":
                    emit_quoted_block(gc, lines)
            lines.append("")


def convert_xml(xml_path: Path, out_path: Path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    body = choose_legis_body(root)

    lines: list[str] = []
    for c in body:
        if local_name(c.tag) == "section":
            section_to_markdown(c, lines)

    cleaned = []
    blank = 0
    for ln in lines:
        t = ln.rstrip()
        if not t:
            blank += 1
            if blank <= 1:
                cleaned.append("")
        else:
            blank = 0
            cleaned.append(t)

    out_path.write_text("\n".join(cleaned).strip() + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Convert congressional bill XML to clean Markdown.")
    parser.add_argument("inputs", nargs="*", help="XML file paths. If omitted, convert all *.xml in script directory.")
    args = parser.parse_args()

    base = Path(__file__).resolve().parent
    if args.inputs:
        xml_files = [Path(p).resolve() for p in args.inputs]
    else:
        xml_files = sorted(base.glob("*.xml"))

    if not xml_files:
        raise SystemExit("No XML files found.")

    for xml_file in xml_files:
        out_file = xml_file.with_suffix("").with_name(xml_file.stem + "-clean.md")
        convert_xml(xml_file, out_file)
        print(f"Wrote: {out_file}")


if __name__ == "__main__":
    main()
