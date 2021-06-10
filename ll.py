def solution(t, r):
    answer = []
    # 한대 당 한명 00 이면 01로 바뀜

    for i in range(len(t)):
        small = min(t)

        indexlist = []
        for k in range(len(t)):
            if small == t[k]:
                indexlist.append(k)

        ratinglist = []
        for j in range(len(indexlist)):
            ratinglist.append(r[indexlist[j]])

        minratinglist = []
        minrating = min(ratinglist)
        for l in range(len(ratinglist)):
            if minrating == ratinglist[l]:
                minratinglist.append(indexlist[l])

        top = indexlist.pop(indexlist.index(min(minratinglist)))

        answer.append(top)
        t[top] = 99999
        for idx in indexlist:
            t[idx] += 1

    return answer


t = [1, 0, 0, 4]
r = [0, 0, 0, 2]
result = [1, 0, 2, 3]

print(solution(t, r))
print(solution([7, 6, 8, 1], [0, 1, 2, 3]), [3, 1, 0, 2])
