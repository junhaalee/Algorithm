import sys
input = sys.stdin.readline

n = int(input())
ns = sorted(list(map(int, input().split())))
m = int(input())
ms = list(map(int, input().split()))

def search(x,s,e,arr):

    if s > e:
        return False

    mid = (s+e)//2

    if arr[mid] == x:
        return True
    elif arr[mid] > x:
        e = mid - 1
    else:
        s = mid + 1
    
    return search(x,s,e,arr)
    
for mm in ms:
    if search(mm,0,n-1,ns):
        print(1)
    else:
        print(0)

