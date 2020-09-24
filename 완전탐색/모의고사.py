# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# answers = [1,2,3,4,5]
# return = [1] //
# answers = [1,3,2,4,2]
# return = [1,2,3]

def solution(answers):
    answer = []
    length = len(answers)

    S1 = [1,2,3,4,5]
    S2 = [2,1,2,3,2,4,2,5]
    S3 = [3,3,1,1,2,2,4,4,5,5]

    while len(S1) < length:
        S1 += S1

    while len(S2) < length:
        S2 += S2

    while len(S3) < length:
        S3 += S3

    C1 = C2 = C3 = 0

    for n in range(length):
        N = answers[n]

        if N == S1[n]:
            C1 += 1
        if N == S2[n]:
            C2 += 1
        if N == S3[n]:
            C3 += 1

    m = max(C1,C2,C3)

    if C1 == m:
        answer.append(1)
    if C2 == m:
        answer.append(2)
    if C3 == m:
        answer.append(3)

    return answer

answers = [1,2,3,4,5,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,5,1,5,5,1,5,1,5]
print(solution(answers))