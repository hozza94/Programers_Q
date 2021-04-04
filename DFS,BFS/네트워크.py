def solution(n, computers):
    answer = 0
    visit = [0] * len(computers)
    st = []

    for i in range(len(computers)):
        if visit[i] == 0:
            visit[i] = 1
            for j in range(i+1, len(computers)):
                if computers[i][j] == 1:
                    st.append(j)
        else:
            pass

    print(st)
    return answer


# n	computers	return
# 3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
# 3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1

n = 3
computers = [[1, 1, 0],
             [1, 1, 0],
             [0, 0, 1]]
result = 2

# n = 6
# computers = [[1, 1, 0, 0, 0, 0],
#              [1, 1, 1, 0, 0, 0],
#              [0, 1, 1, 1, 0, 0],
#              [0, 0, 1, 1, 1, 0],
#              [0, 0, 0, 1, 1, 1],
#              [0, 0, 0, 0, 1, 1]]
# result = 2

print(solution(n, computers))
