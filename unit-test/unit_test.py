import unittest

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b
    
def division(a, b):
    if b == 0: return 0
    else: return a / b

class testArithmetic(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(a.addition(6, 2), 8)
        self.assertEqual(a.addition(12, 4), 16)
    
    def test_subtraction(self):
        self.assertEqual(a.subtraction(6, 2), 4)
        self.assertEqual(a.subtraction(12, 4), 8)

    def test_division(self):
        self.assertEqual(a.division(6, 2), 3)
        self.assertEqual(a.division(12, 3), 4)

    def test_multiplication(self):
        self.assertEqual(a.multiplication(6, 2), 12)
        self.assertEqual(a.multiplication(12, 4), 48)

if __name__ == '__main__':
    unittest.main()