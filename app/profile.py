import json
from pathlib import Path


PROFILE_FILE = Path("../memory/profile.json")


def load_profile():

    with open(PROFILE_FILE, "r") as file:
        return json.load(file)


def show_profile():

    profile = load_profile()

    print("\n🐼 PANDA PROFILE")
    print("----------------")

    print(f"Name: {profile['name']}")
    print(f"Creator Brand: {profile['creator_brand']}")

    print("\nPlatforms:")

    for platform in profile["platforms"]:
        print(f"🎥 {platform}")

    print("\nContent Style:")

    for style in profile["content_style"]:
        print(f"🎮 {style}")

    print("\nMission:")
    print(profile["mission"])