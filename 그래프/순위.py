from collections import defaultdict, deque


def solution(n, results):
    answer = 0
    g = defaultdict(list)
    v = [0] * n

    for w, l in results:
        g[w].append(l)

    q = deque([[g, 0]])  # node number, depth
    check = [-1] * (n + 1)

    while q:
        print(q)
        index, depth = q.pop()
        check[index] = depth
        for i in g[index]:
            if check[i] == -1:
                check[i] = 0
                q.append([i, depth + 1])
        depth += 1

    print(g)
    print(v)
    return answer


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
result = 2

print(solution(n, results))

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [4, 1]]
result = 3

print(solution(n, results))

n = 5
results = [[4, 3]]
result = 0

print(solution(n, results))
