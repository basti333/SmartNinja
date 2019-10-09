class Vehicle:
    def __init__(self, brand, color, age):
        self.brand = brand
        self.color = color
        self.age = age

    def construction_year(self):
        year = 2019 - self.age
        return year

class Car(Vehicle):
    def __init__(self, brand, color, age, wheel_size, horsepower):
        Vehicle.__init__(self, brand, color, age)
        self.wheel_size = wheel_size
        self.horsepower = horsepower

    def print_car(self):
        Car = (self.brand, self.color, self.age, self.wheel_size, self.horsepower)
        print(Car)

Fiat_500 = Car("Fiat", "black", 10, 16, 100)

Fiat_500.print_car()

def food_list(food):
    for element in food:
        print(element)


veggies = ["Cucumber", "Lettuce", "Pepper", "Peas", "Beans"]

food_list(veggies)


secret = {"Name": "Sebastian", "Age": 23}

for x in secret:
    print(secret[x])
