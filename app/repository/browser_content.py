from ..repository.content import ContentRepository
from ..provider.browser import BrowserProvider


class BrowserContentRepository(ContentRepository):
    def __init__(self, browser_provider: BrowserProvider):
        self.browser_provider = browser_provider

    async def get_content_with_captcha_handling(self, url: str) -> str:
        provider = await self.browser_provider.init_bypass_strategy(url)
        content = await provider.get_content_with_captcha_handling(url)
        return content
