import os
import urllib.request

opener = urllib.request.build_opener()
opener.addheaders = [("User-Agent", "AudioBypass/1.0")]
urllib.request.install_opener(opener)


def save_audio(source):
    """
    Downloads and saves an audio file from the provided URL.

    This function takes a URL (source) as input and performs the following:

    1. Creates a temporary path for the downloaded audio file (audio.mp3) within a 'tmp' directory.
    2. Prints the source URL and the target audio path for informative logging.
    3. Uses urllib.request.urlretrieve to download the audio file from the source URL and save
    it to the created temporary path.
    4. Returns the path of the downloaded audio file.
    """

    audio_path = os.getcwd() + "/tmp/audio.mp3"

    urllib.request.urlretrieve(source, audio_path)

    return audio_path
