def bellman(adjacency_list, start_node):
    dist = [float("Inf")] * len(adjacency_list)
    dist[start_node] = 0
    for _ in range(len(adjacency_list) - 1):
        for u in range(len(adjacency_list)):
            for v, w in adjacency_list[u]:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    ## This checks for negative cycles, it doesnt matter in this case
    # for u in adjacency_list:
    #     for v, w in adjacency_list[u]:
    #         if dist[u] != float("Inf") and dist[u] + w < dist[v]:
    #             return -1

    ans = {}

    for i in range(len(dist)):
        ans[i] = dist[i]

    return ans
