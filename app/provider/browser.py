from ..shared.utils import Utils
from ..clients.playwright import PlaywrightModule
from ..clients.openai import OpenAIModule
from ..strategies.captcha.audio_strategy import AudioCaptchaStrategy
from ..strategies.pages.demo import DemoStrategy


class BrowserProvider:
    def __init__(
        self, playwright: PlaywrightModule, openai: OpenAIModule, utils: Utils
    ):
        self._playwright = playwright
        self._openai = openai
        self._utils = utils
        self._page_strategy = None

    async def init_bypass_strategy(self, url: str):
        """
        Initializes the bypass strategy based on the URL and potentially
        creates Playwright and OpenAI instances.

        This method checks if Playwright and OpenAI instances are provided in
        the constructor. If not, it creates them asynchronously.
        It then selects the appropriate strategy based on the URL (currently using a
        simple "demo" check).
        """
        self._playwright = await self._playwright.launch_playwright()

        if "demo" in url:
            captcha_strategy = AudioCaptchaStrategy(
                playwright=self._playwright, openai=self._openai, utils=self._utils
            )
            self._page_strategy = DemoStrategy(self._playwright, captcha_strategy)

        return self

    async def get_content_with_captcha_handling(self, url: str):
        """
        Retrieves content from the target URL, potentially handling CAPTCHAs.
        """
        if self._page_strategy:
            try:
                await self._page_strategy.vulnerate_page(url)
                await self._page_strategy.submit_form()

                content = await self._page_strategy.get_content()

                await self._playwright.stop_playwright()

                return content
            except Exception as exception:
                raise Exception(f"Error retrieving content: {exception}") from exception
        else:
            print("No strategy set.")
