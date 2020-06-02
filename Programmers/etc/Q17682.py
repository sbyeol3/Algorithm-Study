def solution(dartResult):
    stack = []
    dartResult = dartResult.replace('10','!')
    for d in dartResult :
        ascii = ord(d)
        if ascii == 33 : stack.append(10)
        elif ascii < 48 :
            if ascii == 42 :
                if len(stack)==1 : stack[0] *= 2
                else : 
                    for i in range(-2,0): stack[i] *= 2
            else : stack[-1] *= -1
        elif ascii > 57 :
            if ascii == 68 : stack[-1] **= 2
            elif ascii == 84 : stack[-1] **= 3
        else : stack.append(int(d))
    return sum(stack)
print(solution('1S*2T*3S')) # 9