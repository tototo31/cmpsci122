### LAB #10 due 03/30 at 11:59 pm
# Submission Instructions
#  file name: LAB10.py
#  Do NOT change any function name

#### COLLABORATION STATEMENT:
####I WORKED ON THIS ALONE

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self,new_value):
        self.value = new_value

    def setNext(self,new_next):
        self.next = new_next

    def __str__(self):
        return ("{}".format(self.value))

    __repr__ = __str__


class Stack:

    def __init__(self):
        self.top = None #Do NOT modify this line


    def isEmpty(self):
        return self.top is None

    def size(self):
        temp = self.top
        count = 0
        while temp:
            temp = temp.getNext()
            count += 1

    def push(self,item):
        new_node = Node(item)
        new_node.setNext(self.top)
        self.top = new_node


    def pop(self):
        if not self.top is None:
            temp = self.top
            val = temp.getValue()
            self.top = self.top.getNext()
            del(temp)
            return val
        else:
            return

    def peek(self):
        return self.top.getValue() if not self.top is None else None

    def printStack(self):
        temp=self.top
        while temp:
            print(temp.getValue())
            temp=temp.getNext()
