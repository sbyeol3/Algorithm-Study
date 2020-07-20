class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        cnt = 0
        for i in range(length) :
            if i == (length - cnt + 1) : break
            if nums[i] == 0 :
                nums.remove(0)
                nums.append(0)
                cnt += 1
        