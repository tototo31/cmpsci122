import datetime

class Customer:
    def __init__(self,name,birthdate,phone,balance=0.0):
        self.name=name
        self.birthdate=birthdate
        self.phone=phone
        self.balance=balance

    def __str__(self): # this is what is returned when an instance is inside the prnt command
        return "{} has {} USD in this bank".format(self.name, self.balance)

    def __add__(self, other):
        return "{} in combined funds".format(self.balance+other.balance)

    def age(self):
        today=datetime.date.today()
        month, day, year = self.birthdate.split("/")
        age = today.year - int(year)

        if (today.month, today.day) < (int(month),int(day)):
            age-=1

        return age

    def withdraw(self, amount):
        if amount>self.balance:
                return "You don't have enough money"
        else:
            self.balance-=amount
            return self.balance

    def deposit(self, amount):
        self.balance+=amount
        return self.balance

    def check_balance(self):
        return self.balance








