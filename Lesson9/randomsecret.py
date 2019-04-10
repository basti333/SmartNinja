#import random

from random import randint     #nur EIN Teil einer Funktion wird eingebunden, nicht alles

secret = randint(0,30)


while True:
    guess = int(input("What's the secret number? \n"))


    if secret == guess:
        print("Awesome!")
        break
    elif secret < guess:
        print("Too high, loser! Try Again!")
    elif secret > guess:
        print("Too low, loser! Try Again!")

