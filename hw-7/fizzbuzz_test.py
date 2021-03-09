import unittest
from fizzbuzz import fb_value

class test_fizzbuzz(unittest.TestCase):
    def test_fb_value(self):
        self.assertEqual(fb_value(1), '')
        self.assertEqual(fb_value(3), 'Fizz')
        self.assertEqual(fb_value(5), 'Buzz')
        self.assertEqual(fb_value(15), 'FizzBuzz')

if __name__ == '__main__':
    unittest.main()