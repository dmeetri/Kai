from pydoc import text
import re

class ParceCommand:
    def __init__(self, cmd: str):
        parts = re.split(r'\b(и|потом)\b', cmd, flags=re.IGNORECASE)
        parts = [p.strip() for p in parts if p.strip() and p.lower() not in ['и', 'потом']]
        self.command_list = [p.split() for p in parts]
    
    def _parce(self):
        for one_cmd_list in self.command_list:
            pass

    @property
    def run(self):
        for one_cmd_list in self.command_list:
            print(one_cmd_list)