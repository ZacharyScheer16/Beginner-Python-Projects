import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

# --- Player setup ---
while True:
    player = input("Enter number of players (2-4): ")
    if player.isdigit():
        player = int(player)
        if 2 <= player <= 4:
            break
        else:
            print("Must be between two and four players.")
    else:
        print("Invalid input. Try again.")

print(f"\nStarting game with {player} players!\n")

# --- Game setup ---
max_score = 50
player_scores = [0 for _ in range(player)]

# --- Game loop ---
while max(player_scores) < max_score:
    for player_idx in range(player):
        print(f"\n--- Player {player_idx + 1}'s turn ---")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y/n)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn over, no points this round.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}. Current round score: {current_score}")

        # Add round score to total score
        player_scores[player_idx] += current_score
        print(f"Player {player_idx + 1}'s total score: {player_scores[player_idx]}")

        # Check for winner
        if player_scores[player_idx] >= max_score:
            print(f"\n🎉 Player {player_idx + 1} wins with {player_scores[player_idx]} points! 🎉")
            break

    # Stop outer loop if there’s a winner
    if max(player_scores) >= max_score:
        break

print("\nFinal scores:")
for i, score in enumerate(player_scores):
    print(f"Player {i + 1}: {score}")
print("Game over!")
