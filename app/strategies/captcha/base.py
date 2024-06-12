from abc import ABC, abstractmethod
from playwright.async_api import Playwright

class CaptchaStrategy(ABC):
    def __init__(self, playwright: Playwright, url: str):
        self._page = playwright._page
        self._browser = playwright._browser
        self._url = url

    @abstractmethod
    async def bypass_captcha(self):
        pass
