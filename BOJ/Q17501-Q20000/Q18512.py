x, y, startX, startY = map(int,raw_input().split(' '))
if startX < startY :
    startX, startY = startY, startX
    x, y = y, x
# if (x >= y and startX > startY) or (x <= y and startX < startY) : print(-1)
# else :
distance = abs(startX-startY)
i = 0
while True :
    if (distance + i * x) % y == 0 : break
    else : i += 1
print(startX + i * x)