def solution(a, b):
    answer = ''
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU", ]

    day = 0

    for i in range(a - 1):
        day += month[i]

    day += b
    day = day % 7

    answer = days[day - 1]

    return answer


a = 5
b = 24
result = "TUE"

print(solution(a, b))
