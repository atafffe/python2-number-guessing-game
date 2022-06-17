import random
limit = 9
number = random.randint(1, limit)
chances = 0
maxchances = 5

while chances < maxchances:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("You guessed the number which was: ", number)
        break
    elif guess > limit:
        print("Your number is too high! The limit is ", limit)
    else:
        chances += 1
        print("Wrong number, you have: ", maxchances - chances, " guesses left")

if chances >= maxchances:
    print("You lost! The answer was: ", number)        