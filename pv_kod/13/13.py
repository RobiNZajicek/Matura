#Návrhové vzory - creational design patterns, structural design patterns, behavioral patterns

#creational -singleton,factory
#stactrual - fasada
#behav - command

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


a = Singleton()


print(a)  # True

#Factory
class Pes:
    def speak(self):
        return 'Haf haf'
        
class Kocka:
    def speak(self):
        return'mnau mnau'
        
def animal_factory(animal):
    if animal =='dog':
        return Pes()
    if animal =='kocka':
        return Kocka()
    
factoryos = animal_factory('kocka')
print(factoryos.speak())

#Structural pattern - Facade

class CPU:
    def start(self):
        print('CPU start')
class RAM:
    def load(self):
        print( 'RAM start')
class PC:
    def __init__(self,name):
        self.name = name
        self.cpu = CPU()
        self.ram = RAM()
    def start(self):
        self.cpu.start()
        self.ram.load()

pca = PC('Alza')
pca.start()
#Behavioral pattern
#Command
class Light:
    def on(self):
        print('zapnout svetlo')
class Commad():
    def __init__(self,light):
        self.light = light
    def excute(self):
        self.light.on()
l = Light()  
cmd = Commad(l)
cmd.excute()
