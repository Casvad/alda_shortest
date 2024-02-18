def floyd(adjacency_list, start_node):
    matrix = [[float("Inf")] * len(adjacency_list) for i in range(len(adjacency_list))]
    for i in range(len(matrix)):
        matrix[i][i] = 0
    for i in range(len(adjacency_list)):
        for v, w in adjacency_list[i]:
            matrix[i][v] = w
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]

    ans = {}

    for i in range(len(matrix[start_node])):
        ans[i] = matrix[start_node][i]

    return ans
