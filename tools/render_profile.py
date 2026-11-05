#!/usr/bin/env python3
"""Build source-controlled README visuals; never simulates model telemetry.

Run from the repository root: python3 tools/render_profile.py
Requires Playwright and a Chromium browser for the HTML-rendered project cards.
"""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
SOURCE = ASSETS / 'source'
SOURCE.mkdir(parents=True, exist_ok=True)

HEADER = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="360" viewBox="0 0 1200 360" role="img" aria-labelledby="title desc">
<title id="title">Amar Ahmed Hamed — AI Engineer / Machine Learning Engineer</title>
<desc id="desc">An animated neural-system identity in cyan and violet. Decorative animation, not live inference.</desc>
<defs>
 <linearGradient id="bg" x2="1" y2="1"><stop stop-color="#070D19"/><stop offset="1" stop-color="#15102D"/></linearGradient>
 <linearGradient id="edge"><stop stop-color="#43E8E1"/><stop offset="1" stop-color="#A78BFA"/></linearGradient>
 <radialGradient id="halo"><stop stop-color="#624DB7" stop-opacity=".3"/><stop offset="1" stop-color="#624DB7" stop-opacity="0"/></radialGradient>
 <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#9AABCE" stroke-opacity=".055"/></pattern>
</defs>
<style>.mono{font-family:ui-monospace,Consolas,monospace}.sans{font-family:Arial,Helvetica,sans-serif}@media(prefers-reduced-motion:reduce){.motion{display:none}}</style>
<rect x="1" y="1" width="1198" height="358" rx="22" fill="url(#bg)" stroke="#26334D"/>
<rect x="2" y="2" width="1196" height="356" rx="22" fill="url(#grid)"/>
<path d="M24 1H1176" stroke="url(#edge)" stroke-width="2"/>
<circle cx="992" cy="180" r="190" fill="url(#halo)"/>
<g class="mono" font-size="13" letter-spacing="2"><text x="54" y="43" fill="#43E8E1">AMAR / INTELLIGENT SYSTEMS</text><text x="54" y="313" fill="#8C9DBD">RESEARCH DEPTH</text><text x="279" y="313" fill="#8C9DBD">SYSTEM DESIGN</text><text x="494" y="313" fill="#8C9DBD">EVIDENCE FIRST</text></g>
<g class="sans"><text x="52" y="130" fill="#EFF5FF" font-size="57" font-weight="700" letter-spacing="-1.7">Amar Ahmed Hamed</text><text x="55" y="179" fill="#43E8E1" font-size="24">AI Engineer / Machine Learning Engineer</text><text x="55" y="220" fill="#B6C3DB" font-size="18">Agentic workflows. Visual intelligence. Model-based planning.</text><text x="55" y="247" fill="#B6C3DB" font-size="18">From research questions to inspectable AI systems.</text></g>
<path d="M54 280H694" stroke="#283550"/>
<g fill="none" stroke="url(#edge)"><circle cx="991" cy="180" r="111" opacity=".65"/><circle cx="991" cy="180" r="131" stroke-dasharray="4 12" opacity=".45"/>
<circle class="motion" cx="991" cy="180" r="111" stroke-width="3" stroke-dasharray="70 628"><animateTransform attributeName="transform" type="rotate" from="0 991 180" to="360 991 180" dur="18s" repeatCount="indefinite"/></circle>
<path d="M916 141L970 110L1043 143L1064 211L1001 249L933 211Z M916 141L991 180L1043 143 M970 110L991 180L1001 249 M933 211L991 180L1064 211" stroke-opacity=".65"/>
</g>
<g fill="#43E8E1"><circle cx="916" cy="141" r="5"/><circle cx="970" cy="110" r="5"/><circle cx="1043" cy="143" r="5"/><circle cx="1064" cy="211" r="5"/><circle cx="1001" cy="249" r="5"/><circle cx="933" cy="211" r="5"/><circle cx="991" cy="180" r="12"/></g>
<circle class="motion" cx="991" cy="180" r="20" fill="none" stroke="#A78BFA" opacity=".7"><animate attributeName="r" values="18;32;18" dur="5s" repeatCount="indefinite"/><animate attributeName="opacity" values=".7;.1;.7" dur="5s" repeatCount="indefinite"/></circle>
<text x="991" y="345" text-anchor="middle" class="mono" fill="#8C9DBD" font-size="11" letter-spacing="2">AGENTS / VISION / RL</text>
</svg>
'''

FOOTER = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="150" viewBox="0 0 1200 150" role="img" aria-labelledby="title">
<title id="title">Think in systems. Build with evidence. Amar Ahmed Hamed.</title>
<defs><linearGradient id="bg"><stop stop-color="#08111E"/><stop offset="1" stop-color="#15102D"/></linearGradient><linearGradient id="line"><stop stop-color="#43E8E1"/><stop offset="1" stop-color="#A78BFA"/></linearGradient></defs>
<style>@media(prefers-reduced-motion:reduce){.motion{display:none}}</style>
<rect x="1" y="1" width="1198" height="148" rx="18" fill="url(#bg)" stroke="#26334D"/>
<path d="M45 26H1155" stroke="url(#line)" opacity=".4"/>
<circle class="motion" r="3" fill="#43E8E1"><animateMotion dur="12s" repeatCount="indefinite" path="M45 26H1155"/></circle>
<text x="600" y="76" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="26" font-weight="700" fill="#EFF5FF">Think in systems. Build with evidence.</text>
<text x="600" y="111" text-anchor="middle" font-family="Consolas,monospace" font-size="13" letter-spacing="2" fill="#94A7C7">AMAR AHMED HAMED / AI ENGINEERING</text>
</svg>
'''

