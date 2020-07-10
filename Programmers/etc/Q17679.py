def solution(m, n, board):
    result = 0

    for i in range(m) : board[i] = list(board[i])
    while True:
        block = []

        for i in range(0,m-1):
            line = board[i]
            for j in range(1,n) :
                b = line[j]
                if b == '-' : continue
                if line[j-1] == b :
                    nextLine = board[i+1]
                    if nextLine[j-1] == b and nextLine[j] == b: block.extend([(i,j-1),(i,j),(i+1,j-1),(i+1,j)])
                        
        blockSet = list(set(block))
        if len(blockSet) == 0 : break
        result += len(blockSet)

        blockSet.sort()
        for b in blockSet:
            i, j = b
            board[i][j] = '-'
        for i in range(n):
            for j in range(m-1,0,-1):
                if board[j][i] == '-' :
                    start = j-1
                    value = '-'
                    while(start > -1):
                        if board[start][i] != '-' :
                            value = board[start][i]
                            print(value,start,i)
                            break
                        start -= 1
                    if value != '-' : 
                        board[j][i] = value
                        board[start][i] = '-'
                    else : break
        
    return result

                

# print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])) # 15
# print(solution(6,2, ["DD", "CC", "AA", "AA", "CC", "DD"])) # 12
print(solution(8,5,["HGNHU", "CRSHV", "UKHVL", "MJHQB", "GSHOT", "MQMJJ", "AGJKK", "QULKK"])) # 8
        # print(blockSet)
        # for line in board:
        #     print(line)
