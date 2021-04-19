def solution(n, lost, reserve):
    student = [1] * n

    for l in lost:
        student[l-1] -= 1

    for r in reserve:
        student[r-1] += 1

    for i in range(n):
        if student[i] > 1:
            if student[i-1] < 1:
                student[i-1] += 1
            elif student[i+1] < 1:
                student[i+1] += 1
            student[i] -= 1


    print(student)

    return n - student.count(0)


n = 5
lost = [2, 4]
reserve = [1, 3, 5]
result = 5

print(solution(n, lost, reserve))

n = 5
lost = [2, 4]
reserve = [3]
result = 4
print(solution(n, lost, reserve))

n = 4
lost = [3, 1]
reserve = [2, 4]
result = 4
print(solution(n, lost, reserve))
