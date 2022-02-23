class CmdHandler():

    def __init__(self, voice):
        self.voice = voice
        pass

    def handle_command(self, cmd):
        if cmd == 'you awake' or cmd == 'you there':
            self.voice.say('Hello, how can I assist you?')

        # TTS commands
        elif cmd == "what\'s the weather":
            # It is currently __ degress and <description>. There's a high of __ and low of ___.
            pass

        elif cmd == "what\'s the temperature":
            # Return temperature in the current room
            pass

        elif cmd.startswith('show me '):
            # the weather
            # the security cameras
            # Otherwise duckduckgo.com it
            pass

        elif cmd == 'send ___ to my phone':
            # this -- use last saved link
            # directions to ___ to my phone
            pass

        elif cmd.startswith('find my '):
            # phone
            # keys
            # watch
            pass

        elif cmd == "mute":
            pass
        elif cmd == "play":
            pass
        elif cmd == "pause":
            pass

        # Catch all if no command found
        else:
            self.voice.say("Sorry, I don't have a protocol for that.")
