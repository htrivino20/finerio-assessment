from ...strategies.pages.base import PageStrategy


class DemoStrategy(PageStrategy):
    """
    Concrete subclass of PageStrategy implementing basic form submission and content retrieval.

    This strategy demonstrates a basic implementation for submitting forms and retrieving
    page content using testing pages.
    """

    async def submit_form(self):
        """
        Submits the form on the current web page.
        """
        return await self._page.locator("[type=submit]").click()

    async def get_content(self):
        """
        Retrieves the entire content of the current web page.
        """
        return await self._page.content()

    async def vulnerate_page(self, url: str):
        """
        Attempts to bypass CAPTCHA using the injected CaptchaStrategy (if provided).
        """
        return await self._strategy.bypass_captcha(url)
