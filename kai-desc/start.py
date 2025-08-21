import queue, sys, json
import sounddevice as sd
from vosk import Model, KaldiRecognizer

MODEL_PATH = "vosk-model/vosk-model-ru-0.10"

model = Model(MODEL_PATH)
rec = KaldiRecognizer(model, 16000)
q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    print("Говори…")
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            if res.get("text"):
                print("Распознано:", res["text"])
        else:
            # промежуточные результаты (по желанию)
            pass

'''def main():
    pass

if __name__ == '__main__':
    main()'''