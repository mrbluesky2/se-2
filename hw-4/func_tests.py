import unittest
from func import cube_volume, average_list, make_name

class TestFuncs(unittest.TestCase):

    def test_volume(self):
        # volumes: 27, -1
        test_volume = [3*3*3, -1*-1*-1]

        self.assertEqual(cube_volume(3), test_volume[0])
        self.assertNotEqual(cube_volume(-1), test_volume[1])

        with self.assertRaises(TypeError): cube_volume('error')


    def test_average(self):
        # averages: 3, 0, -5
        test_list = [   [1, 2, 3, 4, 5],
                        [-1, 0, 1],
                        [-3, -4, -5, -6, -7],
                        []  ]
        
        self.assertEqual(average_list(test_list[0]), 3)
        self.assertEqual(average_list(test_list[1]), 0)
        self.assertEqual(average_list(test_list[2]), -5)
        self.assertEqual(average_list(test_list[3]), 0)

        with self.assertRaises(TypeError): average_list('error')


    def test_name(self):
        test_name = [ 'will smith', '23nghu *&jkf' ]

        self.assertEqual(make_name('will', 'smith'), test_name[0])
        self.assertEqual(make_name('23nghu', '*&jkf'), test_name[1])
        self.assertEqual(make_name('', ''), '')

        with self.assertRaises(TypeError): make_name(1, 0)


if __name__ == '__main__':
    unittest.main()