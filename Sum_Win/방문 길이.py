def solution(dirs):
    answer = 0
    DELTA = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    visited = set()
    x, y = 0, 0  # position

    for command in dirs:
        dx, dy = DELTA[command]
        nx, ny = x + dx, y + dy


    return answer


dirs = "ULURRDLLU"
result = 7

print(solution(dirs))
