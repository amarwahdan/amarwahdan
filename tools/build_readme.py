#!/usr/bin/env python3
"""Build the profile and project briefs from their source-controlled content."""
from pathlib import Path
from urllib.parse import quote
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'assets/source'
DOCS = ROOT / 'docs/projects'
DOCS.mkdir(parents=True, exist_ok=True)
CARDS = json.loads((SOURCE/'cards.json').read_text())


def button(label, url, color='43E8E1'):
    badge = 'https://img.shields.io/badge/'+quote(label, safe='')+'-'+color+'?style=for-the-badge&labelColor=101B2D'
    return '<a href="'+escape(url,quote=True)+'"><img src="'+badge+'" alt="'+escape(label,quote=True)+'" /></a>'


def main():
    projects=[]
    for c in CARDS:
        spec='./docs/projects/'+c['id']+'.md'
        links=[button('ARCHITECTURE SPEC',spec,c['accent'][1:])]
        if c['repo']:
            links.append(button('CODE REPO','https://github.com/amarwahdan/'+c['repo'],c['accent'][1:]))
        else:
            links.append(button('DISCUSS PROJECT','mailto:aammaarrah10@gmail.com',c['accent'][1:]))
        if c['demo']:
            links.append(button('NOTEBOOK DEMO',c['demo'],c['accent'][1:]))
        if c['writeup']:
            links.append(button('RESEARCH PAPER' if c['id']=='amarzero' else 'WRITEUP',c['writeup'],c['accent'][1:]))
        if c['video']:
            links.append(button('VIDEO WALKTHROUGH',c['video'],c['accent'][1:]))
        section='### '+c['name']+'\n\n'
        section+='<a href="'+spec+'"><img src="./assets/'+c['id']+'-card.png" width="100%" alt="'+escape(c['name']+' — '+c['subtitle']+' '+c['metric']+': '+c['metric_label']+'. '+c['metric_note'],quote=True)+'" /></a>\n\n'
        section+='<p>'+ '\n'.join(links)+'</p>\n\n'
        if c['repo']:
            badge='https://img.shields.io/github/last-commit/amarwahdan/'+c['repo']+'?label=Repository%20updated&color='+c['accent'][1:]+'&labelColor=101B2D'
            section+='[![Latest '+c['name']+' repository commit]('+badge+')](https://github.com/amarwahdan/'+c['repo']+'/commits/main)\n\n'
        section+='<details>\n<summary><b>Open engineering brief — idea / challenge / evidence'+(' / stack' if c['technologies'] else '')+'</b></summary>\n\n'
        section+='**Idea.** '+c['idea']+'\n\n**Engineering challenge.** '+c['challenge']+'\n\n**Result and evidence.** '+c['result']+'\n\n'
        if c['technologies']:
            section+='**Tech stack.** '+c['technologies']+'\n\n'
        section+='**Status and evaluation boundary.** '+c['status']+'\n\n'
        if c['diagram']:
            section+='```mermaid\n'+c['diagram']+'\n```\n\n'
        section+='[Inspect the complete architecture and source artifacts]('+spec+').\n\n</details>\n\n---\n\n'
        projects.append(section)
        doc='# '+c['name']+' — Architecture Brief\n\n[Back to profile](../../README.md#featured-projects)\n\n'
        doc+='## System purpose\n\n'+c['idea']+'\n\n## Engineering challenge\n\n'+c['challenge']+'\n\n'
        if c['diagram']:
            doc+='## Documented data flow\n\n```mermaid\n'+c['diagram']+'\n```\n\n'
        doc+='## Numeric evidence and status\n\n'+c['result']+'\n\n'+c['status']+'\n\n'
        if c['technologies']:
            doc+='## Technologies\n\n'+c['technologies']+'\n\n'
        doc+=c['deep']+'\n\n'
        urls=[]
        if c['repo']:
            urls.append({'label':'Code repository','url':'https://github.com/amarwahdan/'+c['repo']})
        if c['demo']:
            urls.append({'label':'Public notebook demo','url':c['demo']})
        if c['writeup']:
            urls.append({'label':'Paper / writeup','url':c['writeup']})
        if c['video']:
            urls.append({'label':'Video walkthrough','url':c['video']})
        urls+=c['sources']
        if urls:
            doc+='## Original artifacts\n\n'+'\n'.join('- ['+x['label']+']('+x['url']+')' for x in urls)+'\n'
        (DOCS/(c['id']+'.md')).write_text(doc)
    readme=(SOURCE/'profile-intro.md').read_text()+'\n'+''.join(projects)+(SOURCE/'profile-outro.md').read_text()
    (ROOT/'README.md').write_text(readme)
    print('Built README and '+str(len(CARDS))+' project architecture briefs.',flush=True)

if __name__=='__main__':
    main()
