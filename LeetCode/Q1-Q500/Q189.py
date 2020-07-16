class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        arr = nums[l-k:l] + nums[:l-k]
        for i in range(l):
            nums[i] = arr[i]