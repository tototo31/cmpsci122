### LAB #5 due 02/16 at 11:59 pm 
# Submission Instructions
#  file name: LAB5.py
#  Do NOT change any function name

#### COLLABORATION STATEMENT: 
#### I worked on this by myself

from math import sqrt

# ENTER YOUR ANSWER FOR EXERCISE ONE HERE
def answers():
    #Write your answer between the quotes (if multiple values, separate them with commas)
    ex_1 = "5"
    return ex_1


def power(value, exp):
#Write your code here:
    total = 1
    if exp == 0:
        return 1
    elif exp < 0:
        for x in range(abs(exp)):
            total *= 1/value
    else:
        for x in range(exp):
            total *= value
    return round(total, 3)
class Line:
#Write your code here:
    def __init__(self, coord1, coord2):
        self.x = (coord1[0], coord2[0])
        self.y = (coord1[1], coord2[1])

    def slope(self):
        #deltaX = self.x[1]-self.x[0]
        #deltaY = self.y[1]-self.y[0]
        if not self.x[1]-self.x[0]:
            return "Infinity"
        return round((self.y[1]-self.y[0])/(self.x[1]-self.x[0]), 3)

    def distance(self):
        deltaX = self.x[1] - self.x[0]
        deltaY = self.y[1] - self.y[0]
        return round(sqrt(deltaX**2 + deltaY**2), 3)
###TESTING EXAMPLES, Create your own testing examples too, these are just a baseline. REMOVE THIS BEFORE SUBMITTING
#print(power(5,-3))
### OUTPUT:0.008
#line1=Line([2,6],[2,3])
#print(line1.distance())
### OUTPUT: 3.0
#print(line1.slope())
### OUTPUT: 'Infinity'

