def solution(bridge_length, weight, truck_weights):
  bridge = [0]*len(truck_weights)
  first = 0 # 가장 앞에 있는 트럭
  last = 0 # 가장 뒤에 있는 트럭
  out = -1 

  time = 1
  bridge[0] += 1 
  while out < len(truck_weights) :
    if sum(truck_weights[first:last]) + truck_weights[last+1] <= weight: last += 1

    time += 1 # time 2
    for i in range(first, last+1) : #  0
      bridge[i]+=1 # 2
      if bridge[i] == (bridge_length + 1) :
        out = i # 0
        bridge[out] = -1
        first = out + 1 # 1
    if(last==len(truck_weights)-1) :
      while(bridge[last]<bridge_length+1) :
        bridge[last] += 1
        time += 1
      break
  
  return time+1

bridge_length = 2
weight = 10
truck_weights =[7,4,5,6]
print(solution(bridge_length,weight,truck_weights))