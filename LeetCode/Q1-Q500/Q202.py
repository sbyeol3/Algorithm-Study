class Solution:
    def isHappy(self, n: int) -> bool:
        already = []
        while n != 1 :
            nToList = list(map(int,list(str(n))))
            n = 0
            for num in nToList :
                n += num ** 2
            if n in already : return False
            else : already.append(n)
            
        return True