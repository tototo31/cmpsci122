### HW#6 due 04/02 at 7:59 AM 
# Submission Instructions
#  file name: HW6.py
#  Do NOT change any function name

#### COLLABORATION STATEMENT: 
#### I WORKED ON THIS ALONE

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
        # print("adding {}".format(value))
        new_node = Node(value)
        if self.head==None: # if there isnt anything in the list
            self.head=new_node
            self.tail=self.head
        elif self.tail==self.head: # if there is only one value in the list
            if self.head.value < value: #if the value is less than the only other then put it at the tail
                self.tail=Node(value)
                self.head.setNext(self.tail)
            else:
                self.head = new_node
                self.head.setNext(self.tail)
        else:
            current = self.head
            previous = None
            while current.getValue() < new_node.getValue(): # traverse the list
                previous = current
                if current == self.tail: # if we hit the end stop
                    current = None
                    break
                else: # keep going otherwise
                    current = current.getNext()

            if current == self.head:
                self.head = new_node
                new_node.setNext(current)
            elif current is None:
                self.tail = new_node
                new_node.setNext(None)
                previous.setNext(new_node)
            else:
                previous.setNext(new_node)
                new_node.setNext(current)

        self.count+=1

    def delete(self, value):
        current = self.head
        previous = None
        if self.search(value) == True:
            while not current is None:
                if current.getValue() == value:
                    break
                previous = current
                current = current.getNext()
        else:
            print("Value not in list")
            return

        if self.count == 1:
            self.tail = None
            self.head = None
        elif current == self.tail:
            self.tail = previous
            previous.setNext(current.getNext())
        elif current == self.head:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        del(current)
        self.count -= 1

    def search(self,value):
        current = self.head
        found = False
        while not current is None and not found:
            if current.value == value:
                found = not found
            else:
                current = current.getNext()
        return found

    def pop(self):
        value = self.tail.getValue()
        self.delete(self.tail.getValue())
        return value

    def isEmpty(self):
        return self.count == 0

    def size(self):
        return self.count

    def printList(self):
        temp=self.head
        while temp:
            print(temp.getValue(), end=' ')
            temp=temp.getNext()
        # print()


#TESTS - remove before submitting
# if __name__ ==  "__main__":
#     ordered_ll=OrderedLinkedList()
#     ordered_ll.add(8)
#     ordered_ll.add(7)
#     ordered_ll.add(3)
#     ordered_ll.add(-6)
#     ordered_ll.add(58)
#     ordered_ll.add(33)
#     ordered_ll.add(1)
#     ordered_ll.add(-88)
#     ordered_ll.printList()
#     print()
#     ordered_ll.head
#     ordered_ll.tail
#     ordered_ll.isEmpty()
#     ordered_ll.size()
#     ordered_ll.delete(7)
#     ordered_ll.printList()
#     ordered_ll.delete(-88)
#     ordered_ll.printList()
#     ordered_ll.delete(58)
#     ordered_ll.printList()
#     print()
#     ordered_ll.size()
#     ordered_ll.head
#     ordered_ll.tail
#     ordered_ll.pop()
#     ordered_ll.printList()
#     print()
#     ordered_ll.pop()
#     ordered_ll.printList()
#     print()
#     ordered_ll.head
#     ordered_ll.tail
