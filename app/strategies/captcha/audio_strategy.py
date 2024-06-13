from ...shared.audio import save_audio
from ...strategies.captcha.base import CaptchaStrategy
from ...clients.playwright import PlaywrightModule
from ...clients.openai import OpenAIModule

class AudioCaptchaStrategy(CaptchaStrategy):
    def __init__(self, playwright: PlaywrightModule, openai: OpenAIModule, url: str):
        super().__init__(playwright, url)
        self._openai = openai
        self._captcha_modal_locator = 'iframe[title="recaptcha challenge expires in two minutes"]'
        self._captcha_frame_locator = 'iframe[role="presentation"][title="reCAPTCHA"]'

    async def bypass_captcha(self):
        # TODO: Add error handler
        await self._page.goto(self._url)
        
        captcha = self._page.frame_locator(self._captcha_frame_locator).first.locator('[class="recaptcha-checkbox-border"]')
        
        print("captcha click")
        await captcha.click()
        
        audio_button = self._page.frame_locator(self._captcha_modal_locator).locator('#recaptcha-audio-button')
        print("audio click")

        await audio_button.click()
        
        play_button = self._page.frame_locator(self._captcha_modal_locator).get_by_label("Press PLAY to listen")
        
        print("play click")
        await play_button.click()
        
        audio_source = await self._page.frame_locator(self._captcha_modal_locator).locator('#audio-source').get_attribute('src')
        
        path = save_audio(audio_source)

        transcription = await self._openai.transcribe_audio(path=path)

        print("transcription")

        await self._page.frame_locator(self._captcha_modal_locator).locator('#audio-response').fill(transcription)

        await self._page.keyboard.press("Enter")

        return True
