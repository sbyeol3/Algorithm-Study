#!/usr/bin/python3.7
#-*- coding: utf-8 -*-
import heapq
def solution(scoville, K):
    mixtree = []
    mix = 0

    if min(scoville) >= K : return 0
    for s in scoville : 
        heapq.heappush(mixtree, s)
    
    while(len(mixtree)>1):
        min1 = heapq.heappop(mixtree)
        min2 = heapq.heappop(mixtree)
        newScoville = min1 + min2 * 2
        mix = mix + 1
        heapq.heappush(mixtree, newScoville)
        if mixtree[0] >= K : return mix

    return -1

a = [8,9,10,11]
scoville = [1, 2, 3, 9, 10, 12]
k = 100
print(solution(scoville,k))

"""
ä�� ���
��Ȯ��: 52.4
ȿ����: 23.8
�հ�: 76.2 / 100.0

��Ȯ�� �׽�Ʈ :  1, 3, 8, 14, 16 runtime error
"""