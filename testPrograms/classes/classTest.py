class Dog:
    num_of_legs=0   # all have access to this variabl this the difference is
                    # that you can assign a value to all instances via
                    # Dog.num_of_legs = 5 thist would assign a value of five to
                    # all instances in the class. You can however assign each
                    # individual afterwards. if you assign your own value
                    # before changing the class value your custom value will
                    # stay
    count = 0 # what if we want to keep track of how many dogs have been created
    def __init__(self, name, breed, size, age): # only the instance will have access to these variables
        self.name = name
        self.breed = breed
        self.size = size
        self.age = age
        Dog.count += 1 # this is our dog counter

    #def howMany(self): # the function to return a count of all dogs
    #    return Dog.count # this wont work because when you call a method you need to know class instance Dog.howMany() wont work

    @classmethod
    def howMany(): # this works because we are saying howMany() is a methoed that doesnt require an instance to be created
        return Dog.count

    def eat(self):
        print(self.name+" is eating")

    def sit(self):
        print(self.name+" is sitting")

    def rollover(self):
        print(self.name+" is rolling over")

    def run(self):
        print(self.name+" is running")

chuck = Dog("Bird", "breed", "large", 12)
chuck.eat()
