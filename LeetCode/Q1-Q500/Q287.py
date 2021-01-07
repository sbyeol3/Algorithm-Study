class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        find = set()
        
        for i in range(len(nums)) :
            find.add(nums[i])
            if len(find) == i : return nums[i]