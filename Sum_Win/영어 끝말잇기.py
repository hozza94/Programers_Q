def solution(n, words):
    q = [words[0]]

    for i in range(1, len(words)):
        now = words[i]

        if (now in q) or (q[-1][-1] != now[0]):
            num = (i % n) + 1
            order = int(i / n) + 1
            answer = [num, order]
            break
        else:
            q.append(now)
    else:
        answer = [0, 0]
    return answer


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]), [3, 3])
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure",
                   "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]), [0, 0])
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]), [1, 3])

# 이건... 참고할만하다
# def solution(n, words):
#     for p in range(1, len(words)):
#         if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
#     else:
#         return [0,0]