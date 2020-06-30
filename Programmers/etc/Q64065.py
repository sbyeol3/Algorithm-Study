def solution(s):
    answer = []
    setArray = s[1:-2].replace('{','').split('},')
    sortArray = ['']*len(setArray)

    for string in setArray :
        frag = list(map(int,string.split(',')))
        fragLength = len(frag)
        sortArray[fragLength-1] = frag
    
    for frag in sortArray :
        for f in frag :
            if f not in answer : answer.append(f)
    return answer

# print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")) # [2,1,3,4]
print(solution("{{20,111},{111}}")) # [123]
# print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")) # [3,2,4,1]