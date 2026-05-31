arr = [1,2,3,4,5]
hash_set = (1,2,3,4,5)
dictionary = {'a':1,'b':2}

for i in arr:
    print(i)
print('---------------------------------------------')
for i in hash_set:
    print(i)
    
class Node:
    def __init__(self,value,nextos=None):
        self.value = value
        self.nextos= nextos

A = Node(3)
B = Node(4)
C = Node(5)
D = Node(6)
E = Node(8)
# A -> B ->C
A.nextos = B
B.nextos =C
C.nextos =D
D.nextos =E

def printos(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.value))
        curr = curr.nextos
        print('->'.join(elements))


print(printos(A))