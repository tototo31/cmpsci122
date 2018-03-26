### LAB #6 due 02/23 at 11:59 pm 
# Submission Instructions
#  file name: LAB6.py
#  Do NOT change any function name
#  Upload all the functions in a file with the correct file name to Vocareum

#### COLLABORATION STATEMENT: 
#### WORKED ON THIS ALONE

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator==0:
            raise ZeroDivisionError("Denominator cannot be zero")
            return
        self.n = numerator
        self.d = denominator

    def __add__(self, other):
        n = self.n * other.d + self.d * other.n
        d = self.d * other.d
        return Fraction(n, d)

    def __sub__(self, other):
        n = self.n * other.d - self.d * other.n
        d = self.d * other.d
        return Fraction(n, d)

    def __mul__(self, other):
        n = self.n * other.n
        d = self.d * other.d
        return Fraction(n, d)

    def __truediv__(self, other):
        n = self.n * other.d
        d = self.d * other.n
        return Fraction(n, d)

    def __eq__(self, other):
        return self.n/self.d == other.n/other.d

    def __gt__(self, other):
        return self.n/self.d > other.n/other.d

    def __lt__(self, other):
        return self.n/self.d < other.n/other.d

    def __str__(self):
        return "{}/{}".format(self.n, self.d)

    __repr__ = __str__

class Book():
    totalCat = 0
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        Book.totalCat += 1

    def __str__(self):
        return "TITLE: {} by {}".format(self.title, self.author)

    __repr__ = __str__

    def __len__(self):
        return self.pages

    def __del__(self):
       Book.totalCat -= 1
       return Book.totalCat

    @classmethod
    def inventory(self):
        return Book.totalCat
