import datetime

class Person:

    def __init__(self, name, birthday, phoneNum): #birthday in mm/dd/yyyy
        self.name = name
        self.birthday = birthday
        self.phoneNum = phoneNum

    def age(self):
        today = datetime.date.today()
        month, day, year = self.birthday.split("/")
        birthMonth, birthDate, birthYear = self.birthday.split("/")
        age = today.year - int(year)

        if today < datetime.date(int(year), int(month),  int(day)): # this give us an issue beause we are comapring date, but the birthday will always come first because the year will always be less than todays
            age -= 1

        return age
