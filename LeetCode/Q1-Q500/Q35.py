class Solution:
    def searchInsert(self, nums, target: int) -> int:
        for i in range(len(nums)) :
            if nums[i] == target : return i
            elif nums[i] > target : return i
        return len(nums)