#grafy - vrcholy a hrahy 
#stromy - bez cyklu  
#dfs -inorder,postoreder,inorder a bfs

class Node:
    def __init__(self,value,node_left,node_right):
        self.value = value
        self.node_left = node_left
        self.node_right = node_right
    def __str__(self):
       return f'{self.name}'
    
   
A = Node(2)
    
B = Node(3)
C = Node(4)
D = Node(5)
E = Node(6)
F = Node(7)
A.node_left = B 
A.node_right = C

B.node_left =D
B.node_right = E    
C.node_left = F
#    A
#  B    C
#D   E F   

def postorder(node):
    if node:
        postorder(node.node_left)
        postorder(node.node_right)
        print(node.value)
#stav prostor h veze 
# co je stav 

#sorting 
#bubble 
#insertion ,marge , quick sort,counting sort , heap sort , selection sort 

#bubble sort - kdyz cas navic