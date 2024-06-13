from ..clients.playwright import PlaywrightModule
from ..clients.openai import OpenAIModule
from ..strategies.captcha.audio_strategy import AudioCaptchaStrategy
from ..strategies.pages.demo import DemoStrategy

class BrowserProvider:
    def __init__(self, url: str, playwright: PlaywrightModule = None, openai: OpenAIModule = None):
        self._url = url
        self._captcha_strategy = None
        self._page_strategy = None
        self._playwright = playwright
        self._openai = openai

    async def init_bypass_strategy(self):
        """
        Initializes the bypass strategy based on the URL and potentially creates Playwright and OpenAI instances.

        This method checks if Playwright and OpenAI instances are provided in the constructor. If not, it creates them asynchronously.
        It then selects the appropriate strategy based on the URL (currently using a simple "demo" check).
        """
        if not self._playwright:
            self._playwright = PlaywrightModule()
            self._playwright = await self._playwright.launch_playwright()

        if not self._openai:
            self._openai = OpenAIModule()

        if "demo" in self._url:
            self._captcha_strategy = AudioCaptchaStrategy(self._playwright, self._openai, self._url)
            self._page_strategy = DemoStrategy(self._playwright, self._captcha_strategy)

        return self
    async def get_content_with_captcha_handling(self):
        """
        Retrieves content from the target URL, potentially handling CAPTCHAs.
        """
        if self._page_strategy:
            try:
                await self._page_strategy.vulnerate_page()
                await self._page_strategy.submit_form()

                content = await self._page_strategy.get_content()

                await self._playwright.stop_playwright()

                return content
            except Exception as e:
                raise Exception(f"Error retrieving content: {e}")
        else:
            print("No strategy set.")
    

        
