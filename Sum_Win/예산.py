def solution(d, budget):
    answer = 0
    d.sort()

    for i in range(len(d)):
        if budget < d[i]:
            break
        else:
            answer += 1
            budget -= d[i]

    return answer


d = [1, 3, 2, 5, 4]
budget = 9
result = 3

print(solution(d, budget))
