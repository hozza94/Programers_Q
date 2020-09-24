def solution(prices):
    L = len(prices)
    answer = [0] * L

    for i in range(L-1):
        for j in range(i, L-1):
            if prices[i] > prices[j]:
                break
            else:
                answer[i] +=1

    return answer

prices = [1, 2, 3, 2, 3]
result = [4, 3, 1, 1, 0]

print(solution(prices))
