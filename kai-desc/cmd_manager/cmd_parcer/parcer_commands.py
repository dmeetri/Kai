import re
import pymorphy2

from .commands import *

class ParceCommand:
    def __init__(self, cmd: str):
        self.morph = pymorphy2.MorphAnalyzer()
        parts = re.split(r'\b(и|потом)\b', cmd, flags=re.IGNORECASE)
        parts = [p.strip() for p in parts if p.strip() and p.lower() not in ['и', 'потом']]
        self.command_list = [p.split() for p in parts]

    @property
    def run(self):
        for one_cmd_list in self.command_list:
            action = next((w for w in one_cmd_list if self.morph.parse(w)[0].normal_form in open_cmds), None)

            object_words = []
            for w in one_cmd_list:
                if w not in stopwords:
                    parsed = self.morph.parse(w)[0]
                    if parsed.tag.POS == "NOUN":
                        object_words.append(w)

            object_text = " ".join(object_words)

            print("Действие:", action)
            print("Объект:", object_text)
