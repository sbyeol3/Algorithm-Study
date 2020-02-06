def solution(priorities, location):
    num = location
    printCnt = 0
    
    while num>=0 :
      isHighest = True
      for i in range(1, len(priorities)):
        if priorities[0] < priorities[i] :
          isHighest = False
          break
      tmp = priorities.pop(0) # 1 3 2
      num -= 1 # 1 
      if isHighest == False : 
        if num == -1 : num = len(priorities)
        priorities.append(tmp) # 1 3 2 2
      else : printCnt += 1 

    return printCnt

priorities = [1,1,9,1,1,1]
location = 0
print(solution(priorities,location))