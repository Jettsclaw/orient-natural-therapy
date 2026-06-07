import os
from playwright.sync_api import sync_playwright
B = os.path.expanduser("~/Projects/orient-natural-therapy/vid")
with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(viewport={"width":540,"height":1170}, device_scale_factor=2)
    pg = ctx.new_page()
    for name in ["intro","end"]:
        pg.goto("file://"+B+f"/{name}.html")
        pg.wait_for_timeout(1200)
        pg.screenshot(path=f"{B}/{name}.png")
    ctx.close(); b.close()
print("cards shot")
