def solution(number, k):
    num = list(number)
    tempArr = [(int(x),v) for v,x in enumerate(num)]
    length = len(number)
    pickNum = []
    pick = 0
    start = 0

    while(pick<k):
        pickArr = list(filter(lambda x: x[1]>=start and x[1]<=(start+k-pick),tempArr))
        pickTemp = sorted(pickArr, key=lambda x:(-x[0],x[1]))[0]
        for i in range(start,pickTemp[1]): 
            pickNum.append(i)
            pick += 1
        start = pickTemp[1]+1

    while(pickNum): num[pickNum.pop()] = ''
    return ''.join(num)
print(solution("4177252841",4))
# 7, 8, 10 time error, 12 runtime error