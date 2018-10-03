# 784. Letter Case Permutation
# https://leetcode.com/problems/letter-case-permutation
import unittest


# Time complexity: O(n*2^n), Space complexity: O(2^n)
class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        size = len(S)
        res_str = ''
        result = []

        def _dfs(res_str, p):
            if p == size:
                result.append(res_str)
                return

            cur = S[p]
            if cur.isalpha():
                res_str += cur.lower()
                _dfs(res_str, p + 1)
                res_str = res_str[:-1]

                res_str += cur.upper()
                _dfs(res_str, p + 1)
                res_str = res_str[:-1]
            else:
                res_str += cur
                _dfs(res_str, p + 1)

        _dfs(res_str, 0)
        return result


class TestLetterCasePermutation(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(
            sol.letterCasePermutation('a1b2'),
            ['a1b2', 'a1B2', 'A1b2', 'A1B2']
        )
        self.assertEqual(
            sol.letterCasePermutation('3z4'),
            ['3z4', '3Z4']
        )
        self.assertEqual(
            sol.letterCasePermutation('12345'),
            ['12345']
        )


if __name__ == '__main__':
    unittest.TestCase()
