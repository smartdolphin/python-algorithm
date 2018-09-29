import unittest


class BFS(object):
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

    def bfs(self, start):
        visited = []
        queue = [start]

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.append(vertex)

            for v in self.adjacency_list[vertex]:
                if v not in visited:
                    queue.append(v)
        return visited


class TestBFS(unittest.TestCase):
    def test(self):
        bfs = BFS()
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
            bfs.add_edge(sv, ev)

        self.assertEqual(
            bfs.bfs(1),
            [1, 2, 3, 4, 5, 6, 7, 8]
        )


if __name__ == '__main__':
    unittest.TestCase()
