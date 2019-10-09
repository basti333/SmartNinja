schrauben = int(input("Wie viele Schrauben haben Sie? \n"))
muttern = int(input("Wie viele Muttern haben Sie? \n"))
unterlegscheiben = int(input("Wie viele Unterlegscheiben haben Sie? \n"))

rechnungssumme = schrauben * 0.07 + muttern * 0.04 + unterlegscheiben * 0.02


print("Das macht dann bitte " + str(rechnungssumme) + " Euro.")