def solution(p):
    open, close = '(', ')'

    def sliceArr(arr) :
        u, v = [], []
        arr = list(arr)
        length = len(arr)
        for i in range(length) :
            if arr[:i+1].count(open) == arr[:i+1].count(close) :
                u.extend([arr[:i+1]])
                v.extend([arr[i+1:]])
                break
        return u, v
   
    def isProper(arr):
        stack = []
        copyArr = arr[:]
        for ch in copyArr :
            if ch == open : stack.append(open)
            else :
                if len(stack) == 0 : return False
                else : stack.pop()
        return True

    def makeProperString(p):
        if p == '' : return p
        elif isProper(p) : return ''.join(p)
        u, v = sliceArr(p)
        if isProper(u) :
            makeProperString(v)
            return ''.join(u) + ''.join(v)
        else :
            result = open + makeProperString(v) + close
            uSub = u[1:-1]
            for i in range(len(uSub)) :
                if uSub[i] == open : uSub[i] = close
                else : uSub[i] = open
            return result + ''.join(uSub)

    answer = makeProperString(list(p))
    return answer
    
# print(solution("()"))
print(solution("()))(("))