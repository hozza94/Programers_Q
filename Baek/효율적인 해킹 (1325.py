# https://www.acmicpc.net/problem/1325
# 효율적인 해킹

# input
# 5 4
# 3 1
# 3 2
# 4 3
# 5 3

# output
# 1 2

# 자식의 갯수를 저장해서 최대값 출력
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split(" "))

G = defaultdict(list)
visits = [0] * (N + 1)
count = [0] * (N + 1)
edges = []

for i in range(M):
    v1, v2 = map(int, input().split(" "))
    edges.append([v1, v2])

for edge in edges:
    G[edge[0]].append(edge[1])


# print(G)


def dfs(n):
    visits[n] = 1
    count[n] += 1

    # 시간초과..
    for child in G[n]:
        dfs(child)

    # for child in G[n]:
    #     child_sum[n] += 1
    #     if visits[child] == 0:
    #         child_sum[n] += dfs(child)
    #     else:
    #         child_sum[n] += child_sum[child]
    #
    # return child_sum[n]

def bfs(n):
    q = [n]

    while q:
        top = q.pop(0)
        count[top] += 1

        if visits[top] == 0:
            visits[top] = 1

            for c in G[top]:
                q.append(c)



for i in range(1, N + 1):
    bfs(i)

# for i in range(1, N + 1):
#     if visits[i] == 0:
#         dfs(i)

print(count)
# print(visits)

maxscore = max(count)

for j in range(len(count)):
    if maxscore == count[j]:
        print(j, end=" ")
