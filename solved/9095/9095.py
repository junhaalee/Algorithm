import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    ans = [0]

    count = 0

    while(True):
        
        if min(ans) >= n:
            count += ans.count(n)
            break
        
        temp = []
        i = 0
        while(True):

            if i == len(ans):
                break

            if ans[i] < n:
                temp.append(ans[i]+1)
                temp.append(ans[i]+2)
                temp.append(ans[i]+3)
                i += 1
            elif ans[i] == n:
                count += 1
                ans.remove(ans[i])
            else:
                i += 1
        ans = temp
        
    print(count)
