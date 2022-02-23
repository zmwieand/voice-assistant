from src.commands import CmdHandler
from src.speech import Speech
from src.voice import Voice


def main():
    s = Speech()
    v = Voice()
    cmd_handler = CmdHandler(v)

    print('Waiting for input...')
    cmd = s.wait_for_speech(phrase_limit=5)
    print(f'Cmd: {cmd}')


if __name__ == '__main__':
    main()
