from ...strategies.pages.base import PageStrategy
from playwright.async_api import Page
from ...strategies.captcha.base import CaptchaStrategy

class DemoStrategy(PageStrategy):
    def __init__(self, page: Page, strategy: CaptchaStrategy):
        super().__init__(page, strategy)

    async def submit_form(self):
        return await self._page.locator('[type=submit]').click()
    
    async def get_content(self):
        return await self._page.content()
    
    async def vulnerate_page(self):
        return await self._strategy.bypass_captcha()