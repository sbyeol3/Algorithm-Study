class Solution:
    def maxSubArray(self, nums) -> int:
        contiguous = [0] * len(nums)
        contiguous[0] = nums[0]
        
        for i in range(1, len(nums)) :
            contiguous[i] = max(contiguous[i-1]+nums[i], nums[i])
            
        return max(contiguous)