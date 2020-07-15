class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sToArr = s.split(' ')
        words = []
        for word in sToArr :
            if word != '' : words.append(word)
        if len(words) > 0 : return len(words[-1])
        else : return 0