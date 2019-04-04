x = int(input("Gibe eine Zahl ein: "))
y = int(input("Gib eine weitere Zahl ein: "))

some_string = "GRÖßER"

print(x+y)

if x > y:
    print(some_string)
elif x < y:
    print("KLEINER")
else:
    print("Computer says no")
if x != y:
    print("Ungleich")