# 638. Shopping Offers
# https://leetcode.com/problems/shopping-offers
import unittest


class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        return self._helper(price, special, needs, 0, {})

    def _helper(self, price, special, needs, pos, memo):
        if tuple(needs) in memo:
            return memo[tuple(needs)]
        res = self._direct_purchase(price, needs)
        for idx in range(pos, len(special)):
            sale = special[idx]
            temp = []
            for i in range(len(needs)):
                diff = needs[i] - sale[i]
                if diff < 0:
                    break
                temp.append(diff)
            if len(temp) == len(needs):
                res = min(res, sale[-1] + self._helper(price, special, temp, idx, memo))
        memo[tuple(needs)] = res
        return res

    def _direct_purchase(self, prices, needs):
        return sum([price * need for price, need in zip(prices, needs)])


class TestShoppingOffers(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(
            sol.shoppingOffers([2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2]),
            14
        )
        self.assertEqual(
            sol.shoppingOffers([2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1]),
            11
        )


if __name__ == '__main__':
    unittest.TestCase()
