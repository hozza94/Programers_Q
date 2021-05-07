def solution(n):
    ans = 0

    while True:
        if n == 1:
            ans += 1
            break

        if n % 2 == 1:
            ans += 1

        n = int(n/2)

    return ans


print(solution(5), 2)
print(solution(6), 2)
print(solution(5000), 5)
