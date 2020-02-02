def solution(bridge_length, weight, truck_weights):
  if len(truck_weights)==1 : return bridge_length+1
  bridge = [0]*len(truck_weights)
  first = 0 
  last = 0 
  out = -1 
  time = 1
  bridge[0] += 1 

  while out < len(truck_weights) :
    if sum(truck_weights[first:last+1]) + truck_weights[last+1] <= weight: last += 1
    for i in range(first, last+1) : 
      bridge[i]+=1 # 2
      if bridge[i] == (bridge_length + 1) :
        out = i # 0
        bridge[out] = -1
        first = out + 1 # 1
      if i==first : time += 1
    if(last==len(truck_weights)-1) :
      while(bridge[last]<bridge_length+1) :
        bridge[last] += 1
        time += 1
      break
  
  return time

bridge_length = 2
weight = 10
truck_weights =[7,4,5,6]
print(solution(bridge_length,weight,truck_weights))

'''
채점 결과
정확성: 23.1
합계: 23.1 / 100.0
'''