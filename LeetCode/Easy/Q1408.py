class Solution:
    def stringMatching(self, words):
        result = []
        length = len(words)
        
        for i in range(length) :
            word = words[i]
            for j in range(length) :
                if i != j and word in words[j] :
                    result.append(word)
                    break
                    
        return result