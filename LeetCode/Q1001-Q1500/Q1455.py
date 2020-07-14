class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')
        length = len(words)
        
        for i in range(length) :
            if words[i].startswith(searchWord) :
                return i + 1
        return -1