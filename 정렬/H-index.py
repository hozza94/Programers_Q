# h-index <= n

def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()

    for i in range(n):
        if citations[i] >= n - i:
            answer = max(answer, n-i)

    return answer


citations = [3, 0, 6, 1, 5]

print(solution(citations))

citations = [4, 4, 4, 5, 0, 1, 2, 3]

print(solution(citations))

citations = [0, 0, 1, 1]

print(solution(citations))