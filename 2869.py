A,B,V = map(int, input().split())

temp = 0
day = 0

while(True):
    temp += A
    if temp > V:
        break
    else:
        temp -= B
    day += 1
print(day)