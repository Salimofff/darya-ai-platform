import asyncio
from playwright.async_api import async_playwright

pages = [
    ("index", "http://localhost:8765/index.html"),
    ("configurator", "http://localhost:8765/configurator.html"),
    ("register", "http://localhost:8765/register.html"),
    ("payment", "http://localhost:8765/payment.html"),
    ("launch", "http://localhost:8765/launch.html"),
    ("console", "http://localhost:8765/console.html"),
    ("api", "http://localhost:8765/api.html"),
]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for name, url in pages:
            page = await browser.new_page(viewport={"width": 1440, "height": 900})
            await page.goto(url, wait_until="networkidle")
            await page.wait_for_timeout(1000)
            path = f"/home/user/workspace/darya-platform/shots_new/{name}.png"
            await page.screenshot(path=path, full_page=True)
            print(f"Saved: {path}")
            await page.close()
        await browser.close()

asyncio.run(main())
