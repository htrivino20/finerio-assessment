class ContentRepository:
    async def get_content_with_captcha_handling(self, url: str) -> str:
        raise NotImplementedError
