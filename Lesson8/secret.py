secret = 333

loser = True


while(loser):
    guess = int(input("What's the secret number? \n"))


    if secret == guess:
        print("Awesome!")
        loser = False
    elif secret < guess:
        print("Too high, loser! Try Again!")
    elif secret > guess:
        print("Too low, loser! Try Again!")

