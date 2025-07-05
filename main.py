import json
import os

# Load world
with open("world.json", "r") as f:
    world = json.load(f)

# Player state
player = {
    "location": "start",
    "inventory": []
}

def save_game():
    with open("savegame.json", "w") as f:
        json.dump(player, f)
    print("Game saved!")

def load_game():
    global player
    if os.path.exists("savegame.json"):
        with open("savegame.json", "r") as f:
            player.update(json.load(f))
        print("Game loaded!")
    else:
        print("No saved game found.")

def describe_location():
    loc = player["location"]
    print(f"\n{world[loc]['name']}")
    print(world[loc]["desc"])
    if "items" in world[loc]:
        print("You see:", ", ".join(world[loc]["items"]))
    print("Exits:", ", ".join(world[loc]["exits"].keys()))

def move(direction):
    loc = player["location"]
    if direction in world[loc]["exits"]:
        player["location"] = world[loc]["exits"][direction]
        describe_location()
    else:
        print("You can't go that way.")

def get_command():
    return input("\n> ").strip().lower().split()

def game_loop():
    print("Welcome to Terminal Quest! Type 'help' for commands.")
    describe_location()
    while True:
        cmd = get_command()
        if not cmd:
            continue
        if cmd[0] == "go" and len(cmd) > 1:
            move(cmd[1])
        elif cmd[0] == "look":
            describe_location()
        elif cmd[0] == "save":
            save_game()
        elif cmd[0] == "load":
            load_game()
            describe_location()
        elif cmd[0] == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Try: go, look, save, load, quit")

if __name__ == "__main__":
    game_loop()