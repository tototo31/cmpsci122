class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.value = item

class binaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value, node=None):
        if node == None: # is there a Root?
            self.root = Node(value)
        else:
            if value < node.value: # does the value go on the right or the left
                if node.left == None: # is the left node empty?
                    node.left = Node(value)
                else: # NO? recall the function, but call it using the filled left node
                    self.insert(node.left, value)
            else:
                if node.right == None: # is the right node empty?
                    node.right = Node(value)
                else: # NO? recall the function, but call it using the filled right node
                    self.insert(node.right, value)
