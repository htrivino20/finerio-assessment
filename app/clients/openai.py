from openai import AsyncOpenAI
import os
class OpenAIModule:
    def __init__(self):
        self._client = AsyncOpenAI(
            api_key=os.environ['OPENAI_API_KEY']
        )

    async def transcribe_audio(self, path: str):
        audio_file= open(path, "rb")
        transcription = await self._client.audio.transcriptions.create(
            model = "whisper-1", 
            file = audio_file
        )

        return transcription.text