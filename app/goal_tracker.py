import json
from pathlib import Path


GOAL_FILE = Path("../memory/goals.json")


def load_goals():

    if not GOAL_FILE.exists():

        return {
            "mission": "Grow PandaManz413",
            "videos_completed": 0,
            "uploads": 0
        }

    with open(GOAL_FILE, "r") as file:
        return json.load(file)


def save_goals(data):

    with open(GOAL_FILE, "w") as file:
        json.dump(data, file, indent=2)


def show_progress():

    goals = load_goals()

    print("\n🐼 PANDA CREATOR TRACKER")
    print("------------------------")

    print("\nMission:")
    print(goals["mission"])

    print("\n📊 Progress:")
    print(f"Videos Completed: {goals['videos_completed']}")
    print(f"Uploads: {goals['uploads']}")


def complete_video():

    goals = load_goals()

    goals["videos_completed"] += 1

    save_goals(goals)

    print("\n🐼 Panda: Video completed added! 🚀")