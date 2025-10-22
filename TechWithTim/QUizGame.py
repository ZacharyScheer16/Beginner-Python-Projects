print("Welcome to my computer quiz")

# Initialize the score variable
score = 0

playing = input("Do you want to play: ")
if playing.lower() != "yes":
    quit()

print("Ok lets play!")

# --- Question 1 ---
answer = input(" What does CPU stand for: ").lower()
if answer == "central processing unit":
    print("Correct! ✅")
    score += 1  # Add a point
else:
    print("Incorrect. ❌")

# --- Question 2 ---
answer2 = input("\n2. What does RAM stand for: ").lower()
if answer2 == "random access memory":
    print("Correct! ✅")
    score += 1  # Add a point
else:
    print("Incorrect. It stands for Random Access Memory. ❌")

# --- Question 3 ---
answer3 = input("\n3. What does HTML stand for: ").lower()
if answer3 == "hypertext markup language":
    print("Correct! ✅")
    score += 1  # Add a point
else:
    print("Incorrect. It stands for HyperText Markup Language. ❌")

# --- Final Score ---
print(f"\nQuiz Finished! You got {score} out of 3 questions correct. 🎉")