def solution(n, lost, reserve):
    for i in range(1, n + 1):
        if i in reserve and i in lost:
            reserve.remove(i)
            lost.remove(i)

    for i in range(1, n + 1):
        if i in reserve:
            if i - 1 in lost:
                lost.remove(i - 1)
                reserve.remove(i)
            elif i + 1 in lost:
                lost.remove(i + 1)
                reserve.remove(i)

    return n - len(lost)


n = 5
lost = [2, 4]
reserve = [1, 3, 5]
result = 5

print(solution(n, lost, reserve))

n = 4
lost = [3, 2, 1]
reserve = [2, 4, 3]
result = 3
print(solution(n, lost, reserve))

n = 3
lost = [1, 2]
reserve = [2, 3]
result = 2
print(solution(n, lost, reserve))

# 12번 : 3 / [1,2] / [2,3] => 답 : 2
