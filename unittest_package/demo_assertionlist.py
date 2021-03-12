import unittest


class TestCaseDemo3(unittest.TestCase):

    def test_assertTrueFalse(self):
        x = True
        self.assertTrue(x, 'x is NOT True')

    def test_assertEquals(self):
        x = 30
        self.assertEqual(x, 30)


if __name__ == '__main__':
    unittest.main(verbosity=1)
