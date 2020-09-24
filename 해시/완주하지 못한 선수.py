def solution(participant, completion):
    participant.sort()
    completion.sort()

    for n in range(len(completion)):
        if participant[n] != completion[n]:
            return participant[n]

    return participant[-1]


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))
