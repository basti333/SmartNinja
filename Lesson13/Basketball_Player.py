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




#zuerst Funktion erstellen und vom User jeden einzelen Parameter abfragen
#dann mit Return das Objekt erzeugen

def new_football_player():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    height_cm = int(input("Height: "))
    weight_kg = int(input("Weight: "))
    goals = int(input("Goals: "))


    return Football_Player(first_name, last_name, height_cm, weight_kg, goals)



if __name__ == "__main__":         #wird verwendet um zu TESTEN, funktioniert nur in der eigenen Datei
    player1 = new_football_player()


    with open("Football_Player.json", "w") as json_file:
        json_file.write(json.dumps(player1.__dict__))

