class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        lettersOfs,lettersOft = dict(), dict()
        for letter in s :
            if letter in lettersOfs : lettersOfs[letter] += 1
            else : lettersOfs[letter] = 1
        
        for letter in t :
            if letter in lettersOft : lettersOft[letter] += 1
            else : lettersOft[letter] = 1
        
        for k in lettersOft.keys() :
            if k not in lettersOfs : return k
            elif lettersOft[k] != lettersOfs[k] : 
                return k