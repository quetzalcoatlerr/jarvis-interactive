import pyttsx3

# Initiating the TTS system
_engine = pyttsx3.init()

# Speech speech
_engine.setProperty('rate', 180) 
# Volume settings (0.0 - 1.0)
_engine.setProperty('volume', 1.0)

def speak(text: str):
    print(f"Jarvis: {text}")
    
    # Queueing
    _engine.say(text)
    # Block until the speaker finishes
    _engine.runAndWait()
