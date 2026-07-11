import json
from pathlib import Path


MODE_FILE = Path("../memory/context.json")


def load_mode():

    if not MODE_FILE.exists():
        return "general"

    with open(MODE_FILE, "r") as file:
        data = json.load(file)

    return data.get("mode", "general")


def set_mode(mode):

    with open(MODE_FILE, "w") as file:
        json.dump(
            {
                "mode": mode
            },
            file,
            indent=2
        )


def get_mode():

    return load_mode()


def show_mode():

    print("\n🐼 CURRENT PANDA MODE")
    print("--------------------")
    print(f"Mode: {get_mode()}")