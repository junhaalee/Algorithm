n = int(input())

ind = 1
count = 0

while(True):
    if '666' in str(ind): 
        count += 1
    if count == n:
        print(ind)
        break
    ind += 1
