import os
import urllib.request

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'AudioBypass/1.0')]
urllib.request.install_opener(opener)

def save_audio(source):
    audio_path = os.getcwd() + '/tmp/audio.mp3'

    print(source, audio_path)
    urllib.request.urlretrieve(source, audio_path)

    return audio_path