from playwright.async_api import async_playwright


class PlaywrightModule:
    def __init__(self):
        """
        Initializes the PlaywrightModule instance. The browser is not launched here.
        """
        self.browser = None
        self.page = None
        self._instance = None

    async def launch_playwright(self):
        """
        Launches a new Playwright instance with Firefox browser in headless mode.
        """
        playwright = await async_playwright().start()
        browser = await playwright.firefox.launch(
            headless=True,
        )

        self._instance = playwright
        self.browser = browser
        self.page = await browser.new_page()

        return self

    async def stop_playwright(self):
        """
        Stops the Playwright instance and closes the browser (if launched).
        """
        if self.browser:
            await self.browser.close()
        await self._instance.stop()

        self.browser = None
        self.page = None
        self._instance = None
