from abc import ABC, abstractmethod
from ...strategies.captcha.base import CaptchaStrategy
from ...clients.playwright import PlaywrightModule


class PageStrategy(ABC):
    """
    Abstract base class for defining strategies to interact with web pages using Playwright.
    """

    def __init__(self, playwright: PlaywrightModule, strategy: CaptchaStrategy):
        """
        Initializes the PageStrategy instance.
        """
        self._page = playwright._page
        self._browser = playwright._browser
        self._strategy = strategy

    @abstractmethod
    async def submit_form(self):
        """
        This method should handle the logic for submitting a form on the web page.
        """

    @abstractmethod
    async def get_content(self):
        """
        Abstract method to be implemented by concrete subclasses.
        """

    @abstractmethod
    async def vulnerate_page(self):
        """
        Abstract method to be implemented by concrete subclasses.
        """
