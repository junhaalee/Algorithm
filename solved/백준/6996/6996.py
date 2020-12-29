import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a,b = input().split()
    print(a+' & '+b+' are anagrams.') if sorted(list(a)) == sorted(list(b)) else  print(a+' & '+b+' are NOT anagrams.')