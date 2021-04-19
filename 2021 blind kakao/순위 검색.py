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
        else:
            db[str].append(0)

    return answer


infos = ["java backend junior pizza 150",
         "python frontend senior chicken 210",
         "python frontend senior chicken 150",
         "cpp backend senior pizza 260",
         "java backend junior chicken 80",
         "python backend senior chicken 50"]

querys = ["java and backend and junior and pizza 100",
          "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250",
          "- and backend and senior and - 150",
          "- and - and - and chicken 100",
          "- and - and - and - 150"]

result = [1, 1, 1, 1, 2, 4]

# def solution(infos, querys):
#     answer = []
#     info_list = list()
#     for info in infos:
#         info_list.append(info.split(' '))
#     for query in querys:
#         split_query = [_ for _ in query.split(' ') if _ != 'and']
#         res = [info_list[i] for i in range(len(info_list))
#                if (split_query[0] =='-' or split_query[0] == info_list[i][0])
#                and (split_query[1] == '-' or split_query[1] == info_list[i][1])
#                and (split_query[2] == '-' or split_query[2] == info_list[i][2])
#                and (split_query[3] == '-' or split_query[3] == info_list[i][3])
#                and (split_query[4] == '-' or int(split_query[4]) <= int(info_list[i][4]))
#                ]
#         answer.append(len(res))
#     return answer

print(solution(infos, querys))
