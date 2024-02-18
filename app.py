import sys

from base.base import BaseSortingTimeGather
from bellman.algorithm import bellman
from dijkstra.algorithm import dijkstra
from floyd.algorithm import floyd

if __name__ == "__main__":
    base_gather = BaseSortingTimeGather([bellman, dijkstra, floyd])
    table = base_gather.take_execution_time(minimum_size=100, maximum_size=800, step=100, samples_by_size=5)
    for row in table:
        print(row)
