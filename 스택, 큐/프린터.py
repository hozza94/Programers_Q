def solution(priorities, location):
    now = [0] * len(priorities)
    order = []

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


    return order.index(1)+1

