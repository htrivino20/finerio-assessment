from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
from .provider.browser import BrowserProvider

load_dotenv()

app = FastAPI()


async def run_browser(url: str):
    provider = BrowserProvider(url)
    provider = await provider.init_bypass_strategy()

    content = await provider.get_content_with_captcha_handling()

    return HTMLResponse(content=content, status_code=200)


@app.get("/bypass/")
async def handle_captcha_bypass(url: str):
    return await run_browser(url)
