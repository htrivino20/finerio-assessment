import logging
import os
from openai import AsyncOpenAI


class OpenAIModule:
    def __init__(self):
        """
        Initializes the OpenAI client with the provided API key from the environment variable.
        """
        self._client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])

    async def transcribe_audio(self, path: str):
        """
        Transcribes an audio file using OpenAI's Whisper model.
        """
        try:
            with open(path, "rb") as audio_file:
                transcription = await self._client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                )
                return transcription.text
        except Exception as exception:
            # Handle error and potentially return an error message
            logging.error("Error at %s", exc_info=exception)
            return None
