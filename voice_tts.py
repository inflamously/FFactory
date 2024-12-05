import torch
import os
from TTS.api import TTS


class XTTSVoice:
    def __init__(self, voice_pool=None):
        self.samples = []
        if not voice_pool is None:
            self.samples = self.__read_voice_pool(voice_pool)
        print("samples read for voice clone", self.samples[:3], "...")
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
        self.tts.tts_to_file(
            text="That was about the same time, as I learned to maintain. And it certainly raised the question: Do I follow this way or do I meditate?",
            speaker_wav=self.samples,
            language="en", file_path="output.wav")

    def __read_voice_pool(self, path):
        if os.path.exists(path):
            return list(map(lambda f: os.path.join(os.getcwd(), path, f), os.listdir(path)))
        else:
            return []


if __name__ == "__main__":
    voice = XTTSVoice(voice_pool="voice_pool\\grandpa")
