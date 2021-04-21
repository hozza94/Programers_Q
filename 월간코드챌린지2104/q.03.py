from collections import defaultdict
import sys
sys.setrecursionlimit(300000)


def solution(a, edges):
    answer = []
    child_sum = [0] * len(a)
    visit = [0] * len(a)
    graph = defaultdict(list)

    if sum(a) != 0:
        return -1

    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)

    def sum_dfs(node):
        score = 0

        if visit[node] == 0:
            visit[node] = 1

            for n in graph[node]:
                if visit[n] == 0:
                    score += sum_dfs(n)

            child_sum[node] = score + a[node]
            answer.append(abs(score + a[node]))

        return child_sum[node]

    sum_dfs(0)

    return sum(answer)


a = [-5, 0, 2, 1, 2]
edges = [[0, 1], [3, 4], [2, 3], [0, 3]]
result = 9

print(solution(a, edges))

a = [0, 1, 0]
edges = [[0, 1], [1, 2]]
result = -1

print(solution(a, edges))
