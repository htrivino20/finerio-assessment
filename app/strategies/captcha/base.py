from abc import ABC, abstractmethod
from playwright.async_api import Playwright


class CaptchaStrategy(ABC):
    def __init__(self, playwright: Playwright, url: str):
        """
        Initializes the CaptchaStrategy with Playwright instance and target URL.
        """
        if not url:
            raise ValueError("Missing target URL")

        self._page = playwright._page
        self._browser = playwright._browser
        self._url = url

    @abstractmethod
    async def bypass_captcha(self):
        """
        Bypasses the CAPTCHA challenge. This method needs to be implemented by concrete subclasses
        to handle specific CAPTCHA types (audio and image recognition, click challenges, etc.).
        """
        raise NotImplementedError("bypass_captcha not implemented in base class")
