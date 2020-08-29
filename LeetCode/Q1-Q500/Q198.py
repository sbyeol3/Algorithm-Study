class Solution:
    def rob(self, nums) -> int:
        if (len(nums) == 0) : return 0
        elif (len(nums) == 1) : return nums[0]
        money = [0] * (len(nums))
        money[0] = nums[0]
        money[1] = nums[1]
        
        for i in range (2,len(nums)) :
            if (i == 2) : money[2] = nums[0] + nums[2]
            else : money[i] = max(money[i-2], money[i-3]) + nums[i]
    
        return max(money)