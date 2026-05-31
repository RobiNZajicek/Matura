#black box - struktura kodu neznas klikas jak pica  white box - delas kod unittesty grey box - oboji,api - znas streukturu  
#anotamicky manualni 
#FUNKCNI   - konkretni funkce nefunkcni - bezpecnost rychlost skalovatelnost  
#tdd - prvni testy
import unittest 

def soucet(x,y):
    return x/y
    assert y !=0
print(soucet(10,2))


class TestInt(unittest.TestCase):
    def testSoucet(self):
        self.assertEqual(soucet(10,2),5)
        
if __name__ == '__main__':
    unittest.main()


#dasdaddasdasdadasdsad
