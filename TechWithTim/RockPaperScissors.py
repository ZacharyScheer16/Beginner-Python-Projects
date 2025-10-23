import random

user_wins = 0
cpuWins = 0

# The options list is the core logic:
# 0 = rock, 1 = paper, 2 = scissors
options = ["rock" , "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors! 🤜📜✂️")
print("-" * 30)

while True:
    user_Input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    # 1. Check for the exit condition
    if user_Input == "q":
        break

    # 2. Validate the user input
    if user_Input not in options:
        print("Invalid choice. Please type Rock, Paper, Scissors, or Q to quit.")
        continue

    # 3. CPU selects a random option
    random_number = random.randint(0, 2)
    cpuPick = options[random_number]
    print(f"CPU picked **{cpuPick}**.")

    # 4. Determine the winner (The Core Logic)

    # Check for a TIE
    if user_Input == cpuPick:
        print("It's a tie!")

    # Check for USER WINS
    elif (user_Input == "rock" and cpuPick == 'scissors'):
        print("You win! Rock smashes Scissors.")
        user_wins += 1
    elif (user_Input == "paper" and cpuPick == 'rock'):
        print("You win! Paper covers Rock.")
        user_wins += 1
    elif (user_Input == "scissors" and cpuPick == 'paper'):
        print("You win! Scissors cuts Paper.")
        user_wins += 1

    # If it's not a tie and the user didn't win, the CPU must win
    else:
        print("CPU wins this round.")
        cpuWins += 1

    print(f"Current Score: You: {user_wins} | CPU: {cpuWins}\n")
    print("-" * 30)

# Final Score and Goodbye
print("\n" + "=" * 30)
print(f"Final Score: You won {user_wins} times and the CPU won {cpuWins} times.")

# Determine the overall winner
if user_wins > cpuWins:
    print("🎉 Congratulations, you are the overall winner! 🎉")
elif cpuWins > user_wins:
    print("😔 Better luck next time, the CPU takes the victory. 😔")
else:
    print("🤝 It's a draw game! 🤝")

print("GoodBye!")
print("=" * 30)