import os, glob
from playwright.sync_api import sync_playwright

URL = "https://jettsclaw.github.io/orient-natural-therapy/"
FR = os.path.expanduser("~/Projects/orient-natural-therapy/vid/frames")
for f in glob.glob(FR+"/*.png"): os.remove(f) if os.path.exists(f) else None
os.makedirs(FR, exist_ok=True)

with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(viewport={"width":540,"height":1170}, device_scale_factor=2)
    pg = ctx.new_page()
    pg.goto(URL, wait_until="networkidle")
    pg.wait_for_timeout(1500)
    h = pg.evaluate("document.body.scrollHeight - innerHeight")
    idx = 0
    def shot():
        global idx
        pg.screenshot(path=f"{FR}/f{idx:04d}.png")
        idx += 1
    for _ in range(12): shot()              # hold on hero
    steps = 150
    for i in range(1, steps+1):
        y = int(h * (i/steps))
        pg.evaluate(f"scrollTo(0,{y})")
        pg.wait_for_timeout(16)
        shot()
    for _ in range(16): shot()              # hold on footer/offer
    ctx.close(); b.close()
print("FRAMES:", idx)
