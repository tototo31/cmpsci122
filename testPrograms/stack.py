class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def getValue(self): # return what is stored
        return self.value

    def getNext(self): # return the next element in the list
        return self.next

    def setValue(self, new_value): # assign a new value to the element
        self.value = new_value

    def setNext(self, new_next): # create the link
        self.next = new_next

    def __str__(self): # just return the value if we try and print an object
        return "{}".format(self.value)

class Stack:

    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, value):
        self.count += 1
        pass

    def pop(self):
        self.count -= 1
        pass
