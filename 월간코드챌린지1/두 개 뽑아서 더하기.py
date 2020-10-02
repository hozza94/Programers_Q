def solution(numbers):
    answer = []
    L = len(numbers)
    S1 = set()
    for i in range(L):
        for j in range(i + 1, L):
            S1.add(numbers[i] + numbers[j])
    answer = list(S1)
    answer.sort()
    return answer


numbers = [5, 0, 2, 7]
result = [2, 5, 7, 9, 12]

print(solution(numbers))
