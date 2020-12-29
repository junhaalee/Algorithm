n = int(input())

count = 0
num = 1

while(num != n):

    if num*3 <= n:
        num *= 3
    elif num*2 <= n:
        num *= 2
    elif num+1 <= n:
        num += 1
    
    count+=1

print(count)