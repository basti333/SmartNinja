

class Player:
    def __init__(self, name, age, height_cm, weight):
        self.name = name
        self.age = age
        self.height_cm = height_cm
        self.weight = weight
        self.status = "active"

    def height_in_meters(self):
        height_m = self.height_cm / 100
        return height_m


class FootballPlayer(Player):
    def __init__(self, name, age, height_cm, weight, goals, assists):
        Player.__init__(self, name, age, height_cm, weight)
        self.goals = goals
        self.assists = assists

    def print_player(self):
        print(self.name, self.age, self.height_in_meters(), self.weight, self.status, self.goals, self.assists)


Sebastian = FootballPlayer("Sebastian", 23, 178, 65, 100, 93)

Sebastian.print_player()


def print_food(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry", "lemon"]


print_food(fruits)

