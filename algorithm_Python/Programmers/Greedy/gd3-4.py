def solution(number, k):
    num = list(number)
    length = len(number)
    tempArr = [(int(x),v) for v,x in enumerate(num)]
    pickNum = []
    pick = 0
    start = 0

    while(pick<k):
        if(start==length-1) : break
        pickArr = []
        not9 = True
        for i in range(start,(start+k-pick+1)):
            if(tempArr[i][0]==9):
                pickTemp = tempArr[i]
                not9 = False
                break
            else: pickArr.append(tempArr[i])
        if not9 : pickTemp = sorted(pickArr, key=lambda x:(-x[0],x[1]))[0]
        for i in range(start,pickTemp[1]): 
            pickNum.append(i)
            pick += 1
        start = pickTemp[1]+1

    if(len(pickNum)!=k) : pickNum.append(length-1)
    while(pickNum): num[pickNum.pop()] = ''
    return ''.join(num)
print(solution("21222222",2))
# 1183