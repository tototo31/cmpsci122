### LAB #11 due 04/06 at 11:59 pm
# Submission Instructions
#  file name: LAB11.py
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


class Queue:
    #Do NOT modify the initializer
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def isEmpty(self):
        return not self.count > 0

    def size(self):
        return self.count

    def enqueue(self, item):
        new_node = Node(item)
        if  self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.setNext(self.head)
            self.head = new_node
        self.count += 1

    def dequeue (self):
        toRemove = self.head
        value = self.head.getValue()
        if self.count == 1:
            self.head = None
            self.tail = None
            self.count -= 1
        elif self.count == 0:
            return "Queue is empty"
        else:
            #set new tail remove current tail
            pass # Logic for if there is more than one or none elements

        del(toremove)
        self.count -= 1
        return value


    def printQueue(self):
        temp = self.head
        while (temp):
            print(temp.value, end=' ')
            temp = temp.next

