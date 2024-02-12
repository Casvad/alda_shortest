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

```

# Code beautifier
This code has been beautify using black: https://github.com/psf/black. 
The command to use is `black . -l 120`.


