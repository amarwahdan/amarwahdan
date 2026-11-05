# Profile Design and Maintenance

[Back to profile](../README.md)

## What is interactive

The README combines clickable project cards, native `<details>/<summary>` disclosure controls, GitHub-rendered Mermaid diagrams, and links to actual notebooks, writeups, repositories, and artifacts. Opening an engineering brief reveals its data flow; the Architecture Spec expands the source and evaluation context.

GitHub does not execute arbitrary JavaScript in a README. The visual system therefore uses self-contained SVG animation and supported Markdown/HTML—not nonfunctional web-app controls or fake inference dashboards. No SVG animation represents live latency, system uptime, or model output.

## Visual sources

- `assets/header.svg`, `assets/footer.svg`: animated identity assets.
- `assets/tech-pipeline.svg`: animated, deterministic capability graph.
- `assets/source/tech-pipeline.mmd`: the pipeline's structured topology.
- `assets/source/cards.json`: project facts, numeric labels, diagrams, and original links.
- `assets/source/*.html`: editable HTML/CSS layouts for exact-information project cards.
- `assets/*-card.png`: rendered card images used by the README.
- `assets/source/profile-intro.md` and `profile-outro.md`: editable profile copy.
- `docs/projects/*.md`: generated architecture briefs.

SVG assets include decorative-motion suppression for viewers preferring reduced motion. The name, meaning, and project facts remain visible without animation. Cards have descriptive alternative text, and core details remain available as Markdown.

## Rebuild

Run from the repository root:

```bash
python3 tools/build_readme.py
python3 tools/render_profile.py
```

The README/document generator uses only the Python standard library. Card rendering additionally requires Playwright and Chromium. The renderer uses `/usr/bin/chromium`; adjust that executable path for a different environment. Cards are rendered at double pixel density from a flow-layout HTML container.

Edit source files before rebuilding so content and visuals stay synchronized. Source-controlled HTML is a static asset layout, not a hosted application. Generated pages and images must not include private repository content or personal records beyond the intentionally public profile summary.

## Content discipline

Use scoped metrics: distinguish performance, regression coverage, dataset scale, architecture scope, and historical status. Keep #34 WiDS explicitly tied to the Public Leaderboard; it is not a final ranking. Do not label a notebook, video, or expired session as an always-on live demo. Mooox-Agent source remains private. Smart Healthmeror is a past implemented project that is no longer running; do not invent its stack or active endpoint.

Upstream release badges and GitHub commit badges are provider-fetched data and may be cached. Existing contribution-snake automation is left unchanged; no new scheduled automation is installed by this redesign.
