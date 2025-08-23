import re
import pymorphy2

from .commands import *

class ParceCommand:
    def __init__(self, cmd: str):
        self.morph = pymorphy2.MorphAnalyzer()
        self.cmd = cmd

    def run(self):
        parts = re.split(r'\b(и|потом)\b', self.cmd , flags=re.IGNORECASE)
        parts = [p.strip() for p in parts if p.strip() and p.lower() not in ['и', 'потом']]
        command_list = [p.split() for p in parts]

        for one_cmd_list in command_list:
            action = next((w for w in one_cmd_list if self.morph.parse(w)[0].normal_form in open_cmds), None)
            action = self.morph.parse(action)[0].normal_form if action else None

            object_words = []
            numbers = []

            for w in one_cmd_list:
                if w in stopwords:
                    continue

                parsed = self.morph.parse(w)[0]
                if parsed.tag.POS == "NOUN":
                    object_words.append(w)
                elif parsed.tag.POS == "NUMR" or w.isdigit():
                    numbers.append(w)

            object_text = " ".join(object_words)

            print("Your commands:")
            print("Действие:", action)
            print("Объект:", object_text)
            print("Аргументы:", numbers)