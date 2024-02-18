import heapq


def dijkstra(adjacency_list, start_node):
    shortest = {}

    min_heap = [[0, start_node]]

    while min_heap:
        weight, node = heapq.heappop(min_heap)
        if node not in shortest:
            shortest[node] = weight

        for neighbor, weight2 in adjacency_list[node]:
            if neighbor not in shortest:
                heapq.heappush(min_heap, [weight + weight2, neighbor])

    return shortest
