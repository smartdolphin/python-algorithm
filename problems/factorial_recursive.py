import unittest


def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)


class TestFactorial(unittest.TestCase):
    def test(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(20), 2432902008176640000)


if __name__ is '__main__':
    unittest.TestCase()
