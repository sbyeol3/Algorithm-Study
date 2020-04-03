def solution(phone_book):
  answer = True
  for i in range(len(phone_book)-1) :
    for j in range(i+1,len(phone_book)):
      if(phone_book[i]==phone_book[j][0:len(phone_book[i])]): return False

  return answer

'''
채점 결과
정확성: 69.2
효율성: 15.4
합계: 84.6 / 100.0
'''