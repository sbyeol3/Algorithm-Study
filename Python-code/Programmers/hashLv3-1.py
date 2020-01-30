from collections import defaultdict
def solution(genres, plays):
  length = len(genres)
  answer = []
  dictGP = dict()
  dictGenres = defaultdict(list)

  for g, p in zip(genres, plays):
    if hash(g) in dictGP : dictGP[hash(g)] += p
    else : dictGP[hash(g)] = p

  for i in range(length):
    hashG = hash(genres[i])
    if len(dictGenres[hashG])==2 :
      if plays[i] > plays[dictGenres[hashG][0]] :
        tmp = dictGenres[hashG][0]
        dictGenres[hashG][0] = i
        dictGenres[hashG][1] = tmp
      elif plays[i] > plays[dictGenres[hashG][1]] : dictGenres[hashG][1] = i
    elif len(dictGenres[hashG])==1 : 
      if plays[i] > plays[dictGenres[hashG][0]] :
        tmp = dictGenres[hashG][0]
        dictGenres[hashG][0] = i
        dictGenres[hashG].append(tmp)
      else : dictGenres[hashG].append(i)
    else : 
      dictGenres[hashG].append(i)

  sDictGP = sorted(dictGP.items(), key=lambda x: x[1], reverse=True)
  for i in sDictGP:
    answer.append(dictGenres[i[0]][0])
    answer.append(dictGenres[i[0]][1])
  return answer

'''
테스트 1 〉	실패 (런타임 에러)
테스트 2 〉	실패 (런타임 에러)
테스트 3 〉	통과 (0.05ms, 10.7MB)
테스트 4 〉	실패 (런타임 에러)
테스트 5 〉	통과 (0.10ms, 10.8MB)
테스트 6 〉	통과 (0.10ms, 10.9MB)
테스트 7 〉	통과 (0.08ms, 10.7MB)
테스트 8 〉	실패 (런타임 에러)
테스트 9 〉	실패 (런타임 에러)
테스트 10 〉	통과 (0.12ms, 10.7MB)
테스트 11 〉	실패 (런타임 에러)
테스트 12 〉	실패 (런타임 에러)
테스트 13 〉	통과 (0.11ms, 10.7MB)
테스트 14 〉	통과 (0.11ms, 10.8MB)
테스트 15 〉	통과 (0.05ms, 10.7MB)

채점 결과
정확성: 53.3
합계: 53.3 / 100.0
'''