def solution(n, computers):
    answer = 0
    visit = [0] * len(computers)

    def dfs(s):
        st = [s]

        while st:
            num = st.pop()
            if visit[num] == 0:
                visit[num] = 1
            for i in range(len(computers[0])):
                if computers[num][i] == 1 and visit[i] == 0:
                    st.append(i)
    i = 0
    while 0 in visit:
        if visit[i] == 0:
            dfs(i)
            answer += 1
        i += 1

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
