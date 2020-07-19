class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1 : return True
        elif n % 2 == 1 : return False

        while n % 2 == 0 and n > 1 :
            n = n // 2
        if n == 1 : return True
        else : return False