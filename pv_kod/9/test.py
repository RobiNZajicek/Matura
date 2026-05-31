
x = 155105510

while True:
    try:
        y = int(input('zadej jak chces cislo delit: '))
        result = x/y
        print(result)
        break
    except ZeroDivisionError as err:
        print("nemuzes delit nulou",err)
        
def deleni(x,y):
    return x/y
    assert x!=0
    
print(deleni(2,2))

import unittest

class TestInt(unittest.TestCase):
    def test_deleni(self):
        self.assertEqual(deleni(100,2),50)

        
if __name__ == '__main__':
    unittest.main()
    

