# 제한사항
# 입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
# 각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
# 심사관은 1명 이상 100,000명 이하입니다.

def solution(n, times):
    answer = 0

    mintime = 1
    maxtime = min(times) * n
    flag = True

    while mintime <= maxtime:
        count = 0

        midtime = (mintime + maxtime) // 2

        for i in range(len(times)):
            count += midtime // times[i]
            if count > n:
                maxtime = midtime

        if count == n:
            answer = midtime
            break
        elif count < n:
            mintime = midtime

    return answer


n = 6
times = [7, 10]
result = 28

print(solution(n, times))
