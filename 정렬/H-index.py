def solution(citations):
    answer = 0
    count = 0
    prev = 0
    n = len(citations)

    citations.sort(reverse=True)

    for n in range(len(citations)):
        prev = n
        if citations[n] <= 0:
            break

        if n + 1 >= citations[n]:
            if n + 1 == citations[n]:
                answer = n + 1
            elif prev == citations[n]:
                answer = prev

    return answer


citations = [3, 0, 6, 1, 5]

print(solution(citations))
