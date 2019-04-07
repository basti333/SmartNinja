zahl1 = int(input("Hallo, ich bin dein Taschenrechner. Nenn mir die erste Zahl: \n"))

zahl2 = int(input("Nenn mir eine zweite Zahl: \n"))

operation = input("Welche Operation soll ausgeführt werden? (+,-,*,/) \n")

if operation == "+":
    print(zahl1 + zahl2)
elif operation == "-":
    print(zahl1 - zahl2)
elif operation == "*":
    print(zahl1 * zahl2)
elif operation == "/":
    print(zahl1 / zahl2)
else:
    print("Fehler: Nur folgende Zeichen sind erlaubt '+ - * /'. Probiere es noch einmal!")
