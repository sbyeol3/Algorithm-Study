import copy

def solution(heights):
  laser = []
  answer = [0]*len(heights)

  for t in heights: laser.append(t)
  for t in heights:
    temp = laser.pop()
    tmpStack = copy.deepcopy(laser)
    while(len(tmpStack)>0):
      if tmpStack.pop() > temp :
        answer[len(laser)] = len(tmpStack)+1
        break
  
  return answer

'''
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''