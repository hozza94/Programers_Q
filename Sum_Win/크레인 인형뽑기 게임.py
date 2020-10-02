# [제한사항]
# board 배열은 2차원 배열로 크기는 5 x 5 이상 30 x 30 이하입니다.
# board의 각 칸에는 0 이상 100 이하인 정수가 담겨있습니다.
# 0은 빈 칸을 나타냅니다.
# 1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냅니다.
# moves 배열의 크기는 1 이상 1,000 이하입니다.
# moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수입니다.

def solution(board, moves):
    answer = 0
    stack = []
    
    for m in moves:
        i = m-1
        for j in range(len(board)):
            doll = board[j][i]
            board[j][i] = 0
            if doll != 0:
                if not stack:
                    stack.append(doll)
                    break
                else:
                    ldoll = stack.pop()
                    if ldoll == doll:
                        answer += 2
                        break
                    else:
                        stack.append(ldoll)
                        stack.append(doll)
                        break
                # break를 적재적소에 배치할수있도록..
    return answer

# B[i][j] 라고 했을때, i가 인형뽑기의 칸
# j는 0이 맨 위
board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]

moves = [1, 5, 3, 5, 1, 2, 1, 4]
# 4 3 1 1 3 2 4 0
result = 4

print(solution(board, moves))
