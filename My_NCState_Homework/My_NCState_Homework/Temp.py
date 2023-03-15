"""
Add comments for you own reference
"""

from collections import defaultdict
import networkx as nx
 
class Tree:
    def __init__(self):
        self.tree = defaultdict(list)
    
    def __str__(self):
        s = ""
        for i in self.tree:
            s += f'\n {i} -> {self.tree[i]}'
        return s
 
    def addEdge(self,u,v):
        self.tree[u].append(v)
    
    def plotTree(self):
        plot = nx.Graph()
        elist = []
        for i in self.tree:
            for j in self.tree[i]:
                elist.append((i,j))
        plot.add_edges_from(elist)
        nx.draw(plot, with_labels = True)
        
    def inorder_traversal(self,root):
        if not self.tree[root]:
            if root!=' ':
                print(root)
        else:
            self.inorder_traversal(self.tree[root][0])
            print(root)
            if len(self.tree[root]) > 1:
                self.inorder_traversal(self.tree[root][1])
                

         
    def preorder_traversal(self,root):
        if not self.tree[root]:
            if root!=' ':
                print(root)
        else:
            print(root)
            self.preorder_traversal(self.tree[root][0])
            if len(self.tree[root]) > 1:
                self.preorder_traversal(self.tree[root][1])

    def postorder_traversal(self,root):
        if not self.tree[root]:
            if root!=' ':
                print(root)
        else:
            
            self.postorder_traversal(self.tree[root][0])
            if len(self.tree[root]) > 1:
                self.postorder_traversal(self.tree[root][1])
                print(root)

"""
Add comments for you own reference
"""

t = Tree()
t.addEdge('f', 'b')
t.addEdge('f', 'g')
t.addEdge('b', 'a')
t.addEdge('b', 'd')
t.addEdge('d', 'c')
t.addEdge('d', 'e')
t.addEdge('g', ' ')
t.addEdge('g', 'i')
t.addEdge('i', 'h')

t.plotTree()
#print(t)
print("INORDER TRAVERSAL")
t.inorder_traversal('f')
print()

print("PREORDER TRAVERSAL")
t.preorder_traversal('f')
print()

print("POSTORDER TRAVERSAL")
t.postorder_traversal('f')
print()