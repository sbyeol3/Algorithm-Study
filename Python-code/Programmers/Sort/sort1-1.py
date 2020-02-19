def solution(array, commands):
    sliceArray = []
    answer = []

    for command in commands :
        i = command[0]-1
        j = command[1]
        sliceArray.append(array[i:j])

    for arr in sliceArray:
        arr.sort()

    for i in enumerate(commands):
        answer.append(sliceArray[i[0]][i[1][2]-1])
    return answer

array = [1,5,2,6,3,7,4]
commands = 	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array,commands))