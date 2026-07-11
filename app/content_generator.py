from idea_vault import load_memory


def generate_content():

    print("\n🎬 PANDA CONTENT GENERATOR")
    print("-------------------------")

    print("\n1. Create from new idea")
    print("2. Use saved idea")

    choice = input("\nChoice: ")

    idea = ""

    if choice == "1":

        idea = input("\nWhat is your video idea?\n> ")

    elif choice == "2":

        data = load_memory()

        ideas = []

        for memory in data["memories"]:
            if memory.get("type") == "creator_idea":
                ideas.append(memory["content"])

        if len(ideas) == 0:
            print("\n🐼 No saved ideas yet.")
            return

        print("\n🎮 Your Creator Vault:")

        for index, item in enumerate(ideas, start=1):
            print(f"{index}. {item}")

        selected = input("\nChoose idea number: ")

        try:
            idea = ideas[int(selected)-1]

        except:
            print("🐼 Invalid choice.")
            return

    else:
        print("🐼 I don't understand that choice.")
        return


    print("\n🐼 Creating your video package...")
    print("-------------------------------")

    print("\n🎯 Title:")
    print(f"When {idea} Happens 😂")

    print("\n🔥 Hook:")
    print("You need to see what happens at the end...")

    print("\n📝 Description:")
    print(f"A gaming moment featuring: {idea}")

    print("\n#️⃣ Hashtags:")
    print("#Gaming #FunnyGaming #PandaManz413")

    print("\n🎥 Structure:")
    print("0-3 seconds: Grab attention")
    print("3-20 seconds: Show the moment")
    print("End: Give viewers a reason to follow")