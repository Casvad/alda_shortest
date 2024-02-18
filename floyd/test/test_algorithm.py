import unittest

from floyd.algorithm import floyd
from utils.constants_test import arrays, expected


class AlgorithmTest(unittest.TestCase):
    def test_floyd(self):
        for i in range(len(arrays)):
            adj_list = arrays[i][1]
            start_node = arrays[i][0]
            result = floyd(adj_list, start_node)
            self.assertEqual(result, expected[i])


if __name__ == "__main__":
    unittest.main()
