def solution(expression):
    operator = ['+', '-', '*']
    combination = [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]
    nums, operation, result = [], [], []
    pointer = 0

    for i, e in enumerate(expression) :
        if e in operator :
            nums.append(int(expression[pointer:i]))
            operation.append(e)
            pointer = i + 1
    nums.append(int(expression[pointer:]))

    for combi in combination:
        numsArr = nums[:]
        opArr = operation[:]
        for c in combi :
            i = 0
            while(len(numsArr)>1 and operator[c] in opArr) :
                op = opArr[i]
                if op == operator[c] :
                    del opArr[i]
                    num1, num2 = numsArr[i:i+2]
                    del numsArr[i:i+2]
                    if c == 0 : numsArr.insert(i,num1+num2)
                    elif c == 1 : numsArr.insert(i,num1-num2)
                    else : numsArr.insert(i,num1*num2)
                else : i += 1
        result.append(abs(numsArr[0]))
    return sorted(result)[-1]        

                
print(solution('100-200*300-500+20')) # 60420
print(solution('50*6-3*2')) # 300