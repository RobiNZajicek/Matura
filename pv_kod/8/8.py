class Zvite:
   
    def __init__(self, name, prij):
        self.name = name
        self.prij = prij
    def __str__(self):
        return f'Nas pes se jmenuje {self.name}  '
class Pes(Zvite):
    def __init__(self,name,prij,plemeno):
        super().__init__(name,prij)
        self.plemeo = plemeno
        
    def __str__(self):
        return f'Nas pes se jmenuje {self.name} {self.plemeo} '
        
#z = Zvite('AZOR') # nefunguje
z2 = Zvite('Zvirre','dasdas')
p = Pes('pes','dasdas','huski')

print(z2)
print(p)