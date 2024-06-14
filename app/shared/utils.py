import os
import urllib.request

opener = urllib.request.build_opener()
opener.addheaders = [("User-Agent", "AudioBypass/1.0")]
urllib.request.install_opener(opener)


class Utils:
    def save_audio(self, source):
        """
        Downloads and saves an audio file from the provided URL.
        """
        audio_path = os.getcwd() + "/tmp/audio.mp3"

        urllib.request.urlretrieve(source, audio_path)

        return audio_path
