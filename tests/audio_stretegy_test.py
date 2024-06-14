from unittest.mock import AsyncMock, MagicMock
import pytest
from app.shared.utils import Utils
from app.clients.playwright import PlaywrightModule
from app.clients.openai import OpenAIModule
from app.strategies.captcha.audio_strategy import AudioCaptchaStrategy


@pytest.fixture
def utils():
    module = MagicMock(spec=Utils)
    module.save_audio = MagicMock()
    return module


@pytest.fixture
def playwright():
    module = MagicMock(spec=PlaywrightModule)
    module.page = MagicMock()
    module.page.goto = AsyncMock()
    module.page.frame_locator = MagicMock()
    module.page.frame_locator.return_value.first.locator.return_value.click = (
        AsyncMock()
    )
    module.page.frame_locator.return_value.locator.return_value.click = AsyncMock()
    module.page.frame_locator.return_value.locator.return_value.get_attribute = (
        AsyncMock()
    )
    module.page.frame_locator.return_value.get_by_label.return_value.click = AsyncMock()
    module.page.frame_locator.return_value.locator.return_value.click = AsyncMock()
    module.page.frame_locator.return_value.locator.return_value.fill = AsyncMock()
    module.page.keyboard.press = AsyncMock()
    return module


@pytest.fixture
def openai():
    module = MagicMock(spec=OpenAIModule)
    module.transcribe_audio = AsyncMock()
    return module


@pytest.fixture
def audio_captcha_strategy(playwright, openai, utils):
    return AudioCaptchaStrategy(playwright=playwright, openai=openai, utils=utils)


@pytest.mark.asyncio
async def test_bypass_audio_captcha(audio_captcha_strategy, playwright, openai, utils):
    url = "https://example.com"
    audio_src_url = "audio_src.mp3"
    transcription_text = "test transcription"
    saved_audio_path = "/path/to/audio.mp3"

    playwright.page.frame_locator.return_value.locator.return_value.get_attribute.return_value = (
        audio_src_url
    )
    openai.transcribe_audio.return_value = transcription_text
    utils.save_audio.return_value = saved_audio_path

    result = await audio_captcha_strategy.bypass_captcha(url)

    # should call goto with given url
    playwright.page.goto.assert_awaited_with(url)

    # should locate recaptcha and click button
    playwright.page.frame_locator.return_value.first.locator.assert_called_with(
        '[class="recaptcha-checkbox-border"]'
    )
    playwright.page.frame_locator.return_value.first.locator.return_value.click.assert_awaited_with()

    # should locate play button and click
    assert playwright.page.frame_locator.return_value.locator.call_args_list[0] == [
        ("#recaptcha-audio-button",)
    ]
    playwright.page.frame_locator.return_value.get_by_label.assert_called_with(
        "Press PLAY to listen"
    )
    playwright.page.frame_locator.return_value.get_by_label.return_value.click.assert_awaited_with()

    # should locate audio source and get url
    assert playwright.page.frame_locator.return_value.locator.call_args_list[1] == [
        ("#audio-source",)
    ]
    playwright.page.frame_locator.return_value.locator.return_value.get_attribute.assert_called_with(
        "src"
    )

    # should save audio file
    utils.save_audio.assert_called_with(audio_src_url)

    # should transcribe audio
    openai.transcribe_audio.assert_awaited_with(path=saved_audio_path)

    # should fill the input with the transcription
    assert playwright.page.frame_locator.return_value.locator.call_args_list[2] == [
        ("#audio-response",)
    ]
    playwright.page.frame_locator.return_value.locator.return_value.fill.assert_awaited_with(
        transcription_text
    )

    # should press Enter
    playwright.page.keyboard.press.assert_awaited_with("Enter")

    assert result is True
