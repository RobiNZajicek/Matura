#staticke typovani
#dynamicke typovani 
s = 'ahoj' # string 
inta = 22 # int
fl = 3.14 #float    
d = True #bool

print(type(s), type(inta), type(fl), type(d))    
x = 7
y = 4
print(x + y)
print(x / y)
print(x // y)  # celé dělení
print(x % y)   # zbytek
print(x ** y)  # mocnina
print(True and False)
print(True or False)
print(not True)
a = 10

print(type(a))
print(a.bit_length())

from typing import T,List

class soucet[T]:
    def soucet(a:T,b:T) -> T:
        return a +b
    
gen_int = soucet[int].soucet(2,2)
gen_float=soucet[float].soucet(2.4,2.66)

print(gen_int)
print(gen_float)
# dodelat generika
# or and + - / *
#anotace

def soucet(a:int,b:int):
    return a+b
    
#struktury
from dataclasses import dataclass,field
from enum import Enum
class Bod:
    a:int
    b:int
class direction(Enum):
    SEVER = 'sever'
    JIH = 'jih'
    
# pouziti
