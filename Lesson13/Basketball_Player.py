import json



class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg


class Basketball_Player(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        #mit der Funktion super(). kann auf eine Überklasse zugegriffen werden
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

    def set_points(self, points):
        self.points = points


class Football_Player(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals

if __name__ == "__main__":         #wird verwendet um zu TESTEN, funktioniert nur in der eigenen Datei

    jordan = Basketball_Player("Michael", "Jordan", 205, 90, 150, 69, 33)
    dirk = Basketball_Player("Dirk", "Nowitzki", 210, 100, 130, 23, 90)
    marko = Football_Player("Marko", "Arnautovic", 175, 80, 77)

    dirk.set_points(189)

    player = [jordan, dirk, marko]



    for item in player:
        print(item.first_name)
        print(item.weight_kg)

    print(marko.goals)


#zuerst Funktion erstellen und vom User jeden einzelen Parameter abfragen
#dann mit Return das Objekt erzeugen

def new_player():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    height_cm = input("Height: ")


    Player = Basketball_Player(first_name, last_name)

    return Player

new_player()

print(Player)