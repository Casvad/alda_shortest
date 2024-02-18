import unittest

from dijkstra.algorithm import dijkstra
from utils.constants_test import arrays, expected


class AlgorithmTest(unittest.TestCase):
    def test_dijkstra(self):
        for i in range(len(arrays)):
            adj_list = arrays[i][1]
            start_node = arrays[i][0]
            result = dijkstra(adj_list, start_node)
            self.assertEqual(result, expected[i])


if __name__ == "__main__":
    unittest.main()
