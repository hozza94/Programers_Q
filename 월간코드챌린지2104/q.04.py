from pprint import pprint


def solution(n, z, roads, queries):
    answer = []
    w = [[0 for _ in range(n)] for _ in range(n)]
    v = set()

    roads.sort()

    for r in roads:
        v.add(r[0])
        v.add(r[1])
        w[r[0]][r[1]] = r[2]
    v = list(v)

    pprint(w)
    print(v)

    return answer


n = 5
z = 5
roads = [[1, 2, 3], [0, 3, 2], [0,1,2]]
queries = [0, 1, 2, 3, 4, 5, 6]
result = [0, -1, 1, 2, 3, 1, 4]


print(solution(n, z, roads, queries))
