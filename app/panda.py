from dashboard import show_dashboard
from idea_vault import save_idea, show_ideas
from creator import creator_mode
from context import set_mode, show_mode
from commands import show_commands
from goal_tracker import show_progress, complete_video
from content_generator import generate_content
from personality import (
    WELCOME_MESSAGE,
    UNKNOWN_COMMAND,
    GOODBYE_MESSAGE,
    BUILDING_MESSAGE,
)
import json
from pathlib import Path
from datetime import datetime

MEMORY_FILE = Path("../memory/memories.json")


def load_memory():
    with open(MEMORY_FILE, "r") as file:
        return json.load(file)


def save_memory(data):
    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=2)


def show_memory():
    data = load_memory()

    print("\n🐼 PANDA MEMORY VAULT")
    print("--------------------")

    count = 1

    for memory in data["memories"]:

        memory_type = memory.get("type", "memory")

        if memory_type == "creator_idea":
            icon = "🎮"
            label = "Creator Idea"
        else:
            icon = "🧠"
            label = "Memory"

        print(f"\n{count}. {icon} {label}")
        print(f"   {memory['content']}")

        count += 1


def add_memory(content):

    if not content.strip():
        print("🐼 Panda: I can't save an empty memory.")
        return

    data = load_memory()

    new_memory = {
        "type": "note",
        "title": "New Memory",
        "content": content,
        "date_created": str(datetime.now())
    }

    data["memories"].append(new_memory)

    save_memory(data)

    print("🐼 Panda: Memory saved.")


def start_panda():

    print(WELCOME_MESSAGE)
    print(BUILDING_MESSAGE)
    print("Commands: remember | memories | exit")

    while True:

        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print(GOODBYE_MESSAGE)
            break
        elif user_input.lower() == "mode":
            show_mode()
        elif user_input.lower().startswith("remember"):
            memory = user_input.replace("remember", "").strip()
            add_memory(memory)

        elif user_input.lower() == "memories":
            show_memory()
        
        elif user_input.lower() == "help":
            show_commands()
        
        elif user_input.lower() == "creator":
            set_mode("Creator")
            creator_mode()
        elif user_input.lower() == "generate":
            generate_content()
        elif user_input.lower() == "dashboard":
            set_mode("Dashboard")
            show_dashboard()
        elif user_input.lower() == "idea":
            save_idea()
        elif user_input.lower() == "progress":
            show_progress()

        elif user_input.lower() == "complete":
            complete_video()
        
        elif user_input.lower() == "ideas":
            show_ideas()
        else:
            print(UNKNOWN_COMMAND)


if __name__ == "__main__":
    start_panda()