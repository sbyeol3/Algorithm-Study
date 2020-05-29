import math
from itertools import permutations

def solution(numbers):
    def IsPrime(n):
        if ( n == 1 or n == 0) : return False
        elif ( n in [2,3,5,7]) : return True
        
        check = math.sqrt(n)
        i = 2
        while(i<=check):
            if (n % i == 0): return False
            i += 1
        return True

    num = [ x for x in numbers]
    prime = []
    primeCnt = 0

    for i in range(1,len(num)+1):
        permuteList = list(permutations(num,i))
        while(permuteList):
            temp = int(''.join(list(permuteList.pop())))
            if(IsPrime(temp)):
                if(temp not in prime):
                    primeCnt += 1
                    prime.append(temp)
    return primeCnt

print(solution("011"))
# 2, 10, 11 fail