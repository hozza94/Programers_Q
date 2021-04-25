from pprint import pprint

def solution(n, results):
    answer = 0
    dist = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for res in results:
        dist[res[0]][res[1]] = 1
        dist[res[1]][res[0]] = -1

    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] == 1:
                for k in range(1, n+1):
                    if dist[j][k] == 1:
                        dist[i][k] == 1


    pprint(dist)

    return answer


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
result = 2

print(solution(n, results))

# n = 5
# results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [4, 1]]
# result = 3
#
# print(solution(n, results))
#
# n = 5
# results = [[4, 3]]
# result = 0
#
# print(solution(n, results))
