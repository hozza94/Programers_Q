# https://www.acmicpc.net/problem/1260
# DFS와 BFS

from collections import defaultdict

v, e, s = map(int, input().split(" "))
edges = []

for i in range(e):
    v1, v2 = map(int, input().split(" "))
    edges.append([v1, v2])

G = defaultdict(list)

for edge in edges:
    G[edge[0]].append(edge[1])
    G[edge[1]].append(edge[0])

for k in G.keys():
    G[k].sort()

print(edges)
print(G)

visit = [0] * (v + 1)
stack = [s]


def dfs(n):
    visit[n] = 1
    print(n, end=' ')
    for i in G[n]:
        if visit[i] == 0:
            dfs(i)

def bfs(n):
    q = [n]
    visit[n] = 0

    while q:
        top = q.pop(0)
        print(top, end=" ")
        for i in G[top]:
            if visit[i] == 1:
                visit[i] = 0
                q.append(i)


dfs(s)
print()
bfs(s)