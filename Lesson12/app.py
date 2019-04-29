
#STRINGS

phrase = "Giraffe Academy"

print(len(phrase))   #wieviele Zeichen?

print(phrase.isupper())     #ist alles groß geschrieben?

print(phrase[0])           #ein Zeichen eines Strings ausgeben

print(phrase.index("a"))      #an welcher Stelle ist dieses Zeichen

print(phrase.replace("Giraffe", "Elephant"))        #etwas ersetzen


#NUMBERS

#int() = integer --> GANZE ZAHL

#float() = DEZIMALZAHL

from math import *                  #Mathefunktionen importieren, * = alles

print(8)        #gibt eine Nummer aus

print(2.1568448945616)     #gibt eine Kommazahl aus

print(3 + 4.5)      #Arithmetik

print(10 % 3)       #gibt den Rest aus der Division aus

my_num = 5

print(my_num)      #gibt eine Variable aus

print(str(my_num) + " is my favorite number.")     #print out number AND string

num_2 = -15

print(abs(num_2))      #gibt den absoluten Wert der Zahl aus

print(pow(3, 2))       #3 raised to the power of 2 = 3 hoch 2

print(max(4, 6))        #zeigt die höchste Zahl an

print(min(3,7))         #zeigt die niedrigste Zahl

print(round(3.7))         #rundet auf nächste ganze Zahl

print(floor(3.7))           #egal wie die Zahl ist, immer abrunden

print(ceil(3.7))            #egal wie die Zahl ist, immer aufrunden

print(sqrt(36))             #die Wurzel aus einer Zahl


#INPUT

#name = input("Enter your name: ")
#age = input("Enter your age: ")

#print("Hello " + name + "! Your are " + age)


#MAD LIBS GAME

#color = input("Enter a color: ")
#plural_noun = input("Enter a plural noun: ")
#celebrity = input("Enter a celebrity name: ")


#print("Roses are " + color)
#print(plural_noun + " are blue")
#print("I love " + celebrity)


#LISTS

friends = ["Max", "Antonio", "Jerome"]
             #0        #1        #2
             #-3       #-2      #-3

print(friends[1])      #Elemente anzeigen

print(friends[-2])     #Elemente anzeigen, von hinten gezählt

print(friends[1:])      #alle Elemente ab 1, 1 wird ANGEZEIGT

print(friends[0:2])        #alle Elemente von 0 bis 2, aber Element 2 wird NICHT ANGEZEIGT

friends[1] = "Mike"        #ein Element kann ausgetauscht werden

print(friends)              #Liste wird mit neuem Element ausgegeben


#LIST FUNCTIONS

lucky_numbers = [4, 82, 15, 26, 23, 42]

friends = ["Kevin", "Jerome", "Marcel", "Chantal", "Claudette", "Pascal"]

friends_2 = friends.copy()       #eine Liste kopieren

friends.extend(lucky_numbers)     #eine Liste um eine weitere Liste erweitern, wird hinten drangehängt

friends.append("Samantha")     #Element wird hinten angehängt

friends.insert(1, "Kelly")     #Element an einer Stelle einfügen, die anderen werden nach hinten geschoben

friends.remove("Chantal")      #ein Element entfernen

print(friends.index("Jerome"))    #zeigt welchen Index das Element hat

print(friends.count("Marcel"))      #zeigt wie oft ein Element in einer Liste ist

lucky_numbers.sort()                #aufsteigende Sortierung

print(lucky_numbers)

lucky_numbers.sort(reverse=True)    #absteigende Sortierung

print(lucky_numbers)

lucky_numbers.reverse()             #die Liste von hinten nach vorne

#friends.clear()                 #alle Elemente löschen

print(friends)

print(friends_2)

print(lucky_numbers)


#TUPLES

coordinates = (4, 5)    #ein Tuple kann NICHT verändert werden wie eine Liste

coordinates_2 = [(5,8), (6, 3), (4, 9)]    #Tuples in einer Liste

coordinates_2[2] = "Hund"        #die Liste kann geändert werden aber die Tuples in der Liste nicht

print(coordinates)

print(coordinates_2)


#FUNCTIONS

def say_hi(name):                       #specify the function    name=parameter
    print("Hello " + name)

say_hi("Mike")                            #call the function, give information for parameter
say_hi("James")

def say_hi_2(name, age):                       #specify the function    name=parameter
    print("Hello " + name + ", you are " + str(age))

say_hi_2("Mike", 35)                            #call the function, give information for parameter
say_hi_2("James", 70)


#RETURN STATEMENT

def cube(num):
    return num*num*num          #return something, you cannot put any code below the return keyword in a function

result = cube(4)                #store the return of the function in a variable
print(result)                   #print the result of the funciton


#IF STATEMENTS

is_male = True
is_tall = True

if is_male and is_tall:                              #Möglichkeiten: or und and
    print("You are a tall male")
elif is_male and not(is_tall):                       #not führt dazu, dass das Statement den gegenteiligen Wert annimmt
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are either not male nor tall or both")


#IF STATEMENTS & COMPARISONS

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:               #you can compare all data types
        return num1                                 #!= bedeutet ist nicht gleich, == bedeutet ist gleich
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))


#DICTIONARIES

month_conversions = {
    "Jan": "January",                       #Jan ist der Key, January der Value
    "Feb": "February",                      #Jeder Key darf in einem Dictionary nur einmal vorkommen
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(month_conversions["Nov"])

print(month_conversions.get("Aug"))

print(month_conversions.get("Luv", "Not a valid key"))       #default value can be set


#WHILE LOOP

i = 1
while i <= 10:
    print(i)
    i = i + 1       #oder i += 1   fügt jeweils 1 zu i hinzu

print("Done with loop")


#GUESSING GAME

secret_word = "goat"
guess = ""                   #leere Variable, wird dann mit Input befüllt
guess_count = 0              #der Spieler startet mit 0 guesses
guess_limit = 3              #insgesamt hat der Spieler 3 guesses zur Verfügung
out_of_guesses = False       #wird auf False gesetzt und wird dann True wenn guess limit erreicht

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:               #hier wird überprüft ob der Spieler noch guesses hat
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True           #wird True weil guess count nicht mehr kleiner als guess limit ist

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")


#FOR LOOP

for letter in "Giraffe Academy":       #jeder Buchstabe im String wird ausgegeben
    print(letter)                       #es ist ganz egal welcher variablenname verwendet wird


friends = ["Jim", "Karen", "Kevin"]
for name in friends:                    #alle Elemente der Liste werden ausgegeben
    print(name)

for index in range(10):                 #alle Zahlen von 0 bis 10 werden ausgegeben (10 NICHT)
    print(index)

for index in range(3, 10):
    print(index)                        #alle Zahlen von 3 bis 10 (10 NICHT)

for index in range(len(friends)):       #len gibt die Anzahl an Elementen in der Liste aus
    print(friends[index])               #dadurch werden alle 3 Namen ausgegeben

for index in range(5):                  #if statement im for loop
    if index == 0:
        print("first iteration")
    else:
        print("not first")

