from abc import ABC, abstractmethod
from ...strategies.captcha.base import CaptchaStrategy
from ...clients.playwright import PlaywrightModule

class PageStrategy(ABC):
    def __init__(self, playwright: PlaywrightModule, strategy: CaptchaStrategy):
        self._page = playwright._page
        self._browser = playwright._browser
        self._strategy = strategy

    @abstractmethod
    async def submit_form(self):
        pass
    
    @abstractmethod
    async def get_content(self):
        pass

    @abstractmethod
    async def vulnerate_page(self):
        pass

    async def close_browser(self):
        return await self._browser.close()
