n = int(input())

for i in range(n):
    h, w, n = map(int, input().split())

    a = str(int(n/h)+1)
    b = str(int(n%h))

    if b == '0':
        b = str(h)
        a = str(int(a)-1)
    
    if len(a) == 1:
        print(b+'0'+a)
    else:
        print(b+a)    