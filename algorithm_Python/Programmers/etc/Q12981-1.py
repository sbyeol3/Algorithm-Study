def solution(n, words):
    alreadyWords = [words[0]]
    lastChar = words[0][-1]
    for i in range(1,len(words)):
        if lastChar != words[i][0] or words[i] in alreadyWords:
            return [i%n+1,int((i)/n+1)]
        alreadyWords.append(words[i])
        lastChar = words[i][-1]
    return [0,0]
    

words1 = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
print(solution(3,words1))
words2 = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(2,words2))
words3 = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(3,words3))