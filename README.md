# codex-sandbox

This repository hosts a simple static site used for sandbox testing.

## Sitemap generation

A GitHub Actions workflow automatically scans the repository for `*.html` files
and regenerates `sitemap.xml` on every push to the default branch. The sitemap
is committed back to the repository root.

Once GitHub Pages is enabled for this repository, the sitemap will be available
at `<pages-url>/sitemap.xml`, where `<pages-url>` is the URL of the GitHub Pages
site (for most repositories this is `https://<owner>.github.io/<repo>`).

You can inspect the workflow definition in
[`.github/workflows/generate-sitemap.yml`](.github/workflows/generate-sitemap.yml).
