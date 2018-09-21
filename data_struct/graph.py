import unittest


class Graph(object):
    def __init__(self, size):
        self.adjacency_list = list()
        for _ in range(size):
            self.adjacency_list.append(list())
        self.num_vertices = size

    def add_edge(self, src, dst):
        self.adjacency_list[src].append(dst)
        self.adjacency_list[dst].append(src)

    def get_adjacency_list(self, index):
        sublist = list(self.adjacency_list[index])
        return sublist

    def __getitem__(self, index):
        return self.get_adjacency_list(index)


class TestQueue(unittest.TestCase):
    def test(self):
        # 2 <= VERTEX <= 100, 1 <= EDGE <= 1000
        vertex = 6
        graph = Graph(vertex)
        edge_set = [[0, 1], [0, 2], [0, 3],
                    [1, 2], [1, 4], [3, 4], [4, 5]]
        for sv, ev in edge_set:
            graph.add_edge(sv, ev)

        self.assertEqual(
            graph[0], [1, 2, 3]
        )
        self.assertEqual(
            graph[2], [0, 1]
        )
        self.assertEqual(
            graph[4], [1, 3, 5]
        )

        vertex = 9
        graph = Graph(vertex)
        edge_set = [[0, 1], [0, 2], [0, 6], [1, 3], [1, 4],
                    [1, 7], [2, 4], [4, 5], [6, 7], [7, 8]]
        for sv, ev in edge_set:
            graph.add_edge(sv, ev)
        self.assertEqual(
            graph[0], [1, 2, 6]
        )
        self.assertEqual(
            graph[1], [0, 3, 4, 7]
        )
        self.assertEqual(
            graph[7], [1, 6, 8]
        )


if __name__ == '__main__':
    unittest.TestCase()
