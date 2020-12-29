from collections import Counter
import sys
input = sys.stdin.readline

n = list(map(int, list(input().strip())))
sn = [6,9]
el = [1,2,3,4,5,7,8,0]

count = dict(Counter(n))

sn_count, el_count = 0,0

for s in sn:
    sn_count = sn_count+count[s] if s in count.keys() else sn_count

for e in el:
    el_count = max([el_count,count[e]]) if e in count.keys() else el_count

print(max([(sn_count+1)//2,el_count]))