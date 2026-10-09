"""Generate six screenshots from sample/demo data only."""
from pathlib import Path
from shutil import which
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
OUT.mkdir(parents=True, exist_ok=True)
server = ThreadingHTTPServer(("127.0.0.1", 0), partial(SimpleHTTPRequestHandler, directory=str(ROOT)))
Thread(target=server.serve_forever, daemon=True).start()
URL = f"http://127.0.0.1:{server.server_port}/ClientFlow-Mini.html"

try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path=which("chromium") or None, args=["--no-sandbox"])
        context = browser.new_context(viewport={"width": 1440, "height": 980}, device_scale_factor=1)
        page = context.new_page()
        page.on("dialog", lambda dialog: dialog.accept())
        page.goto(URL, wait_until="load")
        page.screenshot(path=str(OUT / "screenshot-empty.png"), full_page=True)
        page.locator('[data-view="settings"]').click()
        page.locator("#loadDemo").click()
        page.locator('[data-view="dashboard"]').click()
        page.screenshot(path=str(OUT / "screenshot-real.png"), full_page=True)
        page.screenshot(path=str(OUT / "preview-dashboard.png"), full_page=True)
        page.locator('[data-view="leads"]').click()
        page.screenshot(path=str(OUT / "preview-clients.png"), full_page=True)
        page.locator('[data-view="quotes"]').click()
        page.screenshot(path=str(OUT / "preview-quotes.png"), full_page=True)
        context.close()
        context = browser.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=1, is_mobile=True, has_touch=True)
        mobile = context.new_page()
        mobile.on("dialog", lambda dialog: dialog.accept())
        mobile.goto(URL, wait_until="load")
        mobile.locator('[data-view="settings"]').click()
        mobile.locator("#loadDemo").click()
        mobile.locator('[data-view="dashboard"]').click()
        mobile.screenshot(path=str(OUT / "preview-mobile.png"), full_page=True)
        browser.close()
finally:
    server.shutdown()
print("Generated 6 screenshots in assets/")
