#!/usr/bin/env python3
"""Build the static, progressively enhanced AI portfolio from reviewed project facts."""
import html
import json
import re
import shutil
import sys
from pathlib import Path
from visual_data import tool_records, glyph, GROUPS, DOMAINS, SHORT, METRIC_LABELS

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'site'
OUT.mkdir(exist_ok=True)
PROJECTS = json.loads((ROOT / 'src/data/projects.json').read_text())
TOOLS = tool_records()
ORIGIN = (ROOT / 'site-origin.txt').read_text().strip().rstrip('/') if (ROOT / 'site-origin.txt').exists() else ''
H = html.escape


def icon(slug):
    file = ROOT / 'public/assets/icons' / (slug + '.svg')
    if not file.exists():
        return '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m12 2 9 5v10l-9 5-9-5V7Z" fill="none" stroke="currentColor"/><circle cx="12" cy="12" r="3" fill="currentColor"/></svg>'
    raw = file.read_text()
    raw = re.sub(r'<title>.*?</title>', '', raw)
    raw = raw.replace('<svg ', '<svg aria-hidden="true" ')
    return raw


def tech_icon(name):
    aliases = [('python','python'),('pytorch','pytorch'),('tensorflow','tensorflow'),('scikit','scikitlearn'),('opencv','opencv'),('transformer','huggingface'),('hugging','huggingface'),('gemma','google'),('gradio','gradio'),('langchain','langchain'),('ollama','ollama'),('litellm','ollama'),('docker','docker'),('numpy','numpy'),('pandas','pandas'),('mpnet','huggingface'),('zephyr','huggingface'),('spacy','spacy'),('pydantic','python'),('vit','pytorch')]
    for key, slug in aliases:
        if key in name.lower():
            return icon(slug)
    return icon('unbranded-tool')


