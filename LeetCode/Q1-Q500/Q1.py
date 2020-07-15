class Solution:
    def twoSum(self, nums, target: int) :
        numDict = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in numDict:
                numDict[num] = i
            else: return [numDict[n], i]