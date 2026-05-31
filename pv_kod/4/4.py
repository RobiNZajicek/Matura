#Lambda = anonymni metoda

def soucet(a,b):
    return a+b



print(soucet(5,6)) 

soucet2 = lambda x,y,z : x+y+z

print(soucet2(3,1,3))
#hash map = dictionary v python
zbozi = [
    {
        "name" : "IPHONE 14",
        "price" : 22169.0,
        "category" : (12, "Mobilní telefony")
    },
    {
        "name" : "Fujifilm XT30",
        "price" : 2226911.0,
        "category" : (2, "Fotoaparáty")
    },
    {
        "name" : "Niceboy HIVE Pins Black",
        "price" : 999.0,
        "category" : (4, "Sluchátka")
    }
]
price = sorted(zbozi, key=lambda x: x['price'])
print(price)
class Clovek:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f'jmeno {self.name}'
    def __gt__(self, other):
        return
    def __lt__(self,other):
        pass

alovek = Clovek('dadas')
print(alovek)