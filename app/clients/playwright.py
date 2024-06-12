from playwright.async_api import async_playwright

class PlaywrightModule():
    def __init__(self):
        self._browser = None
        self._page = None

    async def init_playwright(self):
        playwright = await async_playwright().start()
        browser = await playwright.firefox.launch(
            headless=True,
        )

        self._browser = browser
        self._page = await browser.new_page()
