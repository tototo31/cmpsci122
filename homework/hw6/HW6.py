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
        if self.head==None: # if there isnt anything in the list
            new_node=Node(value)
            self.head=new_node
            self.tail=self.head
        elif self.tail==self.head: # if there is only one value in the list
            if self.head.value > value: #if the value is greater than the only other then put it at the tail
                self.tail=Node(value)
                self.head.setNext(self.tail)
            else:
                self.head = new_node
                self.head.setNext(self.tail)
        else:
            new_node=Node(value)
            current = self.head
            previous = None
            while current.getValue() < new_node.getValue() and not current.getNext() is None:
                previous = current
                current = current.getNext()
            if current == self.head:
                self.head = new_node
            new_node.setNext(current)
            current.setNext(new_node)
        self.count+=1

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
print("list =")
ordered_ll.printList()
print(ordered_ll.head)
print(ordered_ll.tail)
print(ordered_ll.isEmpty())
print(ordered_ll.size())
