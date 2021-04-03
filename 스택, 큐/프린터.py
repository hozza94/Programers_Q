def solution(priorities, location):
    now = [0] * len(priorities)
    order = []

    if len(now) == 1:
        return 1

    now[location] = 1

    while priorities:
        top = priorities.pop(0)
        if priorities:
            if top < max(priorities):
                if now.pop(0) == 1:
                    now.append(1)
                else:
                    now.append(0)
                priorities.append(top)
            else:
                if now.pop(0) == 1:
                    order.append(1)
                else:
                    order.append(0)
        elif 1 not in order:
            order.append(now.pop())

    return order.index(1) + 1


# priorities = [2, 1, 3, 2]
# location = 2
# result = 1

priorities = [1, 1, 1]
location = 2
result = 1

print(solution(priorities, location))
