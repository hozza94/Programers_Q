# list의 index가 고유번호
# 장르 - 재생수 - 고유번호낮은 순
from collections import defaultdict


def solution(genres, plays):
    answer = []
    d = defaultdict(list)
    c = defaultdict(int)

    for i in range(len(genres)):
        d[genres[i]].append(i)
        c[genres[i]] += plays[i]

    keys = sorted(c, key=lambda x: c[x], reverse=True)

    for k in keys:
        if len(d[k]) < 2:
            answer.append(d[k][0])
        else:
            s = defaultdict(int)
            for l in d[k]:
                s[l] += plays[l]
            maxnum = sorted(s, key=lambda x: s[x], reverse=True)
            if s[maxnum[0]] == s[maxnum[1]] and maxnum[0] > maxnum[1]:
                answer.append(maxnum[1])
                answer.append(maxnum[0])
            answer.extend(maxnum[:2])

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
result = [4, 1, 3, 0]

print(solution(genres, plays))

print(solution(['A', 'A', 'B', 'A', 'B', 'B'], [5, 5, 6, 5, 7, 7]) == [4, 5, 0, 1])
print(solution(["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 1, 2, 4])
print(solution(["classic", "pop", "classic", "pop", "classic", "classic"], [400, 600, 150, 600, 500, 500]) == [4, 5, 1, 3])
print(solution(["classic", "classic", "classic", "classic", "pop"], [500, 150, 800, 800, 2500]) == [4, 2, 3])
