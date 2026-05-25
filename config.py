import os
from pathlib import Path

# defining project's root (no matter where from it was lauched)
BASE_DIR = Path(__file__).resolve().parent

# audio settings
SAMPLING_RATE = 16000 #whisper's default freq, 16kHz
AUDIO_TEMP_FILE = str(BASE_DIR / "temp_vioce.wav")

# ai settings
WHISPER_MODEL_SIZE = "base"
LLM_MODEL = "llama3"
LLM_URL = "http://localhost:11434/v1"

# lingo
WAKE_WORDS = ["джарвис", "jarvis"]

SYSTEM_PROMT = (
    "You are Jarvis, a brilliant, concise AI assitent. "
    "Answer short and summary-focused, unless specified otherwise. Use English or Russian depending on the user's input."
)
