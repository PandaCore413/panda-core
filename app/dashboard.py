from idea_vault import load_memory


def show_dashboard():

    data = load_memory()

    ideas = 0
    latest_idea = None

    for memory in data["memories"]:

        if memory.get("type") == "creator_idea":
            ideas += 1
            latest_idea = memory["content"]

    print("\n🐼 PANDA CORE DASHBOARD")
    print("----------------------")

    print("\nWelcome back, Manny.")

    print("\n🎮 CREATOR STATS")
    print("----------------")

    print(f"Ideas Saved: {ideas}")

    if latest_idea:
        print("\nLatest Creator Idea:")
        print(latest_idea)

    print("\n🚀 Missions:")
    print("🎥 Create content")
    print("💡 Save new ideas")
    print("🎮 Grow PandaManz413")