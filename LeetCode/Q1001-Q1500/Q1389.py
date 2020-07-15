class Solution:
    def createTargetArray(self, nums, index):
        length = len(nums)
        target = []
        for i in range(length) :
            num, idx = nums[i], index[i]
            if idx == len(target) : target.append(num)
            else : target.insert(idx,num)
        return target