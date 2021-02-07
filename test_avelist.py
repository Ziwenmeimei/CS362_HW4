import unittest
import avelist

class Testlist(unittest.TestCase):
    def test_list1(self):
        self.assertEqual(avelist.calculate_list([2,4,6]),4)
        self.assertEqual(avelist.calculate_list([-1,-3,-5]),-3)
    
    def test_list2(self):
        self.assertEqual(avelist.calculate_list([]),"Empty List")
        self.assertEqual(avelist.calculate_list([2]),2)

    def test_list3(self):
        self.assertEqual(avelist.calculate_list('0'),"Type Error")
        self.assertEqual(avelist.calculate_list('two'),"Type Error")


if __name__ == '__main__':
    unittest.main(verbosity=2)