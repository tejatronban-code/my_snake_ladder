import random

# Snake positions (start: end)
snakes = {
    99: 54,
    70: 55,
    52: 42,
    25: 2
}

# Ladder positions (start: end)
ladders = {
    6: 25,
    11: 40,
    60: 85,
    46: 90
}

player_position = 0

def roll_dice():
    return random.randint(1, 6)

print("🎲 Welcome to Snake and Ladder 🎲")

while player_position < 100:
    input("\nPress Enter to roll the dice...")
    dice = roll_dice()
    print(f"You rolled: {dice}")

    player_position += dice

    if player_position > 100:
        player_position -= dice
        print("Roll exceeded 100. Stay at same position.")

    if player_position in snakes:
        print("🐍 Oh no! Snake bite!")
        player_position = snakes[player_position]

    elif player_position in ladders:
        print("🪜 Great! You climbed a ladder!")
        player_position = ladders[player_position]

    print(f"Your current position: {player_position}")

print("\n🏆 Congratulations! You won the game!")