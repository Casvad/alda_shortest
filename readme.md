# About this repo

Project with 3 shortest path algorithm, Dijkstra's, Bellman-Ford, Floyd-Warshall

## Dijkstra's

Time complexity: `O((V + E) * log(V))`

## Bellman-Ford

Time complexity: `O(VE)`

## Floyd-Warshall

Time complexity: `O(V^3)`

---

# Python version
Python 3.11.0

# Running locally and testing

```
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```

# Check coverage

Make sure you have "coverage" in your requirements.txt file and run pip install. 
Then run `coverage run -m unittest discover` and after that run `coverage report` to get the following table:

```shell
Name                              Stmts   Miss  Cover
-----------------------------------------------------
base/__init__.py                      0      0   100%
base/test/__init__.py                 0      0   100%
bellman/__init__.py                   0      0   100%
bellman/algorithm.py                 12      0   100%
bellman/test/__init__.py              0      0   100%
bellman/test/test_algorithm.py       12      1    92%
dijkstra/__init__.py                  0      0   100%
dijkstra/algorithm.py                12      0   100%
dijkstra/test/__init__.py             0      0   100%
dijkstra/test/test_algorithm.py      12      1    92%
floyd/__init__.py                     0      0   100%
floyd/algorithm.py                   16      0   100%
floyd/test/__init__.py                0      0   100%
floyd/test/test_algorithm.py         12      1    92%
utils/__init__.py                     0      0   100%
utils/constants_test.py               6      0   100%
-----------------------------------------------------
TOTAL                                82      3    96%

```

# Code beautifier
This code has been beautify using black: https://github.com/psf/black. 
The command to use is `black . -l 120`.


