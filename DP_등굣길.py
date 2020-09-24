def solution(m, n, puddles):
    answer = 0
    W = [[0]*(m+1) for _ in range(n+1)] # 행렬 생성
    P = [[0]*(m+1) for _ in range(n+1)] # 찾아갈 행렬 생성

    # 행렬 초기화 작업 -1은 제외되는 부분으로서, 벗어나는지 확인할 도구
    for i in range(m+1):
        W[0][i] = -1
    for j in range(n+1):
        W[j][0] = -1

    # 장애물 추가
    for pud in puddles:
        x = pud[0]
        y = pud[1]
        W[x][y] = -1

    for i in range(n,0,-1):
        for j in range(m,0,-1):
            if W[j-1][i] < 0:
                if W[j][i-1] < 0:
                    if j==1 and i==1:
                        # 정점 도착
                        print("ok")
                    else:
                        print("end")
                else:
                    P[j][i-1] +=1



    print(W)
    return answer

def path (n,m):

    if

m = 4
n = 3
puddles = [[2, 2]]
result = 4

print(solution(m, n, puddles))
