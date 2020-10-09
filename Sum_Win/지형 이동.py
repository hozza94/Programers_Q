# 제한사항
# land는 N x N크기인 2차원 배열입니다.
# land의 최소 크기는 4 x 4, 최대 크기는 300 x 300입니다.
# land의 원소는 각 격자 칸의 높이를 나타냅니다.
# 격자 칸의 높이는 1 이상 10,000 이하인 자연수입니다.
# height는 1 이상 10,000 이하인 자연수입니다.

from collections import defaultdict


def solution(land, height):
    answer = 0
    N = len(land)  # Matrix의 길이
    visit = [[0] * N for _ in range(N)]

    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]  # 오른쪽, 아래, 왼쪽. 위 순
    num = 0
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                q = [[i, j]]
                visit[i][j] = num + 1
                while q:
                    print(q)
                    x, y = q[0][0], q[0][1]

                    for k in range(4):
                        kx, ky = x + dx[k], y + dy[k]
                        if 0 <= kx < N and 0 <= ky < N:  # Matrix를 벗어나는지 확인
                            if abs(land[x][y] - land[kx][ky]) <= height:
                                if visit[kx][ky] == 0:
                                    visit[kx][ky] = num + 1
                                    q.append([kx, ky])
                    q.pop(0)
                num += 1
    # 여기까지 height를 기준으로 사다리가 없어도 되는 길만큼 같은 수로 묶어주었음
    print(visit)
    D = defaultdict(list)

    for i in range(N):
        for j in range(N):
            q = [[i, j]]


            print("q1", q)
            while q:
                x, y = q[0][0], q[0][1]
                for k in range(2):
                    kx, ky = x + dx[k], y + dy[k]
                    if 0 <= kx < N and 0 <= ky < N and visit[x][y] != visit[kx][ky]:
                        D[visit[x][y]].append([abs(land[x][y] - land[kx][ky]), visit[kx][ky]])
                    elif [kx, ky] not in q:
                        q.append([kx, ky])
                q.pop(0)

    print(D)


    return answer


land = [[1, 4, 8, 10],
        [5, 5, 5, 5],
        [10, 10, 10, 10],
        [10, 10, 10, 20]]

height = 3
result = 15

print(solution(land, height))
