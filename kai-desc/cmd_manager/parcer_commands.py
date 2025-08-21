import fasttext
import numpy as np

class ParceCommand:
    def __init__(self, cmd: str):
        self.cmd = cmd
        self.model = fasttext.load_model("ai_models/commands_model.bin")

    def parce(self):
        labels, probabilities = self.model.predict(self.cmd)
        probabilities = np.asarray(probabilities)
        print(f"FAST - {labels}, {probabilities}")

    def say_hallo(self):
        print('FASTTEXT - HALLO')