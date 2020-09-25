def solution(numbers):
    numbers = sorted(list(map(str, numbers)), key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


# >>> a = [1,2,3]>>> "".join(map(str, a))'123'

numbers = [3, 30, 34, 5, 9]
result = "9534330"

print(solution(numbers))