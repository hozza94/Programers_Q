def solution(people, limit):
    answer = 0
    people.sort()

    left = 0
    right = len(people) -1

    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1

    if left == right:
        answer += 1

    return answer


people = [70, 50, 80, 50, 100]
limit = 100
result = 4

print(solution(people, limit))

people = [10, 20, 30, 40, 50, 60, 70, 80, 90]
limit = 100
result = 5

print(solution(people, limit))
