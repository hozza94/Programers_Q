# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.

def solution(begin, target, words):
    if begin == target:
        return 0
    elif target not in words:
        return 0
    else:
        G = dict()
        words.reverse()
        words.append(begin)
        words.reverse()

        # 아마 여기서 시간 초과가 발생할것으로 예상.. 어떻게 수정하지?
        for w1 in words:
            for w2 in words:
                if diff(w1, w2):
                    if w1 in G:
                        G[w1].append(w2)
                    else:
                        G[w1] = [w2]

        answer = []
        st = [begin]

        while st:
            top = st.pop()
            answer.append(top)
            for i in range(len(G[top])):
                st.append(G[top][i])
            if top == target:
                return len(answer) - 1

def diff(w1, w2):
    diff_count = 0

    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diff_count += 1

    if diff_count == 1:
        return True
    else:
        return False
#
# begin = "hit"
# target = "cog"
# words = ["hot", "dot", "dog", "lot", "log", "cog"]
# result = 4

begin = "hit"
target = "hhh"
words = ["hhh","hht"]
result = 2

print(solution(begin, target, words))
