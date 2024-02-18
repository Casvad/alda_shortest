import unittest

from bellman.algorithm import bellman
from utils.constants_test import arrays, expected


class AlgorithmTest(unittest.TestCase):
    def test_bellman(self):
        for i in range(len(arrays)):
            adj_list = arrays[i][1]
            start_node = arrays[i][0]
            result = bellman(adj_list, start_node)
            self.assertEqual(result, expected[i])


if __name__ == "__main__":
    unittest.main()
