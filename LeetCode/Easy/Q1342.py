# 1342. Number of Steps to Reduce a Number to Zero
class Solution:
    def numberOfSteps (self, num: int) -> int:
        result = 0
        while(num) :
            result += 1
            if num % 2 == 0 : num /= 2
            else : num -= 1
        return result