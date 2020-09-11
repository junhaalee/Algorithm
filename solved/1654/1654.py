import sys
input = sys.stdin.readline

k, n = map(int, input().split())

length = [int(input()) for _ in range(k)]

start, finish = 0, max(length)

while(start <= finish):

    target = (start+finish)//2

    temp = 0
    for l in length:
        temp += l//target
    
    if temp < n:
        finish = target - 1
    else:
        start = target + 1

print(finish)