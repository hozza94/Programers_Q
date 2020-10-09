from collections import defaultdict, deque

def solution(n, edge):
    routes = defaultdict(list)
    for e1, e2 in edge:
        routes[e1].append(e2)
        routes[e2].append(e1)

    print(routes)

    q = deque([[1, 0]]) # node number, depth
    check = [-1]*(n+1)

    while q:
        print(q)
        index, depth = q.pop()
        check[index] = depth
        for i in routes[index]:
            if check[i]==-1:
                check[i] = 0
                q.append([i, depth+1])
        depth += 1

    print(check)
    return check.count(max(check))

# def solution(n, edge):
#     answer = 0
#
#     dists = {i:0 for i in range(1, n+1)}
#     edges = defaultdict(list)
#
#     for u, v in edge:
#         edges[u].append(v)
#         edges[v].append(u)
#
#     q = deque(edges[1])
#     dist = 1
#     while q:
#         size = len(q)
#         for i in range(size):
#             v = q.popleft()
#
#             if dists[v] == 0:
#                 dists[v] = dist
#                 for w in edges[v]:
#                     q.append(w)
#
#         dist += 1
#
#     del dists[1]
#
#     max_dist = max(dists.values())
#     for i in dists.values():
#         if max_dist == i :
#             answer += 1
#
#     return answer



n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n, vertex))

# defaultdict(<class 'list'>, {3: [6, 4, 2, 1], 6: [3], 4: [3, 2], 2: [3, 1, 4, 5], 1: [3, 2], 5: [2]})
# deque([[1, 0]])
# deque([[3, 1], [2, 1]])
# deque([[2, 1], [6, 2], [4, 2]])
# deque([[6, 2], [4, 2], [5, 2]])
# deque([[4, 2], [5, 2]])
# deque([[5, 2]])
# [-1, 0, 1, 1, 2, 2, 2]
# 3

# defaultdict(<class 'list'>, {3: [6, 4, 2, 1], 6: [3], 4: [3, 2], 2: [3, 1, 4, 5], 1: [3, 2], 5: [2]})
# deque([[1, 0]])
# deque([[3, 1], [2, 1]])
# deque([[3, 1], [4, 2], [5, 2]])
# deque([[3, 1], [4, 2]])
# deque([[3, 1]])
# deque([[6, 2]])
# [-1, 0, 1, 1, 2, 2, 2]
# 3
