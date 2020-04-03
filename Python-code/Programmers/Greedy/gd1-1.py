def solution(n, lost, reserve):
    lostNum = 0
    if not set(lost).isdisjoint(set(reserve)):
        inter = set(lost) & set(reserve)
        lost = list(filter(lambda x: x not in inter,lost))
        reserve = list(filter(lambda x: x not in inter,reserve))

    for student in lost:
        check = [student-1, student, student+1]
        for c in check:
            if c in reserve:
                reserve.remove(c)
                lostNum += 1
                break
    return n - (len(lost)-lostNum)

print(solution(5,[3,4],[1,3,5]))