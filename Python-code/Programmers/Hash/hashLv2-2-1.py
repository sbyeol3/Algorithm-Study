def solution(clothes):
  kind = dict()
  answer = 1

  for i in range(len(clothes)):
    if hash(clothes[i][1]) in kind: kind[hash(clothes[i][1])]+=1
    else: kind[hash(clothes[i][1])]=1
  for key in kind: answer *= (kind[key]+1)
  return answer-1

'''
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''