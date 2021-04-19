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

        # 문제는 이곳에서 무한 반복이 일어나는 경우가 생김 like hit-hot-lot-hot-lot
        while st:
            top = st.pop()
            if top not in answer:
                answer.append(top)
            for i in range(len(G[top])):
                if G[top][i] not in answer:
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
words = ["hhh", "hht"]
result = 2

print(solution(begin, target, words))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"]), 1)
print(solution("1234567000", "1234567899", [
    "1234567800", "1234567890", "1234567899"]), 3)
print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"]), 4)
