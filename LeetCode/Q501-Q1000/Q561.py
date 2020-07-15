class Solution:
    def arrayPairSum(self, nums) -> int:
        arr = sorted(nums)
        n = int(len(nums)/2)
        total = 0
        for i in range(n):
            total += arr[2*i]
        return total
    