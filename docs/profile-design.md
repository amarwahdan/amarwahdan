# Visual README + Interactive AI Portfolio

The README is a visual gateway, not an embedded web application. Its cover, recorded GIF demonstrations, and buttons open the real portfolio. GitHub does not execute custom JavaScript or hover CSS inside README images.

The live portfolio provides hover/focus/tap project-stack reveals, active technology connections, pointer effects, magnetic links, project filtering, horizontal gallery controls, keyboard interaction, and reduced motion. Main-page copy is deliberately brief; full project evidence lives on separate pages and in `docs/projects/`.

## Update the README

Edit `assets/source/visual-readme.md`, then run:

```bash
python3 tools/build_visual_readme.py
```

To refresh the cover and GIF demonstrations from the actual published interface:

```bash
python3 tools/capture_visual_gateway.py https://amarai-jzurfwqv.manus.space
```

The website source is in `portfolio/`. `portfolio/src/data/projects.json` retains the reviewed project facts. The website is hosted separately; rebuilding README does not change project implementations or publish the website.

The previous `tools/build_readme.py` and `tools/render_profile.py` belong to the earlier documentation-heavy design. They are retained as historical source, not the current build path. Do not use them to regenerate the current README.

Mooox-Agent source remains private. Smart Healthmeror remains inactive without an invented stack. #34 refers to the Public Leaderboard, not the final/private rank. Project-metric scope stays in the linked briefs.
