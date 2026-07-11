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

    print("\n🐼 PANDA CORE MEMORY")
    print("-------------------")

    for memory in data["memories"]:
        print(f"\n{memory['title']}")
        print(memory["content"])


def add_memory(content):
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

    print("🐼 PANDA CORE ONLINE")
    print("-------------------")
    print("Hello Manny. What would you like me to do?")
    print("Commands: remember | memories | exit")

    while True:

        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("🐼 Panda: Shutting down. See you soon, Manny.")
            break

        elif user_input.lower().startswith("remember"):
            memory = user_input.replace("remember", "").strip()
            add_memory(memory)

        elif user_input.lower() == "memories":
            show_memory()

        else:
            print("🐼 Panda: I don't understand that yet, but I'm learning.")


if __name__ == "__main__":
    start_panda()