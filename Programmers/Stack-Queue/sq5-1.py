def solution(arrangement):
    answer = []
    cnt = 0
    for i, ch in enumerate(arrangement) :
        if ch == '(': answer.append(ch)
        elif ch == ')' and arrangement[i-1] == '(' : #레이저
            answer.pop()
            cnt = cnt + len(answer)
        elif ch == ')' :
            answer.pop()
            cnt = cnt + 1
    
    return cnt


arrangement = "()(((()())(())()))(())" # 17
print(solution(arrangement))