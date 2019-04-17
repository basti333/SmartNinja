some_number = 3
float_number = 4.56
string_text = "hallo"
boolean = True

# Das sind primitive Datentypen in Python


number_list = [2, 4, 1, 7, 8]

print(number_list)

print(number_list[3])

print(number_list[0:3])

print(number_list[1:-1])


auto_list = ["audi", "tesla", "vw"]

print(auto_list)

auto_list.append("honda")       #etwas hinzufügen

print(auto_list)

auto_list.sort()                #Liste sortieren

print(auto_list)


for item in auto_list:
    item = "bla"                #Liste wird dadurch nicht verändert
    print(item)

print(auto_list)


