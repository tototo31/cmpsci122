class Animal:
    number_of_legs = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print( "{} is eating".format(self.name))

    def sleep(self):
        print("{} is sleeping".format(self.name))

    def run(self):
        print("{} is running".format(self.name))

    def __add__(self, other):
        return(self.name + " and " + other.name + " are friends")

    def __str__(self):
        return "{} is a {} year old animal".format(self.name, self.age)

    __repr__ = __str__

class Dog(Animal):
    def __init__(self, name, age, size, breed):
        Animal.__init__(self, name, age) # inherit same definitions from animal super class ( we dont have to reassign name and age since thats taken care of in Animals __init__
        self.breed = breed
        self.size = size

    def sit(self):
        print("{} is sitting".format(self.name))

    def bark(self):
        print("bark bark")

    def roll_over(self):
        print("{} is rolling over".format(self.name))

class Cat(Animal):
    def __init__(self, name, color, age):
        Animal.__init__(self, name, age)
        self.color = color
    def meow(self):
        print("meow meow")
