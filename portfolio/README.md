# Amar AI — Interactive Portfolio

A static, progressively enhanced portfolio for **Amar Ahmed Hamed, AI Engineer / Machine Learning Engineer**. The homepage is deliberately visual and concise. Hover, keyboard focus, and tap reveal project stacks; technology icons activate illustrative AI interactions and expose documented project connections. Detailed engineering information is on separate pages.

## Source structure

`src/index.html` contains the homepage layout. `src/styles.css` defines the visual system, responsive layouts, and hover/reduced-motion behavior. `src/app.js` implements pointer effects, project-stack reveals, filtering, rail navigation, tool connections, and the motion preference. `src/data/projects.json` is the reviewed project-content source. `tools/visual_data.py` defines tool metadata and source-controlled project glyphs. `tools/build_site.py` generates the content-bearing static pages in `site/`. `public/assets/` contains the actual brand icons and original monogram.

## Rebuild and run

```bash
python3 tools/build_site.py
python3 -m http.server 3000 --bind 0.0.0.0 --directory site
```

The generated `site/` directory is committed for deterministic static publication. No Node dependencies, API keys, backend, database, or live model calls are required. Asset URLs beginning with `/manus-storage/` are served by the managed website origin, not the plain local Python server.

The visual AI capability signatures are illustrative interface effects, not live inference or fabricated performance telemetry. No source code or features of the original showcased projects are modified. The private Mooox-Agent source and full personal attachments are not included.

The primary deployment uses Manus-managed hosting. The GitHub profile links to the published origin. When serving this source elsewhere, the hero asset must be exported from the managed origin or replaced with its authorized local copy.
