class Solution:
    def findNumbers(self, nums) -> int:
        answer = 0
        for num in nums :
            if len(str(num)) % 2 == 0 : answer += 1
        return answer