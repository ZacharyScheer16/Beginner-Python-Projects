import random


minNumber = int(input("What do you want to be the minimum Number: "))
maxNumber = int(input("What do you want to be the max Number: "))

answer = random.randrange(minNumber,maxNumber)
guess = False
while guess == False:
    UserGuess = int(input(f"What do you think the number is between {minNumber} and {maxNumber}: "))
    if UserGuess == answer:
        print(f"Correct, you guessed {answer}")
        guess = True

    if UserGuess > answer: ## answer 5       /// guess is 8    8 > 5
        minNumber = minNumber
        maxNumber = UserGuess
        print("Try again")

    if UserGuess < answer: #
        minNumber = UserGuess
        maxNumber = maxNumber
        print("Try again")

