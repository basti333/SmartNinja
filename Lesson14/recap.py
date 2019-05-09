class animal():
    count = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.count.append(name)

    def get_number_animals(self):
        return len(self.count)

class dog(animal):
    def __init__(self, name, age, paws):
        super().__init__(name, age)
        self.paws = paws

    def bark(self):
        return "Wuff"

class fish(animal):
    def __init__(self, name, age, fins):
        super().__init__(name, age)
        self.fins = fins

    def blub(self):
        return "Blub"

a = dog("Bello", 10, 4)
b = fish("Charlie", 13, 8)


print(a.get_number_animals())

print(a.bark())

print(b.blub())