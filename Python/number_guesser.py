import random

low = 1
high = 100

answer = random.randint(low,high)
print(answer)

gusses = 0
is_running = True

print("Python Number Guesser")
print(f"Guess a number between {low} and {high}")

while is_running:
    guess = int(input("Enter a guess: "))
    gusses += 1

    if guess == answer:
        print(f"Correct! The answer was {answer}")
        print(f"It took you {gusses} guesses")
        is_running = False
    elif guess < answer:
        print("Guess higher")
    else:
        print("Guess lower")