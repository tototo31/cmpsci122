### LAB #9 due 03/23 at 11:59 pm 
# Submission Instructions
#  file name: LAB9.py
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

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def insert(self, after, item):
        isFound = self.search(after)
        current = self.head
        if not isFound: #did we find the value
            print("Value Not found")
            return -1
        else:
            while not current.getValue() == after: #while the node were looking at doesnt have the correct value continue on
                current = current.next
            new_node = Node(item) #weve found our item so create the new node
            new_node.next = current.next # set the next node to afters previously next node
            current.next = new_node # set afters new node to the one we just created

    def pop(self):
        current = self.head
        value = None
        while not current.next is None: #while there is a next value keep going
            current = current.next
        value = current.getValue() # weve gotten to the final value in the list - store it so we have access once it has been deleted
        self.remove(value) # delete the node
        return value # return the value we just deleted

    #Make sure the rest of the methods work correclty after you implement insert and pop
    def append(self, value):
        if self.head==None:
            new_node=Node(value)
            self.head=new_node
            self.tail=self.head
        elif self.tail==self.head:
            self.tail=Node(value)
            self.head.setNext(self.tail)
        else:
            new_node=Node(value)
            self.tail.setNext(new_node)
            self.tail=new_node
        self.count+=1


    def remove(self, value):
        current=self.head
        previous=None
        found=False
        while not found:
            if current.getValue()==value:
                found=True
            else:
                previous=current
                current=current.getNext()

        if previous==None:
            self.head=current.getNext()
        elif current.getNext()==None:
            self.tail=previous
            previous.setNext(None)
        else:
            previous.setNext(current.getNext()) 

        self.count-=1


    def isEmpty(self):
        return self.head == None

    def size(self):
        return self.count

    def add(self, value):
        new_node=Node(value)
        new_node.setNext(self.head)
        self.head=new_node
        self.count+=1

        if self.size()==1:
            self.tail=new_node


    def search(self,value):
        current=self.head
        found=False
        while current!=None and not found:
            if current.getValue()==value:
                return True
            else:
                current=current.getNext()
        return found


    def printList(self):
        temp=self.head
        while temp:
            print(temp.value, end=' ')
            temp=temp.next

linked_list = LinkedList()
linked_list.add(9)
linked_list.add(8)
linked_list.add(7)
linked_list.add(6)
linked_list.add(5)
