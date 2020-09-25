def solution(array, commands):
    answer = []
    for n in range(len(commands)):
        sarr = array[(commands[n][0]-1) : (commands[n][1])]
        sarr.sort()
        answer.append(sarr[commands[n][2]-1])

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
result = [5, 6, 3]

print(solution(array,commands))