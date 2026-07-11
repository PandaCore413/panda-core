import json
from pathlib import Path

MEMORY_FILE = Path("../memory/memories.json")


def load_memory():
    with open(MEMORY_FILE, "r") as file:
        return json.load(file)


def show_memory():
    data = load_memory()

    print("🐼 PANDA CORE MEMORY")
    print("-------------------")

    for memory in data["memories"]:
        print(f"{memory['title']}:")
        print(memory["content"])
        print()


if __name__ == "__main__":
    show_memory()