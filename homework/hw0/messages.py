def print_message(day):
    messages = {
        "monday": "Hello, world!",
        "tuesday": "Today is tuesday!",
        "wednesday": "Hump day!!",
        "thursday": "Today is Jueves in Spanish!",
        "friday": "Last day of the week!",
        "saturday": "Game Day!!",
        "sunday": "Aww, the weekend is almost over."
    }
    print(messages[day])

def print_friday_message():
    print_message("Friday")


print_friday_message()