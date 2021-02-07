import unittest
import cube

class TestCube(unittest.TestCase):
    def test_cube1(self):
        self.assertEqual(cube.calculate_cube(2),8)
        self.assertEqual(cube.calculate_cube(3),27)

    def test_cube2(self):
        self.assertEqual(cube.calculate_cube('cube'),"Type Error")
        self.assertEqual(cube.calculate_cube('0'),"Type Error")

    def test_cube3(self):
        self.assertEqual(cube.calculate_cube(1.2),1.728)
        self.assertEqual(cube.calculate_cube(2.5),15.625)


if __name__ == '__main__':
    unittest.main(verbosity=2)