PIPELINE_SOURCE = '''flowchart LR
    D[Data and signals] --> F[Clean and represent]
    F --> M[Train and adapt]
    F --> A[Retrieve and orchestrate]
    M --> I[Inference]
    A --> I
    I --> V[Validate and inspect]
    V -. feedback .-> F
'''

# Exact topology derives from the Mermaid source above. This is a capability map,
# not a claim that every project uses every component or is deployed in production.
def pipeline_svg():
    nodes = [
        (40,160, '01 / SIGNALS', 'Data & inputs', 'Python / SQL', 'NumPy / pandas'),
        (275,160, '02 / REPRESENT', 'Features & context', 'EDA / OpenCV', 'spaCy / NLTK'),
        (515,60, '03A / LEARN', 'Train & adapt', 'PyTorch / TensorFlow', 'scikit-learn / LoRA'),
        (515,255, '03B / REASON', 'Retrieve & orchestrate', 'LangChain / CrewAI', 'Google ADK / RAG'),
        (755,160, '04 / INFERENCE', 'Model execution', 'LiteLLM / Ollama', 'Gradio / Docker'),
        (990,160, '05 / EVIDENCE', 'Validate & inspect', 'Pytest / safety gates', 'OpenTelemetry')
    ]
    parts = ['''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="470" viewBox="0 0 1200 470" role="img" aria-labelledby="title desc"><title id="title">Tech stack as an AI capability pipeline</title><desc id="desc">Signals enter representation, branch into learning or retrieval, then inference and validation. Animation illustrates flow only.</desc><defs><linearGradient id="bg"><stop stop-color="#091321"/><stop offset="1" stop-color="#13112C"/></linearGradient><marker id="arrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7Z" fill="#43E8E1"/></marker></defs><style>.mono{font-family:Consolas,monospace}.sans{font-family:Arial,Helvetica,sans-serif}@media(prefers-reduced-motion:reduce){.motion{display:none}}</style><rect x="1" y="1" width="1198" height="468" rx="20" fill="url(#bg)" stroke="#26334D"/><text x="40" y="35" class="mono" font-size="12" letter-spacing="2" fill="#43E8E1">TECH STACK / CAPABILITY GRAPH</text>''']
    paths = ['M245 220H275', 'M480 220H496V120H515', 'M480 220H496V315H515', 'M720 120H740V220H755', 'M720 315H740V220H755', 'M960 220H990']
    for i,path in enumerate(paths):
        parts.append(f'<path d="{path}" fill="none" stroke="#43E8E1" stroke-opacity=".65" stroke-width="1.5" marker-end="url(#arrow)"/>')
        parts.append(f'<circle class="motion" r="3" fill="#A78BFA"><animateMotion dur="{4+i%3}s" begin="{i*.6}s" repeatCount="indefinite" path="{path}"/></circle>')
    parts.append('<path d="M1092 295V416H376V295" fill="none" stroke="#A78BFA" stroke-dasharray="5 7" stroke-opacity=".5"/><text x="690" y="440" text-anchor="middle" class="mono" font-size="12" fill="#9BAFCF">INSPECT / EVALUATE / REFINE</text>')
    for x,y,label,title,l1,l2 in nodes:
        parts.append(f'<rect x="{x}" y="{y}" width="205" height="135" rx="12" fill="#0D1B2E" stroke="#324564"/><rect x="{x}" y="{y}" width="205" height="3" rx="1" fill="#43E8E1"/>')
        parts.append(f'<text x="{x+14}" y="{y+27}" class="mono" font-size="10" letter-spacing="1.1" fill="#A78BFA">{escape(label)}</text><text x="{x+14}" y="{y+57}" class="sans" font-size="15" font-weight="700" fill="#EFF5FF">{escape(title)}</text><text x="{x+14}" y="{y+87}" class="sans" font-size="12" fill="#B7C7E0">{escape(l1)}</text><text x="{x+14}" y="{y+110}" class="sans" font-size="12" fill="#B7C7E0">{escape(l2)}</text>')
    parts.append('</svg>\n')
    return ''.join(parts)

