def solution(nums):
    answer = 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if isPrimeNum(nums[i]+nums[j]+nums[k]):
                    answer += 1

    return answer


def isPrimeNum(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True


nums = [1, 2, 7, 6, 4]
result = 4

print(solution(nums))
