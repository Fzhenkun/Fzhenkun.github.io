# 非鱼随记

Jekyll + Chirpy,部署于 GitHub Pages:<https://fzhenkun.github.io>

## 上线步骤

1. 在 GitHub 创建**公开**仓库 `Fzhenkun.github.io`
2. 在本目录执行:
   ```bash
   git init -b main
   git add .
   git commit -m "init blog"
   git remote add origin https://github.com/Fzhenkun/Fzhenkun.github.io.git
   git push -u origin main
   ```
3. 仓库 Settings → Pages → Source 选 **GitHub Actions**

## 日常发文

在 `_posts/` 新建 `YYYY-MM-DD-slug.md`,push 即可。公式在 Front Matter 加 `math: true`。

## 访问统计(GoatCounter)

注册 <https://www.goatcounter.com>,把站点代码填入 `_config.yml` 的 `analytics.goatcounter.id`;
需要显示阅读量时同时设置 `pageviews.provider: goatcounter`。

## 评论(预留)

`_config.yml` 的 `comments` 已保留 giscus/utterances/disqus 配置项。启用时:
开启仓库 Discussions → 在 <https://giscus.app> 获取参数 → 填入 `comments.giscus` 并设置 `comments.provider: giscus`。
