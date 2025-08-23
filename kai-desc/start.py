from cmd_manager import *

from cmd_manager.parcer_commands import ParceCommand

def main():
    cmd = input(">>> ")
    pcm = ParceCommand(cmd)
    pcm.run

    '''v = InputCommands()
    v.voice_input()'''

if __name__ == "__main__":
    main()