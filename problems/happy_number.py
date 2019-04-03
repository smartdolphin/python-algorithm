import unittest


class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True

        val = n
        history = set()
        while True:
            ret = sum([int(x)**2 for x in str(val)])
            if ret == 1:
                return True
            if ret in history:
                return False
            history.add(ret)
            val = ret


class TestHappyNum(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertTrue(sol.isHappy(1))
        self.assertFalse(sol.isHappy(2))
        self.assertTrue(sol.isHappy(19))
        self.assertFalse(sol.isHappy(17))


if __name__ == '__main__':
    unittest.TestCase()
