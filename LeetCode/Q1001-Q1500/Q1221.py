class Solution:
    def balancedStringSplit(self, s: str) -> int:
        length = len(s)
        result = 0
        p = 0
        for i in range(length) :
            if s[p:i+1].count('L') == s[p:i+1].count('R') :
                result += 1
                p = i+1
        return result