class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

print("")
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        #langkah 1
        new = Node(data)

        #langkah 2
        if self.root is None:
            #jika iya
            self.root = new
            return
        
        #langkah 3
        P = self.root
        Q = self.root

        #langkah 4
        while Q is not None and new.data != P.data:

            #langkah 5
            P = Q

            #langkah 6
            if new.data < P.data:
                Q = P.left
            else:
                Q = P.right
        
        #langkah 7:
        if new.data == P.data:
            #jika iya
            print("Datanya duplikat")
            return

        #langkah 8
        if new.data < P.data:
            #jika iya
            P.left = new
        #jika tidak
        else:
            P.right = new

bst = BinarySearchTree()

bst.insert(66)
bst.insert(90)
bst.insert(245)
bst.insert(98)
bst.insert(547)

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" → ")
        inorder(node.right)

inorder(bst.root)

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_root(self,data):
        self.root = Node(data)

    def insert_left(self, parent_node, data):
        if parent_node is None:
            parent_node = Node(data)

        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node

    def insert_right(self, parent_node, data):
        if parent_node.right is None:
            parent_node.right = Node(data)

        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node    

tree = BinaryTree()

tree.insert_root("F")

tree.insert_left(tree.root, "B")
tree.insert_right(tree.root, "G")

tree.insert_left(tree.root.left, "A")
tree.insert_right(tree.root.left, "D")

tree.insert_left(tree.root.left.right, "C")
tree.insert_right(tree.root.left.right, "E")

tree.insert_right(tree.root.right, "I")
tree.insert_right(tree.root.right.right, "H")

print("")
inorder(tree.root)
