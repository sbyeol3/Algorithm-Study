from itertools import combinations
def solution(relation):
    row = len(relation)
    column = len(relation[0])
    if row == 1 : return column
    
    unique = []
    for i in range(column) : 
        col = list(zip(*relation))[i]
        if len(set(col)) == len(col) : unique.append(i)

    for i in range(2,column-len(unique)+1) :
        candidates = list(combinations(list(filter(lambda x: x not in unique, range(column))),i))
        for cnd in candidates :
            isMinimal = True
            for u in unique :
                if type(u)!=int and set(u).issubset(set(cnd)) :
                    isMinimal = False
                    break
            if not isMinimal : continue
            string = []
            for t in relation : string.append(''.join([value for i, value in enumerate(t) if i in cnd]))
            if len(set(string)) == row : unique.append(cnd)

    return len(unique)
    

# 18 19 20 22 25
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
# print(solution([['b','2','a','a','b'],['b','2','7','1','b'],['1','0','a','a','8'],['7','5','a','a','9'],['3','0','a','f','9']]))