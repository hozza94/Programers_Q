def solution(N, number):
    answer = -1
    S = [set() for x in range(8)]

    # n*n나열
    for i, x in enumerate(S, start=1):
        x.add(int(str(N) * i))

    # range(1, len(S)) -> range(0, len(S)) 로 수정. 1부터 하는경우 n == number인 경우를 놓치게 됨..
    for i in range(0, len(S)):
        for j in range(i):
            for op1 in S[j]:
                for op2 in S[i - j - 1]:
                    S[i].add(op1 + op2)
                    S[i].add(op1 - op2)
                    S[i].add(op2 - op1)
                    S[i].add(op1 * op2)
                    if op2 != 0:
                        S[i].add(op1 // op2)

        if number in S[i]:
            answer = i + 1
            break

    return answer


N = 5
number = 12
result = 4

print(solution(N, number))

N = 5
number = 5
result = 1
print(solution(N, number))
