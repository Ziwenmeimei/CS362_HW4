import unittest
import name

class TestName(unittest.TestCase):
    def test_name1(self):
        self.assertEqual(name.add_name("Ziwen","Tong"), "Ziwen Tong")
        self.assertEqual(name.add_name("Chaowen","Tong"),"Chaowen Tong")

    def test_name2(self):
        self.assertEqual(name.add_name("Pallavi","Roy"),"Pallavi Roy")
        self.assertEqual(name.add_name("Aman","Verma"),"Aman Verma")

    def test_name3(self):
        self.assertEqual(name.add_name('432fs3',1), "Type Error")
        self.assertEqual(name.add_name("2","1"), "2 1")
if __name__ == '__main__':
    unittest.main(verbosity=2)