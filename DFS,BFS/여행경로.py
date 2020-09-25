def solution(tickets):
    answer = []
    tickets.sort(reverse=True)
    # tickets.sort()
    routes = dict()
    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]

    ans = []

    st = ['ICN']
    while st:
        top = st[-1]
        if top not in routes or len(routes[top])==0: # 루트안에 top이 존재하지않는다 -> 더이상 갈 곳이 없다. 는 답에 저장
            ans.append(st.pop())
        else:
            st.append(routes[top].pop()) # ex ICN을 시작점으로 하는 것들중에서 가장 알파벳이 빠른것을 저장

    ans.reverse()
    return ans



tickets = [["ICN", "AAA"], ["ICN", "BBB"], ["BBB", "CCC"], ["CCC", "BBB"], ["BBB","ICN"]]
print(solution(tickets))