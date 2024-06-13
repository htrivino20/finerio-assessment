import logging
from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse, JSONResponse

from ..provider.browser import BrowserProvider
from ..provider.container import app_container
from ..repository.content import ContentRepository
from ..repository.browser_content import BrowserContentRepository


router = APIRouter()


def get_content_repository() -> ContentRepository:
    return BrowserContentRepository(app_container[BrowserProvider])


@router.get("/bypass/")
async def bypass_captcha(
    url: str, content_repository: ContentRepository = Depends(get_content_repository)
):
    """
    This function handles requests to bypass captcha for a given URL.
    """
    try:
        content = await content_repository.get_content_with_captcha_handling(url)

        return HTMLResponse(content=content, status_code=200)
    except Exception as exception:
        logging.error("Error at %s", exc_info=exception)
        return JSONResponse({"message": "An error occurred"})
