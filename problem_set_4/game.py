import sys
from random import randint

while True:
    try:
        level = input("Level: ")
        n = randint(1, int(level))
        while True:
            guess = int(input("Guess: "))
            if guess == n:
                sys.exit("Just right!")
            elif guess < n:
                print("Too small!")
            elif guess > n:
                print("Too large!")
    except (TypeError, ValueError):
        pass