#!/usr/bin/env python3
"""Extract readable text from source files into .tmp/extracted/.

Usage:
    python3 execution/extract_text.py <file-or-directory> [more files...]

Supports: .pdf (needs pymupdf: pip install pymupdf), .html/.htm, .docx,
.pptx, .txt/.md. Output: .tmp/extracted/<name>.txt, one per input file.
Deterministic: same input always yields the same output.
"""
import html
import re
import sys
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = REPO_ROOT / ".tmp" / "extracted"


def extract_pdf(path: Path) -> str:
    try:
        import fitz  # pymupdf
    except ImportError:
        sys.exit("PDF extraction needs pymupdf: pip install pymupdf")
    doc = fitz.open(path)
    parts = []
    for i, page in enumerate(doc):
        text = page.get_text().strip()
        parts.append(f"--- page {i + 1} ---\n{text}")
    return "\n\n".join(parts)


def extract_html(path: Path) -> str:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    raw = re.sub(r"<(script|style)[\s\S]*?</\1>", " ", raw, flags=re.I)
    text = html.unescape(re.sub(r"<[^>]+>", "\n", raw))
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return "\n".join(lines)


def _xml_to_text(xml: str) -> str:
    # Word/PowerPoint store text in <w:t>/<a:t> runs; paragraph tags become breaks.
    xml = re.sub(r"</(w:p|a:p)>", "\n", xml)
    text = html.unescape(re.sub(r"<[^>]+>", "", xml))
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return "\n".join(lines)


def extract_docx(path: Path) -> str:
    with zipfile.ZipFile(path) as z:
        return _xml_to_text(z.read("word/document.xml").decode("utf-8", "ignore"))


def extract_pptx(path: Path) -> str:
    parts = []
    with zipfile.ZipFile(path) as z:
        slides = sorted(
            (n for n in z.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)),
            key=lambda n: int(re.search(r"\d+", n).group()),
        )
        for i, name in enumerate(slides):
            body = _xml_to_text(z.read(name).decode("utf-8", "ignore"))
            parts.append(f"--- slide {i + 1} ---\n{body}")
    return "\n\n".join(parts)


HANDLERS = {
    ".pdf": extract_pdf,
    ".html": extract_html,
    ".htm": extract_html,
    ".docx": extract_docx,
    ".pptx": extract_pptx,
    ".txt": lambda p: p.read_text(encoding="utf-8", errors="ignore"),
    ".md": lambda p: p.read_text(encoding="utf-8", errors="ignore"),
}


def main(args: list[str]) -> None:
    if not args:
        sys.exit(__doc__)
    files: list[Path] = []
    for arg in args:
        p = Path(arg)
        if p.is_dir():
            files += [f for f in sorted(p.rglob("*")) if f.suffix.lower() in HANDLERS]
        else:
            files.append(p)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for f in files:
        handler = HANDLERS.get(f.suffix.lower())
        if not handler:
            print(f"SKIP (unsupported {f.suffix}): {f}")
            continue
        if not f.exists():
            print(f"SKIP (missing): {f}")
            continue
        out = OUT_DIR / (f.stem.strip().replace(" ", "_") + ".txt")
        text = handler(f)
        out.write_text(text, encoding="utf-8")
        status = "OK " if len(text) > 200 else "THIN (little text — scanned/image file?)"
        print(f"{status} {f.name} -> {out.relative_to(REPO_ROOT)} ({len(text)} chars)")


if __name__ == "__main__":
    main(sys.argv[1:])
