class Solution:
    def runningSum(self, nums):
        sum, answer = 0, []
        for i in range(len(nums)) :
            num = nums[i]
            sum += num
            answer.append(sum)
        return answer