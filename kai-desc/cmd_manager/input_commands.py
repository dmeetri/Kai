import queue, sys, json
import sounddevice as sd
from vosk import Model, KaldiRecognizer

from .parcer_commands import ParceCommand

class InputCommands:
    def __init__(self):
        self.model = Model("vosk-model/vosk-model-ru-0.10")
        self.rec = KaldiRecognizer(self.model, 16000)
        self.q = queue.Queue()

    def _callback(self, indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(indata))
    
    def voice_input(self):
        with sd.RawInputStream(samplerate=16000, blocksize=4000, dtype="int16", channels=1, callback=self._callback):
            print("Speaking…")

            while True:
                data = self.q.get()
                if self.rec.AcceptWaveform(data):
                    res = json.loads(self.rec.Result())
                    if res.get("text"):
                        print("You", res["text"])
                        
                        pc = ParceCommand(res["text"])
                        pc.parce()
                else:
                    pass