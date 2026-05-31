#Dědičnost, method overriding, function overloading
class Animal:
    def __init__(self,name):
        self.name = name 
    #function overloading 
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        
        
    def speak(self):
        return 'zvuk zvuk'
    
class Dog(Animal):
    def __init__(self,name,age,bread):
       super().__init__(name,age)
       self.bread = bread
    def speak(self):
        return 'haf haf'
class Kocka(Animal):
    def __init__(self,name,age,barva):
       super().__init__(name,age)
       self.barva = barva
    def speak(self):
        return 'manu mnau'
    
an =Animal("Azor",11)
p = Dog('Azor2',12,'Ohar')
koc = Kocka('Azor2',12,'bila')
#method overriding 
print(an.speak())
print(p.speak())
print(p.speak())

#
from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def test(self):
        print('A')
class B(A):
    def test(self):
        super().test()
        print("B")
class C(A):
    def test(self):
        super().test()
        print("C")
class D(B,C):
    def test(self):
        super().test()
        print("D")
d = D()
d.test()
    
