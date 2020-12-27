class Solution:
    def countSegments(self, s: str) -> int:
        return len(list(filter(lambda word: word != '', s.strip().split(' '))))