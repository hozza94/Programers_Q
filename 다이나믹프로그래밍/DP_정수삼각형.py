def solution(triangle):
    answer = 0
    length = len(triangle)

    W = [[0] * length for _ in range(length)]
    W[0][0] = triangle[0][0]  # 시작 숫자

    for i in range(0, length):
        for j in range(0, i + 1):
            if j == 0:
                W[i][j] = W[i - 1][j] + triangle[i][j]
            else:
                W[i][j] = max(W[i - 1][j - 1] + triangle[i][j], W[i - 1][j] + triangle[i][j])

    print(W)
    answer = max(W[length - 1])
    return answer


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
result = 30

print(solution(triangle))
