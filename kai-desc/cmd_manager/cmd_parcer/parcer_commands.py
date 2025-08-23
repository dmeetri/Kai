import re

from .commands import *

class ParceCommand:
    def __init__(self, cmd: str):
        parts = re.split(r'\b(и|потом)\b', cmd, flags=re.IGNORECASE)
        parts = [p.strip() for p in parts if p.strip() and p.lower() not in ['и', 'потом']]
        self.command_list = [p.split() for p in parts]
    
    def _parce(self):
        for one_cmd_list in self.command_list:
            for keywords, func in open.items():
                #if any(word in one_cmd_list for word in keywords):
                match = next((word for word in keywords if word in one_cmd_list), None)
                if match:
                    idx = one_cmd_list.index(match) + 1
                    func(one_cmd_list[idx])
                    break
            else:
                print("Command not found")

    @property
    def run(self):
        self._parce()