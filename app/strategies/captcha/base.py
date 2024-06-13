from abc import ABC, abstractmethod
from playwright.async_api import Playwright
from ...shared.utils import Utils


class CaptchaStrategy(ABC):
    def __init__(self, playwright: Playwright, utils: Utils):
        """
        Initializes the CaptchaStrategy with Playwright instance and target URL.
        """
        self._page = playwright._page
        self._browser = playwright._browser
        self._utils = utils

    @abstractmethod
    async def bypass_captcha(self):
        """
        Bypasses the CAPTCHA challenge. This method needs to be implemented by concrete subclasses
        to handle specific CAPTCHA types (audio and image recognition, click challenges, etc.).
        """
        raise NotImplementedError("bypass_captcha not implemented in base class")
