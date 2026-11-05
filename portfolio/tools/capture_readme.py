#!/usr/bin/env python3
"""Capture actual UI interactions, without fabricated cursor overlays or telemetry."""
from io import BytesIO
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
ASSETS=Path('/home/ubuntu/amar-profile/repo/assets')
PREVIEW='https://8328-i0nhajbcey41a67v16ict-7a9cf20f.sg2.manus.computer'


def save_gif(frames, path):
    prepared=[]
    for frame in frames:
        image=Image.open(BytesIO(frame)).convert('RGB')
        image.thumbnail((1040,1000),Image.Resampling.LANCZOS)
        prepared.append(image.quantize(colors=160,method=Image.Quantize.MEDIANCUT))
    prepared[0].save(path,save_all=True,append_images=prepared[1:],duration=160,loop=0,optimize=True,disposal=2)
    print(path.name,path.stat().st_size)


with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':1440,'height':1000},device_scale_factor=1)
    page.goto(PREVIEW,wait_until='networkidle',timeout=60000)
    cover=Image.open(BytesIO(page.locator('.hero').screenshot())).convert('RGB')
    cover.save(ASSETS/'portfolio-cover.webp',quality=90,method=6)
    page.set_viewport_size({'width':1040,'height':1000})
    project_frames=[]
    section=page.locator('.project-section')
    section.scroll_into_view_if_needed()
    for project in ['mooox','health-guardian','amarzero','mooox']:
        card=page.locator(f'.project-card[data-project="{project}"]')
        card.scroll_into_view_if_needed()
        card.hover()
        for _ in range(5):
            page.wait_for_timeout(150)
            project_frames.append(section.screenshot())
    save_gif(project_frames,ASSETS/'projects-interaction.gif')
    stack_frames=[]
    stack=page.locator('.stack-section')
    stack.scroll_into_view_if_needed()
    for tool in ['pytorch','opencv','langchain','docker','huggingface']:
        page.locator(f'.tool-node[data-tool="{tool}"]').hover()
        for _ in range(4):
            page.wait_for_timeout(150)
            stack_frames.append(stack.screenshot())
    save_gif(stack_frames,ASSETS/'stack-interaction.gif')
    browser.close()
print('Captured cover and real hover demonstrations for README.')
