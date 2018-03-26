### HW#6 due 04/02 at 7:59 AM 
# Submission Instructions
#  file name: HW6.py
#  Do NOT change any function name

#### COLLABORATION STATEMENT: 
####

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

class OrderedLinkedList:
    #Do NOT modify the constructor
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def add(self, value):
        new_node = Node(value)
        current = self.head
        previous = None
        if self.count == 0: # if the list is empty set head and tail equal to this
            self.head = new_node
            self.tail = new_node
        else:
            while current.getValue() < value and not current.next == None: #while the value of the current node is less than the value were trying to add iterate though the list
                previous = current # set previous - after this loop ends previous should be < value but previous.next > value
                current = current.getNext()
            new_node.setNext = current # set the next node to the one after previous
            previous.setNext = new_node # set the last node < value to point to value
        self.count += 1

    def delete(self, value):
        pass

    def search(self,value):
        pass

    def pop(self):
        pass

    def isEmpty(self):
        return self.count == 0

    def size(self):
        return self.count

    def printList(self):
        temp=self.head
        while temp:
            print(temp.getValue(), end=' ')
            temp=temp.getNext()


#TESTS

ordered_ll=OrderedLinkedList()
ordered_ll.add(8)
ordered_ll.add(7)
ordered_ll.add(3)
ordered_ll.add(-6)
ordered_ll.add(58)
ordered_ll.add(33)
ordered_ll.add(1)
ordered_ll.add(-88)
ordered_ll.printList()
print(ordered_ll.head)
print(ordered_ll.tail)
print(ordered_ll.isEmpty())
print(ordered_ll.size())
