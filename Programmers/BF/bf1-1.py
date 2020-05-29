def solution(answers):
    answer = []
    m1 = [1,2,3,4,5]
    m2 = [2,1,2,3,2,4,2,5]
    m3 = [3,3,1,1,2,2,4,4,5,5]
    num = [0,0,0]

    for i, ans in enumerate(answers):
        if ans == m1[i%5] : num[0] = num[0] + 1
        if ans == m2[i%8] : num[1] = num[1] + 1
        if ans == m3[i%10] : num[2] = num[2] + 1

    a1 = num[0]
    a2 = num[1]
    a3 = num[2]
    num.sort(reverse = True)

    if num[0] == a1 : answer.append(1)
    if num[0] == a2 : answer.append(2)
    if num[0] == a3 : answer.append(3)
    return answer


answers = [1,3,2,4,2]
print(solution(answers))