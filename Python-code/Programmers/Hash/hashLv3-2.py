from collections import defaultdict

def solution(genres, plays):
  answer = []
  dictGenres = defaultdict(list)
  totalPlayes = defaultdict(lambda:0)

  for g, p in zip(genres, plays): totalPlayes[hash(g)] += p
  sTP = sorted(totalPlayes.items(), key=lambda x: x[1], reverse=True)

  for i in range(len(genres)) : dictGenres[hash(genres[i])].append(plays[i])
  for g in dictGenres : dictGenres[g].sort(reverse=True)
  for i in range(len(sTP)):
    answer.append(plays.index(dictGenres[sTP[i][0]][0]))
    if len(dictGenres[sTP[i][0]])>1: answer.append(plays.index(dictGenres[sTP[i][0]][1]))
  return answer

'''
채점 결과
정확성: 86.7
합계: 86.7 / 100.0
'''
