import unittest

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b
    
def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return ZeroDivisionError

class testArithmetic(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(6, 2), 8)
        self.assertEqual(addition(12, 4), 16)
    
    def test_subtraction(self):
        self.assertEqual(subtraction(6, 2), 4)
        self.assertEqual(subtraction(12, 4), 8)

    def test_division(self):
        self.assertEqual(division(1, 0), ZeroDivisionError)
        self.assertEqual(division(6, 2), 3)
        self.assertEqual(division(12, 3), 4)

    def test_multiplication(self):
        self.assertEqual(multiplication(6, 2), 12)
        self.assertEqual(multiplication(12, 4), 48)

if __name__ == '__main__':
    unittest.main()