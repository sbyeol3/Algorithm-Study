# 1346. Check If N and Its Double Exist
class Solution:
    def checkIfExist(self, arr) -> bool:
        copyArr = sorted(arr)
        if copyArr.count(0) > 1 : return True
        for num in copyArr :
            if num != 0 and (num*2) in arr : return True
        return False