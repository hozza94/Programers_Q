def solution(bridge_length, weight, truck_weights):
    answer = 0
    ntruck = len(truck_weights)

    truck_weights.sort() # 4, 5, 6, 7

    mid = [0] * bridge_length # [0,0]
    end = []

    # 가장 작은숫자부터 더해서 진행
    while len(end) < ntruck:
        answer += 1

        if mid[-1] != 0:
            end.append(mid[-1])
            mid[-1] = 0

        for i in range(1, len(mid)):
            mid[i] = mid[i-1]
        mid[0] = 0

        if truck_weights:
            if (sum(mid) + truck_weights[0]) < weight:
                mid[0] = truck_weights.pop(0)

    return answer


bridge_length = 100
weight = 100
truck_weights = [10]
result = 101

print(solution(bridge_length, weight, truck_weights))
#
# 100	100	[10]	101
# 100	100	[10,10,10,10,10,10,10,10,10,10]	110