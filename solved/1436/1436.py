n = int(input())

ans = []

i = 1
while(True):

    if '666' in str(i):
        ans.append(i)
    
    if len(ans) == n:
        print(i)
        break
    
    i += 1