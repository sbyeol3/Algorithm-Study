# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         sortedNums = sorted(nums)
#         for i in range(len(sortedNums)//2) :
#             if sortedNums[2*i] != sortedNums[2*i+1] : return sortedNums[2*i]
#         return sortedNums[-1]

# Time complexity
from collections import defaultdict
class Solution:
    def singleNumber(self, nums) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        
        for i in hash_table:
            if hash_table[i] == 1:
                return i