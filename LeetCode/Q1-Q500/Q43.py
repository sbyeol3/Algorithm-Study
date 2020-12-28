class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convertInteger(numString) -> int:
            digitsNum = len(numString)
            num = 0
            for i in range(digitsNum) :
                num += 10 ** (digitsNum-i-1) * int(numString[i])
            return num
        return str(convertInteger(num1) * convertInteger(num2))