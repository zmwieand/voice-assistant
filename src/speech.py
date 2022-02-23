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

    # def wait_for_input(self):
    #     """
    #     Listens on mic for input. Returns STT on input or None if nothing said.
    #     """
    #     sample_rate = 44100
    #     chunk = 4096
    #     record_seconds = 5

    #     audio = pyaudio.PyAudio()
    #     stream = audio.open(
    #         format=pyaudio.paInt16,
    #         rate=sample_rate,
    #         channels=2,
    #         input_device_index=self.microphone_index,
    #         input=True,
    #         frames_per_buffer=chunk,
    #     )

    #     frames = []
    #     for _ in range(0, int((sample_rate / chunk) * record_seconds)):
    #         data = stream.read(chunk, exception_on_overflow = False)
    #         frames.append(data)

    #     # print(f'Num Frames: {len(frames)}')

    #     # Close audio streams
    #     stream.stop_stream()
    #     stream.close()
    #     audio.terminate()

    #     audio_bytes = b''.join(frames)
    #     audio_data = sr.AudioData(
    #         audio_bytes,
    #         sample_rate,
    #         audio.get_sample_size(pyaudio.paInt16)
    #     )

    #     # with mic as source:
    #     # recognizer.adjust_for_ambient_noise(source)
    #     # audio = recognizer.listen(source, phrase_time_limit=5)

    #     text = self.recognizer.recognize_google(audio_data)

    #     # try:
    #     #     text = self.recognizer.recognize_google(audio_data)
    #     #     return text
    #     # except:
    #     #     return None

    #     return text
