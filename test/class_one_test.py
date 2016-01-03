import unittest, os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from lib.class_one import First

class TestFirst(unittest.TestCase):

    def test_first_param1(self):
        new_class = First("Hi", "Bye")

        self.assertEqual(new_class.a, "Hi")

    def test_first_param2(self):
        new_class = First("Hi", "Bye")

        self.assertEqual(new_class.b, "Bye")

if __name__ == '__main__':
    unittest.main()
