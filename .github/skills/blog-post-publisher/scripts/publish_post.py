#!/usr/bin/env python3
"""Convert local Markdown into a Jekyll/Chirpy post, copy images, optionally git push."""
import argparse
import datetime as dt
import hashlib
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote, unquote

DEFAULT_BLOG = str(Path(__file__).resolve().parents[4])  # <repo>/.github/skills/<name>/scripts/
IMG_MD = re.compile(r'(!\[[^\]]*\]\()(<[^>]+>|[^)\s]+)((?:\s+"[^"]*")?\))')
IMG_HTML = re.compile(r'(<img\b[^>]*?\bsrc=["\'])([^"\']+)(["\'])', re.I)
FENCE = re.compile(r"^\s*(```|~~~)")


def split_front_matter(text):
    if text.startswith("---"):
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.S)
        if m:
            return m.group(1), text[m.end():]
    return "", text


def parse_fm(raw):
    fm, extra = {}, []
    for line in raw.splitlines():
        m = re.match(r"^(title|date|categories|tags|math|mermaid):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
        elif line.strip():
            extra.append(line)
    return fm, extra


def make_slug(name):
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    if len(s) >= 3:
        return s[:60]
    return "post-" + hashlib.md5(name.encode("utf-8")).hexdigest()[:6]


def is_remote(p):
    return re.match(r"^(https?:|data:|//|/|#)", p) is not None


def convert(src, blog, args):
    text = src.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    raw_fm, body = split_front_matter(text)
    fm, extra = parse_fm(raw_fm)

    title = fm.get("title", "").strip("\"'")
    in_fence, out, h1_done = False, [], False
    for line in body.split("\n"):
        if FENCE.match(line):
            in_fence = not in_fence
        # The theme renders the title itself, so drop the first H1.
        if not in_fence and not h1_done and re.match(r"^# +\S", line):
            h1_done = True
            if not title:
                title = line[2:].strip()
            if line[2:].strip() == title:
                continue
        out.append(line)
    title = title or src.stem

    date_str = args.date or fm.get("date")
    if not date_str:
        date_str = dt.datetime.fromtimestamp(src.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S +0800")
    elif re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_str):
        date_str += " 12:00:00 +0800"
    day = date_str[:10]
    slug = args.slug or make_slug(src.stem)

    img_dir = blog / "assets" / "img" / "posts" / slug
    copied, missing = [], []

    def fix(path_str):
        p = path_str.strip("<>")
        if is_remote(p):
            return path_str
        cand = Path(unquote(p))
        if not cand.is_absolute():
            cand = src.parent / cand
        if not cand.is_file():
            missing.append(p)
            return path_str
        if not args.dry_run:
            img_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(cand, img_dir / cand.name)
        copied.append(cand.name)
        return f"/assets/img/posts/{slug}/{quote(cand.name)}"

    in_fence, res = False, []
    for line in out:
        if FENCE.match(line):
            in_fence = not in_fence
        if not in_fence:
            line = IMG_MD.sub(lambda m: m.group(1) + fix(m.group(2)) + m.group(3), line)
            line = IMG_HTML.sub(lambda m: m.group(1) + fix(m.group(2)) + m.group(3), line)
        res.append(line)
    body_out = "\n".join(res).lstrip("\n")

    cats = args.categories or fm.get("categories") or "[随记]"
    tags = args.tags or fm.get("tags") or "[]"
    for v in (cats, tags):
        if not v.startswith("["):
            sys.exit(f"[FAIL] categories/tags must look like [a, b]: {v}")

    head = ["---", f"title: {title}", f"date: {date_str}", f"categories: {cats}", f"tags: {tags}"]
    stripped = re.sub(r"```.*?```", "", body_out, flags=re.S)
    if fm.get("math") or re.search(r"\$\$|(?<![\\$])\$[^$\n]+\$", stripped):
        head.append("math: true")
    if fm.get("mermaid") or re.search(r"^```mermaid", body_out, re.M):
        head.append("mermaid: true")
    head += extra + ["---", ""]
    target = blog / "_posts" / f"{day}-{slug}.md"
    return target, "\n".join(head) + "\n" + body_out.rstrip("\n") + "\n", copied, missing


def git(blog, *a):
    r = subprocess.run(["git", "-C", str(blog), *a], capture_output=True, text=True)
    print(r.stdout + r.stderr, end="")
    if r.returncode:
        sys.exit(f"[FAIL] git {' '.join(a)} exited {r.returncode}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("src", help="a .md file or a directory of .md files")
    ap.add_argument("--blog-dir", default=DEFAULT_BLOG)
    ap.add_argument("--slug")
    ap.add_argument("--date", help="YYYY-MM-DD or full datetime")
    ap.add_argument("--categories", help='e.g. "[C++, 编译优化]"')
    ap.add_argument("--tags", help='e.g. "[cpp, build]"')
    ap.add_argument("--force", action="store_true", help="overwrite existing post")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--push", action="store_true", help="git add/commit/push (needs user approval)")
    args = ap.parse_args()

    blog = Path(args.blog_dir)
    if not (blog / "_config.yml").is_file():
        sys.exit(f"[FAIL] not a Jekyll blog dir: {blog}")
    src = Path(args.src)
    files = sorted(src.glob("*.md")) if src.is_dir() else [src]
    if not files or not all(f.is_file() for f in files):
        sys.exit(f"[FAIL] no markdown found: {src}")
    if len(files) > 1 and args.slug:
        sys.exit("[FAIL] --slug only valid for a single file")

    written = []
    for f in files:
        target, content, copied, missing = convert(f, blog, args)
        if target.exists() and not args.force:
            print(f"[SKIP] exists (use --force): {target}")
            continue
        print(f"[OK] {f.name} -> {target.name}; images copied: {len(copied)}")
        for m in missing:
            print(f"[WARN] image not found: {m}")
        if not args.dry_run:
            target.write_text(content, encoding="utf-8", newline="\n")
            written.append(target)

    if args.push and written and not args.dry_run:
        git(blog, "add", "-A")
        git(blog, "commit", "-m", f"新增文章:{', '.join(p.stem[11:] for p in written)}")
        git(blog, "push")
        print("[OK] pushed; Actions will deploy in 1-3 minutes")


if __name__ == "__main__":
    main()
