import unittest


class DFS(object):
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, src, dst):
        if src not in self.adjacency_list:
            self.adjacency_list[src] = [dst]
        else:
            self.adjacency_list[src] += [dst]
        if dst not in self.adjacency_list:
            self.adjacency_list[dst] = [src]
        else:
            self.adjacency_list[dst] += [src]

    def dfs(self, start):
        visited = []
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)

            for v in self.adjacency_list[vertex]:
                if v not in visited:
                    stack.append(v)
        return visited


class TestDFS(unittest.TestCase):
    def test(self):
        dfs = DFS()
        edge_set = [[1, 2],
                    [1, 3],
                    [2, 4],
                    [2, 5],
                    [4, 8],
                    [5, 8],
                    [3, 6],
                    [3, 7],
                    [6, 8],
                    [7, 8]]
        for sv, ev in edge_set:
            dfs.add_edge(sv, ev)

        self.assertEqual(
            dfs.dfs(1),
            [1, 3, 7, 8, 6, 5, 2, 4]
        )


if __name__ == '__main__':
    unittest.TestCase()
