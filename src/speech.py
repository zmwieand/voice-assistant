import pyaudio
import speech_recognition as sr

class Speech():
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        # TODO: This will need to be 1 on the pi
        self.microphone_index = 0

    def wait_for_speech(self, phrase_limit=2):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source, phrase_time_limit=phrase_limit)

        try:
            text = self.recognizer.recognize_google(audio)
            return text
        except:
            return None
