import unittest


def multiply(x, y):
    return x+y


class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        test_x = 5
        test_y = 10
        self.assertEqual(multiply(test_x, test_y), test_x*test_y)


if __name__ == "__main__":
    unittest.main()
