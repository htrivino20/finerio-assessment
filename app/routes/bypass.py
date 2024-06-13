import logging
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse

from ..provider.browser import BrowserProvider
from ..provider.container import app_container

router = APIRouter()


async def get_content(url: str):
    provider = app_container[BrowserProvider]

    await provider.init_bypass_strategy(url)

    content = await provider.get_content_with_captcha_handling(url)

    return content


@router.get("/bypass/")
async def bypass_captcha(url: str):
    """
    This function handles requests to bypass captcha for a given URL.
    """
    try:
        content = await get_content(url)

        return HTMLResponse(content=content, status_code=200)
    except Exception as exception:
        logging.error("Error at %s", "division", exc_info=exception)
        return JSONResponse({"message": "An error occurred"})