CSS = '''
*{box-sizing:border-box}body{margin:0;background:#080f1b;font-family:Arial,Helvetica,sans-serif;color:#eff5ff}
main{width:1200px;padding:34px 40px 30px;background:radial-gradient(ellipse at 94% 0%,var(--soft),transparent 45%),linear-gradient(110deg,#0b1524,#11162a);border:1px solid #2a3a55;border-top:3px solid var(--accent)}
.top{display:flex;justify-content:space-between;align-items:center;gap:22px;font:12px Consolas,monospace;letter-spacing:2px;color:#a2b5d3}.category{color:var(--accent)}
.title-row{display:grid;grid-template-columns:minmax(0,1fr) 270px;gap:40px;margin-top:25px;align-items:start}
h1{margin:0 0 10px;font-size:39px;letter-spacing:-1px;line-height:1.13}.sub{font-size:16px;color:#bdd0ec;line-height:1.45;max-width:690px}
.metrics{border-left:1px solid #33425e;padding-left:25px}.value{font:700 33px Consolas,monospace;color:var(--accent);letter-spacing:-1px}.metric-label{font-size:13px;line-height:1.55;color:#a5bbd9;margin-top:6px}.metric-note{font:10px Consolas,monospace;color:#8094b3;line-height:1.5;margin-top:8px}
.flow{display:flex;align-items:center;gap:10px;margin-top:25px}.node{flex:1;background:#0a1424;border:1px solid #31415e;border-radius:8px;padding:11px 12px;font:12px Consolas,monospace;line-height:1.45;color:#d8e7fc;text-align:center}.arrow{color:var(--accent);font:17px Consolas,monospace}
.bottom{display:flex;justify-content:space-between;gap:25px;align-items:center;border-top:1px solid #283752;margin-top:24px;padding-top:18px}.chips{display:flex;flex-wrap:wrap;gap:8px}.chip{font:11px Consolas,monospace;color:#afc6e6;background:#111f34;border:1px solid #2a3b57;padding:5px 8px;border-radius:5px}.hint{font:11px Consolas,monospace;color:var(--accent);white-space:nowrap}
'''

def card_html(card):
    nodes = ''
    for i,label in enumerate(card['flow']):
        if i: nodes += '<span class="arrow" aria-hidden="true">→</span>'
        nodes += '<div class="node">'+escape(label)+'</div>'
    chips = ''.join('<span class="chip">'+escape(t)+'</span>' for t in card['tech'])
    return '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+escape(card['name'])+'</title><style>'+CSS+'</style><body><main style="--accent:'+card['accent']+';--soft:'+card['soft']+'"><div class="top"><span class="category">'+escape(card['category'])+'</span><span>MODEL CARD / '+escape(card['index'])+'</span></div><div class="title-row"><div><h1>'+escape(card['name'])+'</h1><div class="sub">'+escape(card['subtitle'])+'</div></div><div class="metrics"><div class="value">'+escape(card['metric'])+'</div><div class="metric-label">'+escape(card['metric_label'])+'</div><div class="metric-note">'+escape(card['metric_note'])+'</div></div></div><div class="flow">'+nodes+'</div><div class="bottom"><div class="chips">'+chips+'</div><div class="hint">EXPAND THE ENGINEERING BRIEF BELOW</div></div></main></body></html>\n'


def main():
    (ASSETS/'header.svg').write_text(HEADER)
    (ASSETS/'footer.svg').write_text(FOOTER)
    (ASSETS/'tech-pipeline.svg').write_text(pipeline_svg())
    (SOURCE/'tech-pipeline.mmd').write_text(PIPELINE_SOURCE)
    manifest = SOURCE/'cards.json'
    if not manifest.exists():
        print('Built animated identity and pipeline. No card manifest yet.', flush=True)
        return
    from playwright.sync_api import sync_playwright
    cards = json.loads(manifest.read_text())
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path='/usr/bin/chromium', args=['--no-sandbox'])
        page = browser.new_page(viewport={'width':1200,'height':900},device_scale_factor=2)
        for card in cards:
            html_path = SOURCE/(card['id']+'.html')
            html_path.write_text(card_html(card))
            page.goto(html_path.as_uri())
            page.locator('main').screenshot(path=str(ASSETS/(card['id']+'-card.png')))
            print('Rendered '+card['id'],flush=True)
        browser.close()

if __name__ == '__main__':
    main()
