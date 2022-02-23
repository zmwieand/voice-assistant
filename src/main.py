import speech_recognition as sr

from commands import CmdHandler
from speech import Speech
from voice import Voice


# TODO: Make this a settings thing
HOTWORD = 'Gideon'


def extract_cmd(text):
    """
    Returns text that comes after the HOTWORD
    """
    starting_index = text.find(HOTWORD)
    # Add 1 for space character
    ending_index = starting_index + len(HOTWORD) + 1

    return text[ending_index:]


def main():
    s = Speech()
    v = Voice()
    cmd_handler = CmdHandler(v)

    while True:
        print('Waiting for Hotword...')
        text = s.wait_for_speech()

        if text == None:
            print('')
            continue

        elif text == HOTWORD:
            print('  Waiting for command...')
            v.say('Hello')
            cmd = s.wait_for_speech(phrase_limit=5)
            if cmd == None:
                print('')
                continue

            else:
                print(f'    CMD: "{cmd}"')

        print('')


if __name__ == '__main__':
    main()
