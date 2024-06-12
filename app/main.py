from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from .provider.browser import BrowserProvider

app = FastAPI()

async def run_browser(url: str):
    provider = BrowserProvider(url)

    await provider.init_bypass_strategy()

    content = await provider.vulnerate_content()

    return HTMLResponse(content=content, status_code=200)

@app.get("/bypass/")
async def handle_captcha_bypass(url: str):
    return await run_browser(url)
