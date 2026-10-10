# Usage

```powershell
python scripts/publish_post.py <src> [--blog-dir DIR] [--slug S] [--date D] [--categories "[A, B]"] [--tags "[x]"] [--force] [--dry-run] [--push]
```

`<src>` is a file or a directory (non-recursive, `*.md`). `--blog-dir` defaults to the repository root (resolved from the script location).

## What it does

| Step | Rule |
| --- | --- |
| Title | Front Matter `title`, else first H1 (removed from body, theme renders it), else filename |
| Date | `--date`, else Front Matter, else file mtime (+0800) |
| File name | `_posts/YYYY-MM-DD-slug.md`; slug from ASCII filename, else `post-<hash>` (use `--slug` for readable URLs) |
| Categories/tags | Args > Front Matter > `[随记]` / `[]`; must be `[a, b]` form |
| Math / Mermaid | `math: true` if `$..$`/`$$` outside code fences; `mermaid: true` if a mermaid fence exists |
| Images | Local `![](x)` and `<img src>` copied to `assets/img/posts/<slug>/`, links rewritten to `/assets/img/posts/<slug>/<name>`; remote URLs untouched; missing files give `[WARN]` |
| Other Front Matter keys | Preserved |
| Push | `git add -A`, commit `新增文章:<slug>`, push |

## Limitations

- Same-named images from different folders collide (last wins).
- Multi-line Front Matter lists for title/categories/tags are not parsed; use `[a, b]` single-line.
- Word/PDF must be converted to Markdown first (e.g. `pandoc x.docx -o x.md --extract-media=./media`).
- Images are not compressed; keep each under ~500KB.
- Wiki-links (`[[x]]`) and Obsidian callouts are not converted.
