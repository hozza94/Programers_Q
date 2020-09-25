# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.

def solution(begin, target, words):
    if begin == target:
        return 0
    elif target not in words:
        return 0
    else:
        count = 0
        visit = [0] * len(words)

        while True:
            temp = []
            for word in words:
                if diff(begin, word):
                    temp.append(word)
            visit[count] = temp
            if target in visit[count]:
                return count

def diff(w1, w2):
    diff_count = 0

    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diff_count += 1

    if diff_count == 1:
        return True
    else:
        return False

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
result = 4

print(solution(begin, target, words))
