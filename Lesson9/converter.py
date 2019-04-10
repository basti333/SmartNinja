print("Hello, with this little program you are able to convert kilometers into miles.")


while True:
    km = int(input("Please enter the amount of kilometers: \n"))

    print(str(km * 0.6213719) + " miles")

    answ = input("Do you want to do another conversion? \n")

    if answ == "no":
        print("Thanks for choosing this converter. Goodbye!")
        break

