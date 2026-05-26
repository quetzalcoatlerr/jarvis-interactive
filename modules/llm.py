from openai import OpenAI
import config

# Connecting to local Ollama server. 
# Ollama emulates OpenAI API out of the box.
_client = OpenAI(
    base_url=config.LLM_URL, 
    api_key="ollama"  # API-key can be anyting
)

def ask_jarvis(prompt: str) -> str:
    # Sends a query to the llm and returns the response
    try:
        # Create a chat-session
        response = _client.chat.completions.create(
            model=config.LLM_MODEL,
            messages=[
                # Role system defines the model's behavior at root
                {"role": "system", "content": config.SYSTEM_PROMPT},
                # Role user — your promt
                {"role": "user", "content": prompt}
            ],
            # Creativity control.
            temperature=0.4 
        )
        return response.choices[0].message.content
        
    except Exception as e:
        return f"Sir, I encountered a mistake while refering to the local llm: {e}"
