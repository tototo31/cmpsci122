### LAB #7 due 03/02 at 11:59 pm 
# Submission Instructions
#  file name: LAB7.py
#  Do NOT change any function name
#  Upload all the functions in a file with the correct file name to Vocareum

#### COLLABORATION STATEMENT: 
####

# ENTER YOUR ANSWERS FOR EXERCISE ONE HERE
def answers():

    #Write your answer for exercise 1 between the quotes
    question_1_a = "6,12,36"

    question_1_b = "True"

    return question_1_a, question_1_b


class Vehicle:
    def __init__(self, wheels, miles, make, model, year):
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = False

    def sell(self):
        if self.sold_on == True:
            print("This item has been sold")
        else:
            self.sold_on = True

    def sale_price(self):
        if self.sold_on:
            return 0.0  # Already sold
        return 4000 * self.wheels

    def purchase_price(self):
        return self.flat_rate - (.10 * self.miles)

# Code from LAB7.pdf
class Car(Vehicle):
    def __init__(self, wheels, miles, make, model, year, gear, color):
        Vehicle.__init__(self, wheels, miles, make, model, year)
        self.gear = gear
        self.color = color
        self.flat_rate = 7500

    def getDescription(self):
        sale_price=self.sale_price()
        return "{} {} {} - {}, {} miles >>> ${}".format(self.make, self.model, self.year, self.color, self.miles, sale_price)

class Truck(Vehicle):
    def __init__(self, seats, wheels, miles, make, model, year):
        Vehicle.__init__(self, wheels, miles, make, model, year)
        self.seats=seats
        self.flat_rate = 9000

    def getDescription(self):
        sale_price=self.sale_price()
        return "{} {} {}, {} miles - {} seats >>> ${}".format(self.make, self.model, self.year,self.miles, self.seats, sale_price)
