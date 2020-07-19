class Solution:
    def addDigits(self, num: int) -> int:
        while num>9 :
            numToString = str(num)
            sum = 0
            for c in numToString : sum += int(c)
            num = sum
        return num