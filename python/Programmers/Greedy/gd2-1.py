def solution(name):
    nameArr = list(name)
    length = len(name)
    init = ['A']*length
    success = []
    cnt = 0
    idx = 0

    while(True):
        initAscii = ord(init[idx])
        nameAscii = ord(nameArr[idx])
        diff = nameAscii - initAscii

        if diff > 13 : diff = 26 - diff
        success.append(idx)
        cnt += diff
        init[idx] = nameArr[idx]
        
        if len(success) == length: break
        SearchIdx = list(filter(lambda x: x not in success and (init[x]!=nameArr[x]), range(0,length)))
        if (len(SearchIdx)==0) : break
        minIdxList = [min(abs(x-idx),abs(length+idx-x)) for x in SearchIdx]
        minIdxItem = min(minIdxList)
        minIdx = SearchIdx[minIdxList.index(minIdxItem)]
        cnt += minIdxItem
        idx = minIdx

    return cnt
print(solution("JAN"))
# 1172