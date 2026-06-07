import os, glob
from playwright.sync_api import sync_playwright

FR = os.path.expanduser("~/Projects/orient-natural-therapy/vid/frames2")
for f in glob.glob(FR+"/*.png"): os.remove(f)
os.makedirs(FR, exist_ok=True)

def cap(p):
    if p < 0.09:  return "Two treatments,<br>one visit."
    if p < 0.26:  return "Trusted — <span>4.6&#9733;</span> from 85 reviews"
    if p < 0.46:  return "Acupuncture · massage ·<br>Chinese medicine"
    if p < 0.66:  return "<span>20 years</span> of care"
    if p < 0.86:  return "First visit: <span>30 minutes free</span>"
    return "Book in one tap."

def ease(t):  # easeInOutCubic
    return 4*t*t*t if t < 0.5 else 1 - pow(-2*t+2, 3)/2

with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(viewport={"width":540,"height":960}, device_scale_factor=2)
    pg = ctx.new_page()
    pg.goto("http://localhost:8920/stage.html", wait_until="networkidle")
    pg.wait_for_timeout(2600)
    ih = pg.evaluate("(()=>{const s=document.getElementById('site');return s.contentWindow.document.body.scrollHeight - s.clientHeight;})()")
    idx = 0
    def shot(p):
        global idx
        pg.evaluate(f"window.CAP(`{cap(p)}`)")
        pg.screenshot(path=f"{FR}/g{idx:04d}.png"); idx += 1
    for _ in range(16): shot(0.0)            # hold hero
    steps = 150
    for i in range(1, steps+1):
        p = ease(i/steps)
        pg.evaluate(f"document.getElementById('site').contentWindow.scrollTo(0,{int(p*ih)})")
        pg.wait_for_timeout(16); shot(p)
    for _ in range(18): shot(1.0)            # hold end
    ctx.close(); b.close()
print("FRAMES2:", idx, "innerScroll:", ih)
