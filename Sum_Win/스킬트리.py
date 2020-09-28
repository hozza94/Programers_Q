# 제한 조건
# 스킬은 알파벳 대문자로 표기하며, 모든 문자열은 알파벳 대문자로만 이루어져 있습니다.
# 스킬 순서와 스킬트리는 문자열로 표기합니다.
# 예를 들어, C → B → D 라면 CBD로 표기합니다
# 선행 스킬 순서 skill의 길이는 1 이상 26 이하이며, 스킬은 중복해 주어지지 않습니다.
# skill_trees는 길이 1 이상 20 이하인 배열입니다.
# skill_trees의 원소는 스킬을 나타내는 문자열입니다.
# skill_trees의 원소는 길이가 2 이상 26 이하인 문자열이며, 스킬이 중복해 주어지지 않습니다.


def solution(skill, skill_trees):
    answer = 0
    fs = [] # 'C' 'B' 'D'

    for s in skill:
        fs.append(s)

    for st in skill_trees:
        first_step = True # 선행스킬을 찍었는가? 선행관련 스킬이 없을때는 통과

        test = []
        for sk in st:
            if sk in fs:
                test.append(sk)

        for i in range(len(test)):
            if test[i] == fs[i]:
                first_step = True
            else:
                first_step = False
                break

        if first_step:
            answer += 1
    # for loop end

    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA", "AQWER"]
result = 2

print(solution(skill,skill_trees))