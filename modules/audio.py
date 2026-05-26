import speech_recognition as sr
import config

def listen_voice():
    # recognizer initiation
    recognizer = sr.Recognizer()

    # silence sensitivity
    recognizer.pause_threshold = 0.8 # so many seconds of silence means end of input
    recognizer.non_speaking_duration = 0.5 # noize duration before speech

    # using the built-in Kubuntu mic
    with sr.Microphone(sample_rate=config.SAMPLING_RATE) as source:
        print("[Listening to the environment for noise calibration...]")
        # adapting to background noise
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        print("[Jarvis is here, sir]")
        try:
            audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            return audio_data
        except (sr.WaitTimeoutError, Exception):
            return None

