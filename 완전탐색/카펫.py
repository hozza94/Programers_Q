def solution(brown, yellow):
    answer = []

    for row in range(2500):
        for col in range(0,row+1):
            if 2*(row+col-2) == brown and brown+yellow == row*col:
                answer.append(row)
                answer.append(col)
                return answer


brown = 24
yellow = 24

print(solution(brown,yellow))