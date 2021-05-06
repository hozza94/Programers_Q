import heapq


def solution(N, roads, K):
    answer = 0
    INF = 999999
    graph = [[] for _ in range(N + 1)]
    dist = [INF for _ in range(N + 1)]
    dist[0] = 0
    # print(dist)

    for road in roads:
        graph[road[0]].append([road[1], road[2]])
        graph[road[1]].append([road[0], road[2]])

    # print(graph)

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))

        dist[start] = 0
        while q:
            d, v = heapq.heappop(q)

            if dist[v] < d:
                continue

            for g in graph[v]:
                cost = d + g[1]

                if cost < dist[g[0]]:
                    dist[g[0]] = cost
                    heapq.heappush(q, (cost, g[0]))

    dijkstra(1)
    # print(dist)

    for i in range(1, N + 1):
        if dist[i] <= K:
            answer += 1

    return answer


N = 6
roads = [[1, 2, 1],
         [1, 3, 2],
         [2, 3, 2],
         [3, 4, 3],
         [3, 5, 2],
         [3, 5, 3],
         [5, 6, 1]]
K = 4
result = 4

print(solution(N, roads, K), 4)
print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3), 4)
