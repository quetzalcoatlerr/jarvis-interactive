import os
import os
from faster_whisper import WhisperModel
import config

print("[Initiating Whisper...]")
# Loading the model ONCE on module import.
# device="cpu": launching on a cpu, write "cuda" instead to use your GPU.
# compute_type="int8": quaitification.
# Saving RAM and optimizing the cpu load.
_whisper_model = WhisperModel(
    config.WHISPER_MODEL_SIZE, 
    device="cpu", 
    compute_type="int8"
)

def transcribe(audio_data) -> str:
    #gets bites, returns a string
    if not audio_data:
        return ""

    try:
        # 1. Writing the bites into .wav for Whisper
        with open(config.AUDIO_TEMP_FILE, "wb") as f:
            f.write(audio_data.get_wav_data())

        # 2. Launching the model's inference
        # beam_size=5: algorithm for finding optimal text.
        segments, info = _whisper_model.transcribe(config.AUDIO_TEMP_FILE, beam_size=5)
        
        # The info automatically contains language data (e.g., 'ru' or 'en')
        # print(f"[Detected language: {info.language} with probability {info.language_probability:.2f}]")

        # Model returns segmented text. Glueing into a single string.
        final_text = "".join([segment.text for segment in segments]).strip()
        
        # 3. Cleaning the storage
        if os.path.exists(config.AUDIO_TEMP_FILE):
            os.remove(config.AUDIO_TEMP_FILE)
            
        return final_text

    except Exception as e:
        print(f"[STT module error]: {e}")
        return ""
