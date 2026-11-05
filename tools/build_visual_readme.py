#!/usr/bin/env python3
"""Build the visual README gateway from its maintained Markdown source."""
from pathlib import Path
import argparse

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--portfolio-url',help='Actual published portfolio origin, without a trailing slash')
args=parser.parse_args()
source=ROOT/'assets/source/visual-readme.md'
text=source.read_text()
if args.portfolio_url:
    origin=args.portfolio_url.rstrip('/')
    if not origin.startswith('https://'):
        raise ValueError('The published portfolio requires an HTTPS origin.')
    text=text.replace('__PORTFOLIO_URL__',origin)
if '__PORTFOLIO_URL__' in text:
    raise ValueError('Supply --portfolio-url with the actual successfully published origin.')
for relative in ['assets/portfolio-cover.webp','assets/stack-interaction.gif','assets/projects-interaction.gif','assets/source/visual-ribbon.svg']:
    file=ROOT/relative
    if not file.exists() or file.stat().st_size==0:
        raise FileNotFoundError(relative)
(ROOT/'README.md').write_text(text)
print('Built the visual README gateway. Long project briefs remain in docs/projects/.')
