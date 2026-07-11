COMMANDS = {
    "remember": "Save a new memory",
    "memories": "Show all memories",
    "creator": "Creator Mode",
    "business": "Business Mode",
    "idea": "Save a creator idea",
    "ideas": "Show creator ideas",
    "dashboard": "Show Creator Dashboard",
    "help": "Show available commands",
    "exit": "Exit Panda"
}


def show_commands():
    print("\n🐼 Available Commands\n")

    for command, description in COMMANDS.items():
        print(f"{command:<10} - {description}")