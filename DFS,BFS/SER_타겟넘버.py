def solution(numbers, target):
    answer = 0
    head =[0]

    for n in numbers:
        child = []
        for h in head:
            child.append(h + n)
            child.append(h - n)
        head = child

    answer = head.count(target)
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
result = 5

print(solution(numbers, target))
