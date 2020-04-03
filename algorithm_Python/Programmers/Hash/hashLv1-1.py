def solution(participant, completion):
  nonCompletion = dict()
  for player in set(participant): nonCompletion[player] = 0

  for player in participant :
    if (player not in completion) : nonCompletion[player] += 1
    else : completion.remove(player)

  answer = ''
  for player in nonCompletion :
    answer += player * nonCompletion[player]
  
  return answer