def solution(board, moves):
    result = 0
    stack = []
    top = 0
    for i in range(len(moves)) :
        mv = moves[i]
        if sum(board[mv-1]) == 0 : continue
        t = board[mv-1][-1]
        while t == 0 and len(board[mv-1]) > 0 :
            t = board[mv-1].pop()
        if t == top : 
            stack.pop()
            result += 1
            if len(stack) > 0 : top = stack[-1]
            else : top = 0
        else :
            stack.append(t)
            top = t
    return result



print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))