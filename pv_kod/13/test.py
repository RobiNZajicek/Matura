#creational - factory 
#behavioral - command
#structural - fasade


class Pes:
    def Zvuk(self):
        return 'Haf Haf'
class Kocka:
    def Zvuk(self):
        return 'Maw maw '
    
def factory_func(zvite):
    if zvite =='dog':
        return Pes()
    if zvite =='cat':
        return Kocka()
    
pes = Pes()
kocka = Kocka()
fac =factory_func('dog')
print(fac.Zvuk())

#structural Fasade
class CPU:
    def start(self):
        print('CPU started')
class RAM:
    def load(self):
        print('RAM loaded')
class Computer:
    def __init__(self,name):
        self.name = name
        self.cpu = CPU()
        self.ram = RAM()
    def execute(self):
        self.cpu.start()
        self.ram.load()
        
c = Computer('Alza Ui9')
print(c.execute())

#behavioral 
class Light:
    def on(self):
        print('the light is on')
class Command:
    def __init__(self,light):
        self.light = light
    def execute(self):
        self.light.on()
        
l = Light()
command = Command(l)
print(command.execute())