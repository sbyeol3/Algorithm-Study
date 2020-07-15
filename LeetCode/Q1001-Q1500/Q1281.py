class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product, sum = 1, 0
        for digit in str(n) :
            product *= int(digit)
            sum += int(digit)
        return product - sum