import unittest, os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from lib.class_two import Second

class TestSecond(unittest.TestCase):

    def test_first_param1(self):
        new_class = Second("Hi", "Bye")

        self.assertEqual(new_class.x, "Hi")

    def test_first_param2(self):
        new_class = Second("Hi", "Bye")

        self.assertEqual(new_class.z, "Bye")

if __name__ == '__main__':
    unittest.main()
