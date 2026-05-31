
#Adresování a správa paměti - Garbage collecting, Reference/ukazatele, Struktura paměti programu

#Ram - 1.Heap -  
#      2.Stack - 

a = 10
b = 11
c = 10 

strin = 'aaaaaa'

print(id(a))
print(id(b))
print(id(c))
print(id(strin))
strin = 'dsadasdasdasd'
print(id(strin))

print(a is c)


jazyky  = ['java','c#','ruby','python','swift']

print(id(jazyky))
jazyky.append('kotlin')
print(id(jazyky))

d = [1,2]
f =d
# 2 reference
# lokalni promena na stacku 
# test funkce na heapu
def test():
    x=5