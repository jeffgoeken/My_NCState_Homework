class Node:
    def __init__(self,Data):
        self.data = Data
        self.right = None
        self.left = None

    def search(self,target):
        if self.data == target:
            print ("Found it")
            return self.data

        if self.left and self.data > target:
            return self.left.search(target) 
        
        if self.right and self.data < target:
            return self.right.search(target)

        return "Value is not in tree"
    
    def preOrderTraversal(self):
        print(self.data)

        if self.left:
            self.left.preOrderTraversal()
        
        if self.right:
            self.right.preOrderTraversal()

    def InorderTraversal(self):
        if self.left:
            self.left.preOrderTraversal()

            print(self.data)
        
        if self.right:
            self.right.preOrderTraversal()
    
    def PostorderTraversal(self):
        if self.left:
            self.left.preOrderTraversal()
        
        if self.right:
            self.right.preOrderTraversal()

        print(self.data)

    

class Tree:
    def __init__(self,Root,Name):
        self.root = Root
        self.name = Name

    def search(self,target):
        return self.root.search(target)
    
    def InorderTraversal(self):
        return self.root.InorderTraversal()
    
    def PreOrderTraversal(self):
        return self.root.PreorderTraversal()
    
    def PostorderTraversal(self):
        return self.root.PostorderTraversal()

    def __str__(self):
        return f'This tree is named {self.name}. The root node is {self.root.data}'

node = Node(50)

node.left = Node(25)
node.right = Node(75)

node.left.left = Node(10)
node.left.right = Node(35)

node.left.left.left = Node(5)
node.left.left.right = Node(13)

node.left.right.left = Node(30)
node.left.right.right = Node(42)

#print(node.right.right.data)

mytree = Tree(node,'Jeff\'s Tree')

#print(mytree.root.right.right.data)

mytree.PreorderTraversal()

