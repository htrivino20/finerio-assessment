from playwright.async_api import async_playwright

class PlaywrightModule():
    def __init__(self):
        """
        Initializes the PlaywrightModule instance. The browser is not launched here.
        """
        self._browser = None
        self._page = None

    async def launch_playwright(self):
        """
        Launches a new Playwright instance with Firefox browser in headless mode.
        Returns the PlaywrightModule instance for method chaining.
        """
        playwright = await async_playwright().start()
        browser = await playwright.firefox.launch(
            headless=True,
        )
        self._browser = browser
        self._page = await browser.new_page()

        return self
    