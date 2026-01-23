from intent_detector import detect_intent
from action_mapper import map_action
from droidrun_client import run_action
import voice_input


def show_banner():
    banner = r"""
 ██████╗ ██████╗ ██████╗ ███████╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝
██║     ██║   ██║██████╔╝█████╗  
██║     ██║   ██║██╔══██╗██╔══╝  
╚██████╗╚██████╔╝██║  ██║███████╗
 ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝

████████╗███████╗ █████╗ ███╗   ███╗
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
   ██║   █████╗  ███████║██╔████╔██║
   ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝

        🔥  CORE TEAM  🔥
-------------------------------------
 Voice Controlled Android Automation
-------------------------------------
"""
    print(banner)


def main():
    show_banner()

    while True:
        print("Bol bhai...")
        text = voice_input.listen()

        if not text:
            continue

        print(f"You said: {text}")

        intent = detect_intent(text)
        print(f"Intent: {intent}")

        action = map_action(intent, text)
        print(f"Action: {action}")

        result = run_action(action)
        print(f"Result: {result}")
        print("-" * 40)


if __name__ == "__main__":
    main()
