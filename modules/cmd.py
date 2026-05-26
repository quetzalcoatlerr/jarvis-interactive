import os
import sys

def handle_command(text: str) -> bool:
    # Gets filtered text.
    # Match -> execs the coomand through the ОS and returns True.
    # If no match, returns False (reroute to LLM)
    query = text.lower().strip()
    
    # CAT: Software launching
    if "открой браузер" in query or "open browser" in query:
        os.system("xdg-open https://github.com &")
        return True
        
    if "терминал" in query or "terminal" in query:
        # Lauch terminal emulator, I use default Kubuntu Konsole
        os.system("konsole &")
        return True

    # CAT: Syscalls
    if "выключи компьютер" in query or "shutdown system" in query:
        os.system("poweroff")
        return True

    # CAT: Custom scripts (automation)
    if "проверь контейнеры" in query or "docker status" in query:
        os.system("konsole -e 'docker ps; read' &")
        return True

    return False
