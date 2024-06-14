from abc import ABC, abstractmethod


class CaptchaStrategy(ABC):
    @abstractmethod
    async def bypass_captcha(self, url: str):
        """
        Bypasses the CAPTCHA challenge. This method needs to be implemented by concrete subclasses
        to handle specific CAPTCHA types (audio and image recognition, click challenges, etc.).
        """
        raise NotImplementedError("bypass_captcha not implemented in base class")
