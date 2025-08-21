import fasttext
import numpy as np

class ParceCommand:
    def __init__(self, cmd: str):
        self.cmd = cmd
        self.model = fasttext.load_model("ai_models/commands_model.bin")

        self.command_methods = {
            "say_hallo": self.say_hallo,
        }

    def parce(self):
        labels, probabilities = self.model.predict(self.cmd)
        labels = [label.replace("__label__", "") for label in labels]
        probabilities = np.asarray(probabilities)

        if not labels: return

        if labels[0] in self.command_methods:
            self.command_methods[labels[0]]()
        else:
            print("Команда не найдена")

    def say_hallo(self):
        print('FASTTEXT - HALLO')