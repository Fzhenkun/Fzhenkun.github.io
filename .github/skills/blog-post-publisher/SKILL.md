---
name: blog-post-publisher
description: MUST USE when the user wants to turn local Markdown/笔记/文档 into a blog post for this Jekyll + Chirpy GitHub Pages blog (非鱼随记) and optionally publish it. Adds Front Matter (title/date/categories/tags/math), renames to YYYY-MM-DD-slug.md, copies local images to assets/img/posts and rewrites links, then git add/commit/push. 触发词:发布文章、markdown转博客、把文档放进博客、导入文档、批量导入、上传博客、发文。Do NOT use for creating a new blog site (use personal-website-builder), non-Jekyll sites, or editing the theme/config.
---

# Blog Post Publisher

Routing only. One command does the conversion: `scripts/publish_post.py`.

## Flow

1. Get the source `.md` path (or a directory) from the user; pass it verbatim.
2. Ask only what is missing: categories (max 2 levels), tags (lowercase English). Default categories is `[随记]`.
3. Preview first: `python scripts/publish_post.py "<src>" --dry-run --categories "[A, B]" --tags "[x, y]"`
4. Run without `--dry-run` and report `[WARN]` lines (missing images) to the user.
5. Publishing: only add `--push` after the user explicitly agrees; push triggers a public deployment.
6. Tell the user the post appears in 1-3 minutes at https://fzhenkun.github.io.

## Read when needed

| Need | File |
| --- | --- |
| Options, conversion rules, limitations | `references/usage.md` |
| Any `[FAIL]`, git or script error | `references/fallback.md` |
| Sample invocations | `examples/positive.md`, `examples/negative.md` |

## Hard rules

- Never edit the script to force success; on failure read `references/fallback.md` first.
- Existing posts are skipped unless the user approves `--force`.
- Never push without user approval.
- Audit before delivery (optional, if the skill-lifecycle-engine skill is installed): `python <path>\skill-lifecycle-engine\scripts\maintain_skill.py --skill-dir <this-folder>`
