def solution(phone_book):
  answer = True
  for i in range(len(phone_book)) :
    for j in range(len(phone_book)):
      if(i!=j and phone_book[i]==phone_book[j][0:len(phone_book[i])]): return False

  return answer

'''
채점결과
정확성: 84.6
효율성: 15.4
합계: 100.0 / 100.0
'''