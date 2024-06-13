from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from ..provider.browser import BrowserProvider

router = APIRouter()


@router.get("/bypass/")
async def handle_captcha_bypass(url: str):
    """
    This function handles requests to bypass captcha for a given URL.
    """
    provider = BrowserProvider(url)
    provider = await provider.init_bypass_strategy()

    content = await provider.get_content_with_captcha_handling()

    return HTMLResponse(content=content, status_code=200)
