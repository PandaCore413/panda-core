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


def save_idea():

    data = load_memory()

    print("\n💡 CREATOR IDEA VAULT")
    print("--------------------")

    idea = input("What's your content idea?\n> ")

    new_idea = {
        "type": "creator_idea",
        "title": "Content Idea",
        "content": idea,
        "date_created": str(datetime.now())
    }

    data["memories"].append(new_idea)

    save_memory(data)

    print("\n🐼 Panda: Idea saved to your Creator Vault.")


def show_ideas():

    data = load_memory()

    print("\n💡 YOUR CREATOR VAULT")
    print("--------------------")

    found = False

    for memory in data["memories"]:

        if memory.get("type") == "creator_idea":
            found = True
            print("\n🎮 " + memory["content"])

    if not found:
        print("\nNo creator ideas saved yet.")