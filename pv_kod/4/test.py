
#Anonymní metody (Lambda), speciální (magické) metody, statické metody, ukazatel na metodu (delegát)

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age =age
    def __str__(self):
        return f'Ahoj me jmeno je {self.name} a je mi {self.age}'
    def __gt__(self, other):
        return self.age > other.age 
    
    def __lt__(self, other):
        return self.age < other.age
    @staticmethod
    def sound():
        return 'bark bark' 
    
a = Animal('Azor',21)
b = Animal("Azor2", 20)
c = Animal("Azor3", 17)
print(a)
print(a>b)
print(a<c)

#lambda
print(Animal.sound())
soucet = lambda x,y :x+y
x= soucet(3,4)
print(x)

pole =[
    {
        "name":"Azor",
        "age":12,
        "role":"devOps"
    },
    {
        "name":"Robin",
        "age":22,
        "role":"fe"
    },
     {
        "name":"Krystof",
        "age":23,
        "role":"be"
    }
]
oldest = sorted(pole,key=lambda x: x['age'] ,reverse=True )[0]
print(oldest)
#delegat 
def hello ():
    print('hi')
f= hello
f()