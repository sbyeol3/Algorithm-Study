from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        N, n = len(s), len(p)
        anagrams = dict(Counter(p))
        pointer = 0
        result = []
        
        while pointer < N :
            ch = s[pointer]
            if pointer >= n and s[pointer-n] in anagrams :
                anagrams[s[pointer-n]] += 1
            if ch in anagrams :
                anagrams[ch] -= 1
                if set(anagrams.values()) == {0} : result.append(pointer-n+1)
            pointer += 1
        
        return result