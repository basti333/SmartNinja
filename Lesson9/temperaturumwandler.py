print("Hallo beim Temperaturumwandler.")

while True:
    answ = input("""Welche Umwandlung möchtest du durchführen?
    1 Umrechnung von Celsius nach Kelvin
    2 Umrechnung von Celsius nach Fahrenheit
    3 Umrechnung von Kelvin nach Celsius 
    4 Umrechnung von Kelvin nach Fahrenheit 
    5 Umrechnung von Fahrenheit nach Celsius 
    6 Umrechnung von Fahrenheit nach Kelvin
Wenn du das Programm beenden möchtest, tippe 'ende'!\n""")

    if answ == "1":
        grad = float(input("Bitte gib die Temperatur ein: \n"))
        print(str(grad) + " Grad Celsius sind " + str(grad + 273.15) + " Grad Kelvin")

    elif answ == "2":
        grad = float(input("Bitte gib die Temperatur ein: \n"))
        print(str(grad) + " Grad Celsius sind " + str(grad/(5/9)+32) + " Grad Fahrenheit")

    elif answ == "3":
        grad = float(input("Bitte gib die Temperatur ein: \n"))
        print(str(grad) + " Grad Kelvin sind " + str(grad - 273.15) + " Grad Celsius")

    elif answ == "4":
        grad = float(input("Bitte gib die Temperatur ein: \n"))
        print(str(grad) + " Grad Kelvin sind " + str((grad - 273.15) * (9/5) + 32) + " Grad Fahrenheit")

    elif answ == "5":
        grad = float(input("Bitte gib die Temperatur ein: \n"))
        print(str(grad) + " Grad Fahrenheit sind " + str((grad - 32) * (5/9)) + " Grad Celsius")

    elif answ == "6":
        grad = float(input("Bitte gib die Temperatur ein: \n"))
        print(str(grad) + " Grad Fahrenheit sind " + str((grad - 32) * (5/9) + 273.15) + " Grad Kelvin")

    elif answ.lower() == "ende":
        print("Auf Wiedersehen!")
        break

    else:
        print("Bitte verwende nur folgende Zeichen: '1, 2, 3, 4, 5, 6, ende'")