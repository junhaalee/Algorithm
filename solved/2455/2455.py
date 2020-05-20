import sys
input = sys.stdin.readline

ans = [0]*5

for ind in range(1,5):
    o,i = map(int, input().split())
    ans[ind] = ans[ind-1]-o+i
print(max(ans))