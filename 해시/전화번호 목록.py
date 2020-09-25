def solution(phone_book):
    answer = True

    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if len(phone_book[i]) > len(phone_book[j]) or i==j:
                continue
            else:
                if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                    return False
    return answer

phone_book = ["123", "456", "789"]
print(solution(phone_book))