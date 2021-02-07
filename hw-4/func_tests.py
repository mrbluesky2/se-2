import unittest
import math
import func

class TestFuncs(unittest.TestCase):

    def test_average(self):
        # averages: 3, 0, -5
        test_list = [   [1, 2, 3, 4, 5],
                        [-1, 0, 1],
                        [-3, -4, -5, -6, -7]  ]
        
        self.assertEqual(func.average_list(test_list[0]), 3)
        self.assertEqual(func.average_list(test_list[1]), 0)
        self.assertEqual(func.average_list(test_list[2]), -5)

        self.assertRaises(TypeError, func.average_list, 'hey')

    def test_volume(self):
        # volumes: 27, -1
        test_volume = [3*3*3, -1*-1*-1]

        self.assertEqual(func.cube_volume(3), test_volume[0])
        self.assertNotEqual(func.cube_volume(-1), test_volume[1])

        with self.assertRaises(TypeError): func.cube_volume('hey')

    def test_name(self):
        test_name = 'fred greg'
        self.assertEqual(func.make_name('fred', 'greg'), test_name)
        self.assertRaises(TypeError, func.make_name, 1, 0)

if __name__ == '__main__':
    unittest.main()