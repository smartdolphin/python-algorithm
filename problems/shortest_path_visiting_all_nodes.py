import unittest
import collections


class Solution:
    def shortestPathLength(self, g_list):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        if not g_list:
            return 0

        size = len(g_list)
        done = (1 << size) - 1
        queue = [(i, 1 << i, 0) for i in range(size)]

        graph = {}
        for i, targets in enumerate(g_list):
            graph[i] = targets
        visited = collections.defaultdict(set)

        while queue:
            node, state, cnt = queue.pop(0)
            if state == done:
                return cnt

            # exploration
            for next_idx in graph[node]:
                new_state = state | 1 << next_idx
                if new_state not in visited[next_idx]:
                    visited[next_idx].add(new_state)
                    queue.append((next_idx, new_state, cnt+1))
        return -1

    def shortestPathLength_v0(self, g_list):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        if not g_list:
            return 0

        graph = {}
        for i, targets in enumerate(g_list):
            graph[i] = targets
        size = len(graph)
        masks = [1 << i for i in range(size)]
        self.done = (1 << size) - 1
        self.int_max = 2 ** 31 - 1
        visit_list = [{masks[idx]} for idx in range(size)]
        shortest = min(self.dfs(graph, idx, 1 << idx, visit_list, {}) for idx in range(size))
        return shortest

    def dfs(self, graph, idx, state, visit_list, memo):
        if (state, idx) in memo:
            return memo[(state, idx)]

        # is finish?
        if self.done == state:
            return 0

        shortest = self.int_max

        # exploration
        for next_idx in graph[idx]:
            new_state = state | 1 << next_idx
            if new_state not in visit_list[next_idx]:
                visit_list[next_idx].add(new_state)
                dist = self.dfs(graph, next_idx, new_state, visit_list, memo)
                if dist != -1:
                    shortest = min(shortest, dist + 1)
                visit_list[next_idx].remove(new_state)
        if shortest == self.int_max:
            return -1
        memo[(state, idx)] = shortest
        return shortest


class TestShortestPathVisitingAllNodes(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(
            sol.shortestPathLength([[1, 2, 3], [0], [0], [0]]),
            4
        )
        self.assertEqual(
            sol.shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]),
            4
        )


if __name__ == '__main__':
    unittest.TestCase()
