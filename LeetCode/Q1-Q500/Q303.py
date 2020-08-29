class NumArray:
    
    def __init__(self, nums):
        self.nums = nums
        self.sumArr = [0] * len(nums)
        if (len(nums) > 0) :
            self.sumArr[0] = nums[0]
        
            for i in range(1,len(self.nums)) :
                self.sumArr[i] = self.sumArr[i-1] + self.nums[i]

    def sumRange(self, i: int, j: int) -> int:
        if (i==0): return self.sumArr[j]
        return self.sumArr[j] - self.sumArr[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)