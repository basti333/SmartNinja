number = int(input("Select a number between 1 and 100: "))



for item in range (1, number+1):

    if item % 3 and item % 5 == 0:
        print("fizzbuzz")

    elif item % 3 == 0:
        print("fizz")

    elif item % 5 == 0:
        print("buzz")

    else:
        print(item)