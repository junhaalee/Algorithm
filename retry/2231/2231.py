n = int(input())

i = 1
while(True):
    
    if i > n:
        print(0)
        break
    
    if i+sum(map(int, list(str(i)))) == n:
        print(i)
        break
    i += 1
