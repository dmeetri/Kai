from cmd_manager import *

from cmd_manager import ParceCommand

def main():
    while True:
        cmd = input(">>> ")
        pcm = ParceCommand(cmd)
        pcm.run()

    '''v = InputCommands()
    v.voice_input()'''

if __name__ == "__main__":
    main()