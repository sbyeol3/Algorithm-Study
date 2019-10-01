 """input : 길이가 4이상 20이하인 문자열
 output : 뒤 4자리 제외 모두 *로 표시한 문자열"""

def solution(phone_number):
  phone_number = list(phone_number)
  length = len(phone_number)
  answer=''
  for i in range(0,length-4):
    phone_number[i]='*'
  for i in phone_number:
    answer+=i
  return answer
