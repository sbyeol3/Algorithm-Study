def solution(participant, completion):
  participant.sort()
  completion.sort()
  length = len(completion)

  for idx in range(length) :
    if (participant[idx] != completion[idx]) : return participant[idx]

  return participant[length]
