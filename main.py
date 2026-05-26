import sys
import config
# Import everything from ./modules
from modules import audio, stt, cmd, llm, tts

def main():
    # Hello phrase on service start
    tts.speak("All systems operational, sir. How can I help you today?")
    
    try:
        while True:
            # 1. Capturing the mic audio (not cycling while the user is silent)
            raw_audio = audio.listen_voice()
            if not raw_audio:
                continue
                
            # 2. Audio to text with local Whisper
            user_text = stt.transcribe(raw_audio)
            if not user_text:
                continue
                
            print(f"\n[You said]: {user_text}")
            
            # Lower-casing before comparing with wakewords
            text_lower = user_text.lower()
            
            # 3. if called only by "Jarvis"
            if any(word in text_lower for word in config.WAKE_WORDS):
                print("[Wake Word Activation]")
                
                # Removing the assistent's name from the query
                clean_query = text_lower
                for word in config.WAKE_WORDS:
                    clean_query = clean_query.replace(word, "")
                clean_query = clean_query.strip()
                
                # Jarvis will wait for a request if only called by name
                if not clean_query:
                    tts.speak("At your service, sir.")
                    continue
                    
                print(f"[Обработка команды]: {clean_query}")
                
                # 4. Try to go the hardcode way
                if commands.handle_command(clean_query):
                    print("[Команда успешно выполнена через локальный код]")
                    continue
                
                # 5. if no matching bechaviour in cmd.py — inquire LM Studio / Ollama
                print("[Системный триггер не найден. Отправка в LLM...]")
                ai_response = llm.ask_jarvis(clean_query)
                
                # Verbouzing the AI's response
                tts.speak(ai_response)
                
    except KeyboardInterrupt:
        # Correct Ctrl+C exit in terminal
        print("\n[System exit. Have a nice day, sir.]")
        sys.exit(0)

if __name__ == "__main__":
    main()
