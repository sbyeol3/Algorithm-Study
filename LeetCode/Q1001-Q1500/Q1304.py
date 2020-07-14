# 1304. Find N Unique Integers Sum up to Zero
class Solution:
    def sumZero(self, n: int):
        answer = []
        if n == 1 : return [0]
        elif n % 2 == 1 :
            answer = [0]
            for i in range(int((n-1)/2)):
                answer.extend([i+1,-1*(i+1)])
        else :
            for i in range(int((n/2))):
                answer.extend([i+1,-1*(i+1)])
        return answer