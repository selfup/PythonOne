import unittest, os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from lib.runner import Runner

class TestRunner(unittest.TestCase):

    def test_runner_first(self):
        self.assertEqual(Runner.x.a, "Hi")
        self.assertEqual(Runner.x.b, "Bye")

    def test_runner_second(self):
        self.assertEqual(Runner.x2.x.a, "Hi")
        self.assertEqual(Runner.x2.x.b, "Bye")

if __name__ == '__main__':
    unittest.main()
