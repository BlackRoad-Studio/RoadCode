# BlackRoad-Studio RoadCode

Canonical RoadCode workspace and automation hub for BlackRoad-Studio.

## What Lives Here

- RoadCode landing page and deploy surface
- org-specific operator workflows
- automation entrypoints for GitHub, Gitea, Slack, and Cloudflare

## Deploy

This repo ships a static site from site/ to both GitHub Pages and Cloudflare Pages.

- GitHub Pages URL: https://blackroad-studio.github.io/RoadCode/
- Cloudflare Pages URL: https://blackroad-studio-roadcode.pages.dev
- Expected Cloudflare project name: blackroad-studio-roadcode

## Operator Notes

- Default branch: main
- GitHub Pages workflow: .github/workflows/github-pages.yml
- Workflow: .github/workflows/roadcode-pages.yml
- Site entrypoint: site/index.html
