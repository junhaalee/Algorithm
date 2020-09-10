import sys
input = sys.stdin.readline

n,m = map(int, input().split())
trees = list(map(int,input().split()))

def cut(trees, h):
    return sum([x-h if x>=h else 0 for x in trees])


def sol(m,trees):

    left = 1
    right = max(trees)

    while(left<=right):

        mid = (left+right)//2
        
        length = cut(trees,mid)

        if length >= m:
            left = mid+1
        else:
            right = mid-1

    print(right)

sol(m,trees)