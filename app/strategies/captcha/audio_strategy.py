from app.shared.utils import Utils
from app.strategies.captcha.base import CaptchaStrategy
from app.clients.playwright import PlaywrightModule
from app.clients.openai import OpenAIModule


class AudioCaptchaStrategy(CaptchaStrategy):
    """
    Concrete subclass of CaptchaStrategy for handling audio-based CAPTCHAs.
    """

    def __init__(
        self, playwright: PlaywrightModule, openai: OpenAIModule, utils: Utils
    ):
        """
        Initializes the AudioCaptchaStrategy with Playwright and OpenAI instances, and
        the target URL.
        """
        self._page = playwright.page
        self._utils = utils
        self._openai = openai
        self._captcha_modal_locator = (
            'iframe[title="recaptcha challenge expires in two minutes"]'
        )
        self._captcha_frame_locator = 'iframe[role="presentation"][title="reCAPTCHA"]'

    async def bypass_captcha(self, url: str):
        """
        Attempts to bypass an audio-based CAPTCHA challenge.

        This method interacts with the website using Playwright, retrieves the audio challenge,
        transcribes it using OpenAI, and fills the response field with the transcription.
        """
        await self._page.goto(url)

        # Find and click the checkbox element within the CAPTCHA frame
        captcha = self._page.frame_locator(self._captcha_frame_locator).first.locator(
            '[class="recaptcha-checkbox-border"]'
        )
        await captcha.click()

        # Click the audio button to play the CAPTCHA challenge
        audio_button = self._page.frame_locator(self._captcha_modal_locator).locator(
            "#recaptcha-audio-button"
        )
        await audio_button.click()

        # Click the "Press PLAY to listen" button
        play_button = self._page.frame_locator(
            self._captcha_modal_locator
        ).get_by_label("Press PLAY to listen")
        await play_button.click()

        # Retrieve the audio source URL
        audio_source = (
            await self._page.frame_locator(self._captcha_modal_locator)
            .locator("#audio-source")
            .get_attribute("src")
        )

        # Download and save the audio file using the assumed function from shared.audio
        path = self._utils.save_audio(audio_source)

        # Transcribe the downloaded audio using the OpenAI client
        transcription = await self._openai.transcribe_audio(path=path)

        # Fill the CAPTCHA response field with the transcribed text
        captcha_input = self._page.frame_locator(self._captcha_modal_locator).locator(
            "#audio-response"
        )
        await captcha_input.fill(transcription)

        # Submit the CAPTCHA solution by pressing "Enter"
        await self._page.keyboard.press("Enter")

        return True
