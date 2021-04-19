# info - 3 x 2 x 2 x 2 = 24개 + 점수

from collections import defaultdict


def solution(info, query):
    answer = []
    db = defaultdict(list)

    for inf in info:
        lang = ["-"]
        end = ["-"]
        car = ["-"]
        foo = ["-"]

        inf = inf.split(" ")
        score = int(inf[-1])
        lang.append(inf[0])
        end.append(inf[1])
        car.append(inf[2])
        foo.append(inf[3])

        for l in lang:
            for e in end:
                for c in car:
                    for f in foo:
                        str = ""
                        str += l + e + c + f
                        db[str].append(score)

    for k in db.keys():
        db[k].sort()

    print(db)

    for q in query:
        q = q.split(" and ")
        a = q.pop().split(" ")
        q.extend(a)
        str = ""
        for s in q[:-1]:
            str += s

        for i in db[str]:
            if int(q[-1]) <= i:
                answer.append(len(db[str]) - db[str].index(i))
                break

    return answer


info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]

result = [1, 1, 1, 1, 2, 4]

print(solution(info, query))
