# 1470. Shuffle the Array
class Solution:
    def shuffle(self, nums, n: int):
        answer = []
        for i in range(n):
            answer.extend([nums[i],nums[i+n]])
        return answer