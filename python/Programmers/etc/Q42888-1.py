# -*- coding: utf-8 -*- 
def solution(record):
    chattingRoom = dict()
    cnt = 0
    for i,v in enumerate(record):
        r = v.split(' ')
        if r[0] == 'Enter' :
            cnt += 1
            if r[1] in chattingRoom :
                if chattingRoom[r[1]][0] != r[2] : 
                    chattingRoom[r[1]][0] = r[2]
                    chattingRoom[r[1]].append(i)
            else :
                chattingRoom[r[1]] = [r[2],i]
        elif r[0] == 'Leave' :
            cnt += 1
            chattingRoom[r[1]].append(i)
        else :
            chattingRoom[r[1]][0] = r[2]

    answer = ['']*(cnt)
    for v in chattingRoom.values():
        nickname = v[0]
        for i in range(1,len(v)): # ryan 0 3
            if i % 2 == 1 :
                answer[v[i]] = nickname+ '님이 들어왔습니다.'
            else : answer[v[i]] = nickname+ '님이 나갔습니다.'
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))