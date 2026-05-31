#fin
def fin(value):
    if value == 0:
        return 0
    if value ==1:
        return 1
    return fin(value -1) + fin(value -2)
    
#factorial
def factorial(n):
    if n == 0:
        return 1
    if n ==1:
        return 1
    return  n * factorial(n - 1)
print(fin(12))
print(factorial(5))

class Node:
    def __init__(self,value,node_left=None,node_right=None):
        self.value = value
        self.node_left = node_left
        self.node_right = node_right
        
        
#   A 
# B   C
#D E F 


A = Node(1)    
B = Node(2)    
C = Node(3)    
D = Node(4)    
E = Node(5)    
F = Node(6)    

A.node_left = B
A.node_right = C
B.node_left = D
B.node_right = E
C.node_left = F


def preorder(node):
    if node :
        print(node.value)
        preorder(node.node_left)
        preorder(node.node_right)