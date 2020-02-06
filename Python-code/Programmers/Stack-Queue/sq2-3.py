def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    time = 0
    
    while bridge:
        time += 1
        tmp = bridge[1:]
        bridge = tmp
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights[0])
                truckTemp = truck_weights[1:]
                truck_weights = truckTemp
            else:
                bridge.append(0)

    return time

'''
채점 결과
정확성: 92.3 -> case 5 : 시간초과
합계: 92.3 / 100.0 
'''