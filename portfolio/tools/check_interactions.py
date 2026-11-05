#!/usr/bin/env python3
from pathlib import Path
import json
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PREVIEW = 'https://8328-i0nhajbcey41a67v16ict-7a9cf20f.sg2.manus.computer'
CAPTURE = ROOT / 'checks'
CAPTURE.mkdir(exist_ok=True)
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path='/usr/bin/chromium', args=['--no-sandbox'])
    page = browser.new_page(viewport={'width':1440,'height':1000}, device_scale_factor=1)
    errors = []
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.goto(PREVIEW, wait_until='networkidle', timeout=60000)
    page.get_by_role('heading', name='Intelligence, engineered.').wait_for()
    page.screenshot(path=str(CAPTURE/'hero-desktop.png'))
    card = page.locator('.project-card').first
    card.hover()
    page.wait_for_function("Number(getComputedStyle(document.querySelector('.stack-overlay')).opacity) > .95")
    assert card.locator('.project-tool').count() == 5
    page.screenshot(path=str(CAPTURE/'projects-hover.png'))
    tool = page.locator('.tool-node[data-tool="opencv"]')
    tool.hover()
    assert page.locator('.selected-name').inner_text() == 'OpenCV'
    assert page.locator('.tool-core').get_attribute('data-action') == 'vision'
    assert page.locator('.connected-projects').inner_text().strip() == 'AmarZero'
    page.screenshot(path=str(CAPTURE/'stack-hover.png'))
    tool.click()
    page.get_by_role('button', name='Vision + RL',exact=True).click()
    assert page.locator('.project-card:visible').count() == 1
    page.get_by_role('button', name='All systems',exact=True).click()
    assert page.locator('.project-card:visible').count() == 7
    page.locator('.motion-control').click()
    assert page.locator('html').get_attribute('data-reduced-motion') == 'true'
    images = page.locator('.neural-art').evaluate('(i)=>({loaded:i.complete&&i.naturalWidth>0,src:i.src,width:i.naturalWidth})')
    assert not errors,errors
    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), 'Desktop horizontal overflow'
    phone = browser.new_context(viewport={'width':390,'height':844},is_mobile=True,has_touch=True,device_scale_factor=1)
    mobile = phone.new_page()
    mobile.goto(PREVIEW,wait_until='networkidle',timeout=60000)
    mobile.locator('.card-reveal').first.click()
    mobile.wait_for_function("document.querySelector('.project-card').classList.contains('is-revealed')")
    mobile.wait_for_function("Number(getComputedStyle(document.querySelector('.stack-overlay')).opacity) > .95")
    mobile.screenshot(path=str(CAPTURE/'mobile-stack-reveal.png'))
    mobile.locator('.card-reveal').first.click()
    assert not mobile.locator('.project-card').first.evaluate('(el)=>el.classList.contains("is-revealed")')
    mobile.wait_for_function("Number(getComputedStyle(document.querySelector('.stack-overlay')).opacity) < .05")
    mobile.locator('.tool-node[data-tool="docker"]').tap()
    assert mobile.locator('.selected-name').inner_text() == 'Docker'
    assert mobile.locator('.tool-core').get_attribute('data-action') == 'runtime'
    assert mobile.evaluate('document.documentElement.scrollWidth <= innerWidth'), 'Mobile horizontal overflow'
    print(json.dumps({'desktop_hover_reveal':'passed','tool_hover_actions':'passed','tool_project_connections':'passed','filters':'passed','reduced_motion':'passed','mobile_tap_reveal_hide':'passed','mobile_tool_actions':'passed','horizontal_overflow':'none','javascript_errors':errors,'hero_image':images},indent=2))
    browser.close()
