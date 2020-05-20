def solution(s):
    s = s.split(' ')
    answer = []
    for word in s :
       answer.append(word.lower().capitalize())
    return ' '.join(answer)

print(solution("3people unFollowed me"))