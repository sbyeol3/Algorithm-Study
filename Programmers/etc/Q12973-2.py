def solution(s):
    s = list(reversed(list(s)))
    stack = [s.pop()]
    while s :
        c = s.pop()
        if len(stack) == 0 or stack[-1] != c : stack.append(c)
        else : stack.pop()

    if len(stack) == 0 : return 1
    else : return 0
            
print(solution('baabaa'))
