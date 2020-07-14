# 1313. Decompress Run-Length Encoded List
class Solution:
    def decompressRLElist(self, nums):
        answer, n = [], int(len(nums)/2)
        for i in range(n) :
            freq, val = nums[2*i], nums[2*i+1]
            temp = [val]*freq
            answer.extend(temp)
        return answer