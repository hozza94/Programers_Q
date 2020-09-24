# 제한사항
# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# 013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.


# numbers = 17
# return 3
# numbers = 011
# return 2
#
# 예제 #1
# [1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.
# 예제 #2
# [0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.
# 11과 011은 같은 숫자로 취급합니다.

from itertools import permutations

def check(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = []
    for k in range(1, len(numbers)+1):
        perlist = list(map(''.join, permutations(list(numbers), k)))
        for i in list(set(perlist)):
            if check(int(i)):
                answer.append(int(i))

    answer = len(set(answer))

    return answer

numbers = "17"

print(solution(numbers))
