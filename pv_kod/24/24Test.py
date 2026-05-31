
import unittest


def vypocitaniDeleni(a,b):
        result = a/b
        return result
        
print(vypocitaniDeleni(10,2))

class Testing(unittest.TestCase):
    def test_deleni(self):
        self.assertEqual(vypocitaniDeleni(10,2),5)
        

if __name__ == '__main__':
    unittest.main()