def inline(text):
    text = H(text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return text


def markdown(text):
    blocks = []
    for block in text.split('\n\n'):
        if block.startswith('### '):
            blocks.append('<h3>' + inline(block[4:]) + '</h3>')
        elif block.startswith('## '):
            blocks.append('<h2>' + inline(block[3:]) + '</h2>')
        elif block.strip():
            blocks.append('<p>' + inline(block.strip()) + '</p>')
    return ''.join(blocks)


def links(project):
    result = []
    if project['repo']:
        result.append(('Code repository', 'https://github.com/amarwahdan/' + project['repo']))
    if project['demo']:
        result.append(('Executable notebook', project['demo']))
    if project['writeup']:
        result.append(('Research paper' if project['id'] == 'amarzero' else 'Published writeup', project['writeup']))
    if project['video']:
        result.append(('Video walkthrough', project['video']))
    if not result and project['id'] == 'mooox':
        result.append(('Discuss the private project', 'https://www.linkedin.com/in/amar-ahmed-hamed-25b676302'))
    return ''.join(f'<a href="{H(url, quote=True)}" target="_blank" rel="noopener noreferrer">{H(label)} ↗</a>' for label, url in result)


def meta(path, title, description):
    if not ORIGIN:
        return ''
    url = ORIGIN + path
    return f'<link rel="canonical" href="{H(url)}"><meta property="og:url" content="{H(url)}"><meta property="og:image" content="{ORIGIN}/assets/og.png"><meta name="twitter:title" content="{H(title)}"><meta name="twitter:description" content="{H(description)}">'


def detail_page(title, kicker, lead, body, path):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#07090c"><title>{H(title)} — Amar Ahmed Hamed</title><meta name="description" content="{H(lead[:155])}"><meta property="og:type" content="article"><meta property="og:title" content="{H(title)} — Amar Ahmed Hamed"><meta property="og:description" content="{H(lead[:155])}">{meta(path,title,lead[:155])}<link rel="icon" href="/assets/mark.svg"><link rel="stylesheet" href="/styles.css"><script type="module" src="/app.js"></script></head><body class="detail-page"><a class="skip-link" href="#detail-content">Skip to details</a><div class="pointer-aura" aria-hidden="true"></div><header class="site-header"><a class="brand" href="/"><img src="/assets/mark.svg" alt="" width="32" height="32"><span>AMAR<span class="brand-dot">.AI</span></span></a><nav aria-label="Navigation"><a href="/#projects">Systems</a><a href="/#stack">Stack</a><a href="/#signal">Signal</a></nav><a class="contact-link" href="mailto:aammaarrah10@gmail.com">Let's connect ↗</a></header><main class="detail-shell" id="detail-content"><a class="text-link" href="/#projects">← Back to portfolio</a><p class="detail-kicker">{H(kicker)}</p><h1>{H(title)}</h1><p class="lead">{H(lead)}</p>{body}</main><footer class="site-footer"><a class="brand" href="/"><img src="/assets/mark.svg" alt="" width="25" height="25"><span>AMAR.AI</span></a><span class="mono">BUILD WITH EVIDENCE</span><button class="motion-control mono" aria-pressed="false">REDUCE MOTION</button><a class="mono" href="/">BACK TO PORTFOLIO ↗</a></footer></body></html>'''


cards = []
for p in PROJECTS:
    stack = ''.join(f'<span class="project-tool" style="transition-delay:{i * 35}ms">{tech_icon(t)}<span>{H(t)}</span></span>' for i, t in enumerate(p['tech']))
    if not stack:
        stack = '<span class="project-tool">Stack not publicly documented</span>'
    cards.append(f'''<article class="project-card" data-project="{p['id']}" data-group="{GROUPS[p['id']]}" style="--accent:{p['accent']}"><div class="card-top"><span>{p['index']} / 07</span><span class="card-domain">{DOMAINS[p['id']]}</span></div><h3 class="card-title">{H(p['name'])}</h3><div class="project-glyph">{glyph(p['id'])}</div><div class="card-metric" title="{H(p['metric_note'])}"><span>{H(p['metric'])}</span><small>{H(METRIC_LABELS[p['id']])}</small></div><div class="stack-overlay" aria-hidden="true" id="stack-{p['id']}"><div class="overlay-label">SYSTEM STACK / REVEALED</div><div class="card-stack">{stack}</div><p>{H(SHORT[p['id']])}</p></div><div class="card-bottom"><a href="/projects/{p['id']}/">Inspect architecture ↗</a><button class="card-reveal" aria-expanded="false" aria-controls="stack-{p['id']}"><span class="reveal-label">Reveal stack</span><span class="reveal-symbol">+</span></button></div></article>''')

node_html = []
extra_html = []
for i, tool in enumerate(TOOLS):
    attributes = f'data-tool="{tool["id"]}" data-x="{tool["x"]}" data-y="{tool["y"]}" aria-pressed="false" aria-label="Explore {H(tool["name"])} connections" style="--x:{tool["x"] / 660 * 100:.3f}%;--y:{tool["y"] / 490 * 100:.3f}%;--tool-color:{tool["color"]}"'
    if i < 18:
        node_html.append(f'<button class="tool-node" {attributes}><span class="tool-icon">{icon(tool["id"])}</span><span class="tool-name">{H(tool["name"])}</span></button>')
    else:
        extra_html.append(f'<button class="tool-chip" {attributes}>{icon(tool["id"])}<span>{H(tool["name"])}</span></button>')

filters = [('all','All systems'),('agents','Agents'),('vision','Vision + RL'),('research','Research'),('nlp','NLP'),('archive','Archive')]
filters_html = ''.join(f'<button class="filter-button" data-filter="{key}" aria-pressed="{str(key == "all").lower()}">{label}</button>' for key,label in filters)
source = (ROOT / 'src/index.html').read_text()
replacements = {'__PROJECT_CARDS__': ''.join(cards), '__TOOL_NODES__': ''.join(node_html), '__FILTERS__': filters_html, '__PROJECT_COUNT__': str(len(PROJECTS)).zfill(2), '__INITIAL_ICON__': icon('pytorch'), '__ORIGIN_META__': meta('/','Amar Ahmed Hamed — AI Engineer','Interactive AI engineering portfolio')}
for marker, value in replacements.items():
    source = source.replace(marker, value)
source = source.replace('<div class="stack-foot mono">', '<details class="extended-toolkit"><summary>EXTENDED TOOLKIT / '+str(len(extra_html)).zfill(2)+' MORE ICONS</summary><div class="extended-tools">'+''.join(extra_html)+'</div></details><div class="stack-foot mono">')
data = {'tools': TOOLS, 'projects': [{'id':p['id'],'name':p['name']} for p in PROJECTS]}
source = source.replace('</body>', '<script id="portfolio-data" type="application/json">'+json.dumps(data).replace('</','<\\/')+'</script></body>')
assert not re.search(r'__[A-Z_]+__', source), 'Unresolved page placeholder'
(OUT / 'index.html').write_text('\n'.join(line.rstrip() for line in source.splitlines())+'\n')
shutil.copy2(ROOT / 'src/styles.css', OUT / 'styles.css')
shutil.copy2(ROOT / 'src/app.js', OUT / 'app.js')
shutil.copytree(ROOT / 'public/assets', OUT / 'assets', dirs_exist_ok=True)

routes = [{'path':'/','title':'Amar Ahmed Hamed — AI Engineer'}]
for p in PROJECTS:
    flow = ''
    for i, step in enumerate(p['flow']):
        if i:
            flow += '<i aria-hidden="true">→</i>'
        flow += '<span>'+H(step)+'</span>'
    sources = ''.join(f'<a href="{H(s["url"])}" target="_blank" rel="noopener noreferrer">{H(s["label"])} ↗</a>' for s in p['sources'])
    tech = H(p['technologies']) if p['technologies'] else 'No public technology stack is documented for this inactive project.'
    overview = f'<div class="detail-overview" style="--accent:{p["accent"]}"><div class="detail-art">{glyph(p["id"])}</div><div><p class="detail-kicker">ENGINEERING EVIDENCE</p><div class="detail-body">{markdown(p["result"])}</div><div class="detail-links">{links(p)}</div></div></div>'
    body = overview + f'<div class="detail-body"><h2>The idea</h2><p>{inline(p["idea"])}</p><h2>The engineering challenge</h2><p>{inline(p["challenge"])}</p><h2>Architecture outline</h2><div class="detail-flow">{flow}</div><h2>Technology stack</h2><p>{tech}</p><p class="detail-status">{H(p["status"])}</p>{markdown(p["deep"])}<h2>Source artifacts</h2><div class="detail-sources">{sources if sources else "<p>No public implementation artifacts are available.</p>"}</div><div class="detail-links"><a href="https://github.com/amarwahdan/amarwahdan/blob/main/docs/projects/{p["id"]}.md" target="_blank" rel="noopener noreferrer">GitHub architecture spec ↗</a><a href="/#projects">Explore another system ↗</a></div></div>'
    folder = OUT / 'projects' / p['id']
    folder.mkdir(parents=True, exist_ok=True)
    path = '/projects/'+p['id']+'/'
    (folder / 'index.html').write_text(detail_page(p['name'],DOMAINS[p['id']],SHORT[p['id']],body,path))
    routes.append({'path':path,'title':p['name']})

about_body = '''<div class="about-grid"><div class="detail-body"><h2>Across the system, not just the model</h2><p>I'm Amar Ahmed Hamed, an AI Engineer / Machine Learning Engineer based in Cairo, Egypt. My work spans agentic workflows, computer vision, NLP, scientific retrieval, tactical feature engineering, and vision-based reinforcement-learning research.</p><p>I work on how models see, retrieve, reason, call tools, preserve state, and connect their outputs to useful interfaces. This portfolio links each project to its implementation and available evidence.</p><h2 id="experience">Experience &amp; learning</h2><h3>PathLine Training Academy</h3><p><strong>Machine Learning Engineer — hands-on training · May–June 2025 · Cairo, Egypt.</strong> Built TensorFlow image-classification applications, an NLP sentiment-analysis interface, and a Q-Learning Tic-Tac-Toe agent. Applied preprocessing for imbalance, outliers, skewness, and feature engineering.</p><h3>Information Technology Institute</h3><p><strong>Artificial Intelligence Academy for Professionals.</strong> Specialized training in Computer Vision, NLP, and GenAI Engineering, alongside self-directed study and project work.</p><h2 id="capabilities">Capability notes</h2><p>The interactive toolkit combines documented skills and tools visible in the project artifacts. A connection to a project indicates a documented use; a tool with no featured-project connection is presented as a profile capability, not an assertion that every project uses it.</p><p>Python, PyTorch, TensorFlow, scikit-learn, OpenCV, NLP tools, RAG frameworks, agent-workflow tools, data libraries, SQL, and container tooling are presented through their engineering roles. The visual signatures are interface animations, not live model inference, benchmarks, or claims of production deployment.</p><div class="detail-links"><a href="https://www.linkedin.com/in/amar-ahmed-hamed-25b676302" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a><a href="mailto:aammaarrah10@gmail.com">Email ↗</a><a href="https://www.kaggle.com/amarahmedhamed" target="_blank" rel="noopener noreferrer">Kaggle ↗</a></div></div><aside class="about-aside"><p class="mono">ENGINEERING FOCUS<br><br>AGENTIC WORKFLOWS<br>VISUAL PERCEPTION<br>WORLD MODELS + MCTS<br>RETRIEVAL + PROVENANCE<br>FEATURE ENGINEERING<br>INFERENCE INTERFACES</p></aside></div>'''
research_body = '''<div class="detail-body"><h2>AmarZero</h2><p>Authored research on a proposed hybrid architecture for vision-based object tracking and planning: visual encoding, Kalman state estimation, a learned world model, and Monte Carlo Tree Search. The paper reports limited single-object and multi-object experiment results; the project brief explains their scope.</p><div class="detail-links"><a href="/projects/amarzero/">Research brief ↗</a><a href="https://github.com/amarwahdan/AmarZero/blob/main/AmarZero%20paper%20v10.pdf" target="_blank" rel="noopener noreferrer">Authored paper ↗</a></div><h2>Published project writeups</h2><p>Health Guardian documents multimodal evidence extraction, verification tools, and deterministic safety gating. Tactical Intelligence Framework documents 49 engineered features across 9 analytical clusters.</p><div class="detail-links"><a href="/projects/health-guardian/">Health Guardian ↗</a><a href="/projects/tactical/">Tactical Intelligence ↗</a></div><h2 id="wids">WiDS Global Datathon 2026</h2><p><strong>#34 on the Public Leaderboard, as reported by me.</strong> This is not a private or final leaderboard rank. The competition concerns survival analysis for wildfire threat forecasting, including right-censoring and time-horizon probabilities. No unreported model score or implementation is attributed to the placement.</p><h2>Professional recognition</h2><p>Kaggle Expert · Best Trainee at PathLine · GALACTIC PROBLEM SOLVER · EliteBridge Award nominee. A nomination is presented as a nomination, not an award win.</p><p class="detail-status">The linked papers and writeups are authored research/project publications; no peer-reviewed venue is implied.</p><div class="detail-links"><a href="https://www.kaggle.com/amarahmedhamed" target="_blank" rel="noopener noreferrer">Kaggle profile ↗</a><a href="/about/#experience">Experience ↗</a></div></div>'''
for slug,title,kicker,lead,body in [('about','Across the intelligence layer.','PROFILE / AMAR AHMED HAMED','AI Engineer / Machine Learning Engineer. Cairo, Egypt.',about_body),('research','Research & recognition.','RESEARCH / COMPETITION SIGNALS','Explore the papers, published writeups, and professional signals behind the systems.',research_body)]:
    folder = OUT / slug
    folder.mkdir(exist_ok=True)
    path = '/'+slug+'/'
    (folder / 'index.html').write_text(detail_page(title,kicker,lead,body,path))
    routes.append({'path':path,'title':title})
(OUT / 'manus-routes.json').write_text(json.dumps({'routes':routes},indent=2)+'\n')
(OUT / '404.html').write_text(detail_page('Signal not found.','404 / UNKNOWN ROUTE','This page is not part of the portfolio.','<div class="detail-links"><a href="/">Return to the portfolio ↗</a></div>','/404').replace('<meta name="theme-color"', '<meta name="robots" content="noindex"><meta name="theme-color"'))
if ORIGIN:
    urls = ''.join('<url><loc>'+H(ORIGIN+route['path'])+'</loc></url>' for route in routes)
    (OUT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+urls+'</urlset>')
    (OUT / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+ORIGIN+'/sitemap.xml\n')
print(f'Built {len(routes)} content-bearing pages, {len(PROJECTS)} project cards, and {len(TOOLS)} interactive technology icons.')
