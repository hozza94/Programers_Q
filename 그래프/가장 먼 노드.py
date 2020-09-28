from collections import defaultdict, deque

def solution(n, edge):
    answer = 0

    dists = {i:0 for i in range(1, n+1)}
    edges = defaultdict(list)

    for u, v in edge:
        edges[u].append(v)
        edges[v].append(u)

    q = deque(edges[1])
    dist = 1
    while q:
        size = len(q)
        for i in range(size):
            v = q.popleft()

            if dists[v] == 0:
                dists[v] = dist
                for w in edges[v]:
                    q.append(w)

        dist += 1

    del dists[1]

    max_dist = max(dists.values())
    for i in dists.values():
        if max_dist == i :
            answer += 1

    return answer



n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n, vertex))