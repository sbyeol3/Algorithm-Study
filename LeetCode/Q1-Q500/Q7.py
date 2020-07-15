class Solution:
    def reverse(self, x: int) -> int:
        MIN = -1 * (2 ** 31)
        MAX = 2 ** 31 - 1
        isNegative = -1 if x < 0 else 1
        xToString = str(x)[1:] if isNegative == -1 else str(x)
        answer = ''
        for c in xToString : answer = c + answer
        answer = int(answer) * isNegative
        if answer < MIN or answer > MAX : return 0
        else : return answer
        