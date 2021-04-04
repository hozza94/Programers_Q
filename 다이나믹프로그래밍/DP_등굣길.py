def solution(m, n, puddles):
    answer = 0
    W = [[0] * (m + 1) for _ in range(n + 1)]  # 행렬 생성
    P = [[0] * (m + 1) for _ in range(n + 1)]  # 찾아갈 행렬 생성

    # 행렬 초기화 작업 -1은 제외되는 부분으로서, 벗어나는지 확인할 도구
    for i in range(m + 1):
        W[0][i] = -1
    for j in range(n + 1):
        W[j][0] = -1

    # 장애물 추가
    for pud in puddles:
        y = pud[0]
        x = pud[1]
        W[x][y] = -1

    # 도착점부터 체크
    W[n][m] = P[n][m] = 1

    for i in range(n, 0, -1):
        for j in range(m, 0, -1):
            if W[i][j] == 0:  # 아래 테두리에선 오른쪽 값만, 오른쪽 테두리에선 아랫값만 신경써주면 된다
                if j == m:
                    P[i][j] = P[i + 1][j] % 1000000007
                elif i == n:
                    P[i][j] = P[i][j + 1] % 1000000007
                else:
                    P[i][j] = P[i][j + 1] + P[i + 1][j] % 1000000007

    print(P)
    print(W)
    return P[1][1] % 1000000007


# def path (n,m):
#
#     if

# m = 4
# n = 3
# puddles = [[2, 2]]
# result = 4

m = 5
n = 4
puddles = [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4]]

print(solution(m, n, puddles))
