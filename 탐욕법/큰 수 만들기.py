# 제한 조건
# number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
# k는 1 이상 number의 자릿수 미만인 자연수입니다.


def solution(number, k):
    answer = ''
    l = len(number)
    s = []

    for n in number:
        s.append(n)

    start = 0
    mnum = 0
    for i in range(0,l-k):
        if mnum < int(s[i]):
            mnum = int(s[i])
            start = i

    nnum = 99
    for j in range(0,l-start):
        last = 0
        for k in range(start,l):
            if mnum > s[k]:
                mnum

    print(start)



    return answer


number = "4177252841"
k = 4
result = "775841"

print(solution(number, k))
