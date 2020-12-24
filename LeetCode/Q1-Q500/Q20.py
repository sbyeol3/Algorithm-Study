class Solution:
    def isValid(self, s: str) -> bool:
        OPEN = { '{': 0, '(': 1, '[': 2 }
        CLOSE = { '}': 0, ')': 1, ']': 2 }
        stack = []
        
        for ch in s:
            if ch in [ '{', '(', '['] : stack.append(ch)
            else :
                if len(stack) == 0 : return False
                openBracket = stack.pop()
                if OPEN[openBracket] != CLOSE[ch] : return False
        
        if len(stack) > 0 : return False
        return True