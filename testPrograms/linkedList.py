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

class LinkedList: # prepending linked list
    def __init__(self):
        self.head = None # Whats at the front of the list - initialize as None since there will be no elements when the list is initialized
        self.tail = None # Whats the last element
        self.count = 0

    def isEmpty(self):
        return self.head == None # return True if there is no head

    def size(self): # returns number of "elements" in list
        return self.count

    def add(self, value): # add an element and then set it as head
        new_node = Node(value)
        new_node.setNext(self.head) # create link
        self.head = new_node # set where the beginning of the list is
        if self.size() == 1: # if this is the first element set it as the tail as it will always be at the end
            self.tail = new_node
        self.printList()
        self.count += 1

    def printList(self): # print current list values stored
        temp = self.head
        while temp: #while there is something continue once we hit None we know were at the end of the list
            print(temp, end=" ")
            temp = temp.next
        print()

    def search(self, value): # is the value in the list?
        current = self.head
        found = False
        while current != None and not found:
            if current.getValue() == value:
                found = True
            else:
                current = current.getNext()
        return found

    def append(self, value):
        if self.size() == 0:
            self.add(value)
        elif self.head == None:
            new_node = Node(value)
            self.tail = self.head
        elif self.tail == self.head:
            self.tail = Node(value)
            self.head.setNext(self.tail)
        else:
            new_node = Node(value)
            self.tail.setNext(new_node)
            self.tail = new_node
        self.count += 1

    def remove(self, value):
        current = self.head()
        previous = None
        found = False

        while not found:
            if current.getValue() == value:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None: # If deleting head
            self.head = current.getNext()
        elif current.getNext is None: # if deleting tail
            self.tail = previous
            previous.setNext = None
        else:
            previous.setNext(current.getNext())
        self.count -= 1

if __name__ == "__main__":
    linked_list = LinkedList()
