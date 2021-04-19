from collections import defaultdict


def solution(a, edges):
    answer = 0
    graph = defaultdict(list)
    visit = [0] * len(a)
    que = []

    for i in range(len(a)):
        if a[i] == 0:
            visit[i] = 1

    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)

    print(visit)
    print(graph)

    for g in graph:
        if len(graph[g]) == 1 and visit[g] == 0:
            que.append(g)

    print(que)
    while que:
        top = que.pop(0)
        print(que)
        if visit[top] == 0:
            visit[top] = 1

            q = 0
            for g in graph[top]:
                if visit[g] == 0:
                    q = g
            print("q: ", q)

            for i in range(0, abs(a[top])):
                if a[top] == 0:
                    break

                if a[top] > 0:
                    a[top] -= 1
                    a[q] += 1
                else:
                    a[top] += 1
                    a[q] -= 1
                answer += 1

            for g in graph[top]:
                if visit[g] == 0:
                    que.append(g)

    if answer == 0:
        return -1
    return answer


a = [-5, 0, 2, 1, 2]
edges = [[0, 1], [3, 4], [2, 3], [0, 3]]
result = 9

print(solution(a, edges))