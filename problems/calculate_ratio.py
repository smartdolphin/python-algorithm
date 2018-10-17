import sys
import math
import unittest


class Solution(object):
    def _create_data_structure(self, graph):
        value_map = {}
        for (a, b, c) in graph:
            if a not in value_map:
                value_map[a] = {}
            value_map[a][b] = c
        return value_map

    def _helper(self, src, dst, value_map, visited):
        if dst in value_map[src]:
            return value_map[src][dst]
        visited.add(src)
        for first in value_map[src].keys():
            if first in visited:
                continue
            # should return the ratio between neighbor and dst
            ratio = self._helper(first, dst, value_map, visited)
            if ratio is not None:
                ratio *= value_map[src][first]
                return ratio
        return None

    def calculate_ratio(self, src, dst, graph):
        # create a data structure that can be searched
        value_map = self._create_data_structure(graph)
        # search the data structure for the src, dst, ratio
        if src not in value_map and dst not in value_map:
            raise KeyError('src or dst are not valid')

        # search
        if dst in value_map[src]:
            return value_map[src][dst]
        else:
            return self._helper(src, dst, value_map, set())


class TestCalculateRatio(unittest.TestCase):
    def test(self):
        sol = Solution()
        res = sol.calculate_ratio('USD', 'KOR',
                            [('USD', 'EUR', 0.5),
                             ('EUR', 'JPN', 1.2),
                             ('JPN', 'KOR', 2.0),
                             ('KOR', 'EUR', 0.2),
                             ('JPN', 'USD', 1.5)])
        self.assertTrue(math.fabs(res - 1.2) <= sys.float_info.epsilon)
        res = sol.calculate_ratio('KOR', 'USD',
                              [('USD', 'EUR', 0.5),
                               ('EUR', 'JPN', 1.2),
                               ('JPN', 'KOR', 2.0),
                               ('KOR', 'EUR', 0.2),
                               ('JPN', 'USD', 1.5)])

        self.assertTrue(math.fabs(res - 0.36) <= sys.float_info.epsilon)
        res = sol.calculate_ratio('EUR', 'USD',
                            [('USD', 'EUR', 0.5),
                             ('EUR', 'JPN', 1.2),
                             ('JPN', 'KOR', 2.0),
                             ('KOR', 'EUR', 0.2),
                             ('JPN', 'USD', 1.5)])
        self.assertTrue(math.fabs(res - 1.8) <= sys.float_info.epsilon)


if __name__ == '__main__':
    unittest.TestCase()
