from ..clients.playwright import PlaywrightModule
from ..clients.openai import OpenAIModule
from ..strategies.captcha.audio_strategy import AudioCaptchaStrategy
from ..strategies.pages.demo import DemoStrategy

class BrowserProvider:
    def __init__(self, url: str):
        self._url = url
        self._strategy = None

    async def init_bypass_strategy(self):
        playwright = PlaywrightModule()
        playwright = await playwright.launch_playwright()
    
        openai = OpenAIModule()

        if("demo" in self._url):
            strategy = AudioCaptchaStrategy(playwright, openai, self._url)
            self._page_strategy = DemoStrategy(playwright, strategy)

    async def vulnerate_content(self):
        if self._page_strategy:
            await self._page_strategy.vulnerate_page()
            await self._page_strategy.submit_form()

            content = await self._page_strategy.get_content()

            return content
        else:
            print("No strategy set!")
    

        
