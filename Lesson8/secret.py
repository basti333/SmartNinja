secret = 333

guess = int(input("What's the secret number? \n"))


if secret == guess:
    print("Awesome!")

if secret != guess:
    print("Try again, loser!")

while secret != guess:
    print ("Wrong!")
    secret+=1