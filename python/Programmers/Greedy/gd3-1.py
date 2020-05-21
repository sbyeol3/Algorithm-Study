from itertools import combinations
def solution(number, k):
    length = len(number)
    pickList = [x for x in range(0,length)]
    permute = list(combinations(pickList,k))
    numArr = []

    while(permute):
        num = list(number)
        cmb = list(permute.pop())
        while(cmb):
            c = cmb.pop()
            num[c] = '*'
        num = list(filter(lambda x: x!='*',num))
        numArr.append(''.join(num))
    
    return sorted(numArr)[-1]
print(solution("4177252841",2))
# time