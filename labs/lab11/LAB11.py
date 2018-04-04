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
            self.tail.setNext(new_node)
            self.tail = new_node
        self.count += 1

    def dequeue (self):
        toRemove = self.head
        value = None
        if self.count == 1:
            value = self.head.getValue()
            self.head = None
            self.tail = None
        elif self.count == 0:
            return "Queue is empty"
        else:
            value = self.head.getValue()
            self.head = toRemove.getNext()

        del(toRemove)
        self.count -= 1
        return value


    def printQueue(self):
        temp = self.head
        while (temp):
            print(temp.value, end=' ')
            temp = temp.next

if __name__ == "__main__":
    queue=Queue()
    print(queue.isEmpty())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.printQueue()
    print()
    print(queue.isEmpty())
    print(queue.size())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    queue.enqueue(3)
    queue.enqueue(2)
    queue.printQueue()
    print()
    queue.dequeue()
    queue.printQueue()
    print()
