#!/usr/bin/env python3
"""Capture the real portfolio UI for the README's visual gateway."""
import argparse
from io import BytesIO
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright

parser=argparse.ArgumentParser()
parser.add_argument('origin',help='Actual published or development portfolio origin')
args=parser.parse_args()
ROOT=Path(__file__).resolve().parents[1]
ASSETS=ROOT/'assets'
COLORS=['77ffe0','baff4a','ff6bcd','f9cd5b','ee7758','ffa947','efad5d','88dc7c','ffd75e','8edeb7','ff7e7b','8ebdff','e5eae8','57b7fa','88b0df','b3a6ee','ffa865','73c9e1','f5a765','f38570','e7d29a','59e3b4','a78bfa','f5c76b','6fb8ff','f29dd7','8ba5c6','f1f4f2']


def save_gif(frames,path):
    images=[]
    for frame in frames:
        image=Image.open(BytesIO(frame)).convert('RGB')
        image.thumbnail((1000,1000),Image.Resampling.LANCZOS)
        images.append(image)
    palette=images[0].quantize(colors=128,method=Image.Quantize.MEDIANCUT)
    values=palette.getpalette()[:128*3]
    for color in COLORS:
        rgb=[int(color[i:i+2],16) for i in (0,2,4)]
        for factor in [1,.8,.55]:
            values.extend(round(v*factor) for v in rgb)
    values.extend([0]*(768-len(values)))
    palette.putpalette(values[:768])
    prepared=[image.quantize(palette=palette,dither=Image.Dither.NONE) for image in images]
    prepared[0].save(path,save_all=True,append_images=prepared[1:],duration=180,loop=0,optimize=True,disposal=1)
    print(path.name,path.stat().st_size,flush=True)


with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':1440,'height':1000},device_scale_factor=1)
    page.goto(args.origin,wait_until='networkidle',timeout=60000)
    Image.open(BytesIO(page.locator('.hero').screenshot())).convert('RGB').save(ASSETS/'portfolio-cover.webp',quality=90,method=6)
    page.set_viewport_size({'width':1140,'height':1100})
    frames=[]
    section=page.locator('.project-section')
    for name in ['mooox','health-guardian','amarzero','mooox']:
        page.locator(f'.project-card[data-project="{name}"]').hover()
        for _ in range(4):
            page.wait_for_timeout(170)
            frames.append(section.screenshot())
    save_gif(frames,ASSETS/'projects-interaction.gif')
    frames=[]
    section=page.locator('.stack-section')
    for name in ['pytorch','opencv','langchain','docker','huggingface']:
        page.locator(f'.tool-node[data-tool="{name}"]').hover()
        for _ in range(3):
            page.wait_for_timeout(170)
            raw=Image.open(BytesIO(section.screenshot())).convert('RGB')
            # The development-only fixed Preview toolbar is outside the site UI.
            # A section capture may include its bottom overlap; discard that strip.
            if '.manus.computer' in args.origin:
                raw=raw.crop((0,0,raw.width,raw.height-32))
            buf=BytesIO();raw.save(buf,format='PNG');frames.append(buf.getvalue())
    save_gif(frames,ASSETS/'stack-interaction.gif')
    browser.close()
