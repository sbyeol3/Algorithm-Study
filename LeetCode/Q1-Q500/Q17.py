class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        result = []

        for d in digits:
            if len(result) > 0:
                newResult = []
                while len(result) > 0:
                    string = result.pop()
                    for ch in phone[d]:
                        newResult.append(string + ch)
                result = newResult
            else:
                for ch in phone[d]:
                    result.append(ch)

        return result