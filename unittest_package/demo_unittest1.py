import unittest


class TestClassDemo1(unittest.TestCase):
    def setUp(self):
        print("will run before every test")

    def test_methodA(self):
        print("method A test")

    def test_methodB(self):
        print("method B test")

    def tearDown(self):
        print("will after every test")


if __name__ == '__main__':
    unittest.main(verbosity=3)
