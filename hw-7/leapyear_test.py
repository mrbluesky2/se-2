import unittest
from leapyear import leap_year

class test_leapyear(unittest.TestCase):
    def test_leapyear(self):
        self.assertTrue(not leap_year(1))
        self.assertTrue(leap_year(4))
        self.assertTrue(not leap_year(100))
        self.assertTrue(leap_year(400))

if __name__ == '__main__':
    unittest.main()