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
        
        
print(preorder(A))
import time 
def bubble_sort(arr):
    arr = arr[:]
    for i in range(len(arr)):
        for j in range(len(arr)-i -1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1] ,arr[j]
                
    return arr
def zmer(name,func):
    start = time.perf_counter()
    func()
    cas = time.perf_counter() - start
    print(f'{name} {cas}s ')
    
for n in [100,400,10000]:
    data = list(range(n,0,-1))
    zmer(f'bubble sort n={n}',lambda data=data: bubble_sort(data))
        