#1/usr/local/bin/python3
# an decorator is any function that changes a program or function
class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)

    __repr__ = __str__ #set string representation to opject representation

    def __add__(self, other):
        newNumerator = (self.numerator * other.denominator) + (other.numerator* self.denominator)
        newDenominator = self.denominator * other.denominator

        return Fraction(newNumerator, newDenominator)

    def __sub__(self, other):
        newNumerator = (self.numerator * other.denominator) - (other.numerator* self.denominator)
        newDenominator = self.denominator * other.denominator

        return Fraction(newNumerator, newDenominator)


    def __mul__(self, other):
        newNumerator = self.numerator * other.numerator
        newDenominator = self.denominator * other.denominator

        return Fraction(newNumerator, newDenominator)

    def __truedivision__(self, other):
        newNumerator = self.numerator * other.denominator
        newDenominator = self.denominator * other.numerator

        return Fraction(newNumerator, newDenominator)

frac1 = Fraction(2,6)
frac2 = Fraction(3, 9)
