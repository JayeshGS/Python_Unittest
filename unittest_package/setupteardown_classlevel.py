import unittest


class TestClassDemo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("run before class")

    @classmethod
    def tearDownClass(cls):
        print("run after class")

    def setUp(self):
        print("run before method")

    def tearDown(self):
        print("run after method")

    def test_methodA(self):
        print("test method A")


if __name__ == '__main__':
    unittest.main()
