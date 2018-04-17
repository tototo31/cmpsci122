### HW#7 due 04/18 at 7:59 AM
# Submission Instructions
#  file name: HW7.py
#  Do NOT change any function name

#### COLLABORATION STATEMENT:
####

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self,new_value):
        self.value = new_value

    def setNext(self,new_next):
        self.next = new_next

    def getPrevious(self):
        return self.prev

    def setPrevious(self,new_prev):
        self.prev = new_prev

    def __str__(self):
        return ("{}".format(self.value))

    __repr__ = __str__



class DoublyLinkedList:

    # Do NOT modify the constructor
    def __init__(self):
        self.head = None

    def addFirst(self, value):
        new_node = Node(value)
        if not self.head is None:
            self.head.setPrevious(new_node)
        new_node.setNext(self.head)
        self.head = new_node
        # write your code here

    def addLast(self, value):
        pos = self.head
        new_node = Node(value)
        if not self.head is None:
            while not pos.getNext() is None:
                pos = pos.getNext()
        #create Links
        else:
            self.head = new_node
        pos.setNext(new_node)
        new_node.setPrevious(pos)
         # write your code here

    def addBefore(self, pnode_value, value):
        new_node = Node(value)
        pos = self.head
        while not pos is None and not pos.getValue() == pnode_value:
            pos = pos.getNext()
        if not pos.getPrevious() is None:
            pos.getPrevious().setNext(new_node)
        new_node.setNext(pos)
        new_node.setPrevious(pos.getPrevious())
        pos.setPrevious(new_node)
         # write your code here

    def addAfter(self, pnode_value, value):
        new_node = Node(value)
        pos = self.head
        while not pos is None and not pos.getValue() == pnode_value:
            pos = pos.getNext()
        if not pos.getNext() is None:
            pos.getNext().setPrevious(new_node)
        new_node.setNext(pos.getNext())
        new_node.setPrevious(pos)
        pos.setNext(new_node)
         # write your code here

    def printDLL(self):
        temp=self.head
        print("\nTraversal Head to Tail")
        while temp:
            print(temp.getValue(), end=' ')
            last = temp
            temp=temp.getNext()

        print("\nTraversal Tail to Head")
        while(last is not None):
            print(last.getValue(), end=' ')
            last = last.prev

    def getNode(self,value):
        current=self.head
        found=False
        while current!=None and not found:
            if current.getValue()==value:
                found=True
                return current
            else:
                current=current.getNext()
        return



# def main():
#     dll=DoublyLinkedList()
#     dll.addFirst(5)
#     dll.addFirst(9)
#     dll.addFirst(4)
#     dll.addFirst(3)
#     print(dll.head)
#     dll.addLast(8)
#     dll.addLast(12)
#     dll.addLast(56)
#     dll.printDLL()
#     dll.addBefore(56,44)
#     dll.printDLL()
#     print()
#     dll.addBefore(9,32)
#     dll.printDLL()
#     print()
#     dll.addAfter(56,756)
#     dll.printDLL()
#     print()
#     dll.addAfter(8,47)
#     dll.printDLL()
#     print()
#     dll.addLast(999)
#     dll.addFirst(856)
#     print(dll.head)
#     dll.printDLL()



# main()
