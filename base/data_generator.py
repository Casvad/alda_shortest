import random

from utils import constants


def get_random_list(size, limit=constants.MAX_VALUE):
    answer = []
    while len(answer) < size:
        answer.append(random.randint(0, limit))
    return answer


def get_random_adj_list(size):
    answer = []

    for i in range(size):
        nodes = []
        for j in range(get_random_x(size)):
            nodes.append((get_random_x(size), get_random_x(size)))
        answer.append(_unique(nodes))
    return answer


def get_random_x(limit=constants.MAX_VALUE):
    return random.randint(1, limit - 1)


def _unique(list1):
    unique_indexes = []
    index_mapping = {}

    for (i, j) in list1:
        if i not in index_mapping:
            index_mapping[i] = j
            unique_indexes.append((i, j))
    return unique_indexes
