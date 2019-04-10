name = "wert"
name2 = int(input("Tippe eine Zahl ein: \n"))
name3 = 2.0

if name2 > 3 and name2 < 8:       #or kann auch verwendet werden
    print("yeah")


else:
    print("Nope")

# + - * /

#  % --> modulo - Zeigt den Rest einer Division an

count = 10
while(count):
    print(count)
    count -= 1

    if count < 5:
        #break
        continue

    print("continue text")

# break = Schleife komplett beenden
# continue = Schleife von oben
# count -= 1  --> Zahl wird um 1 verringert

#alles über 0 bzw. 1 ist True, 0 ist False --> 0 wird nicht mehr angezeigt und die Schleife wird beendet


#print(range(0, 4, 2))

for item in range(0, 8, 2):
    print(item)

