import sys
input = sys.stdin.readline

n = int(input())

def primes(n):
    
    result = [False,False] + [True]*(n-1)
    
    for i in range(2, int(n**0.5+1)):
        if result[i]:
            result[2*i::i] = [False]*((n-i)//i)
    
    return [x for x in range(n+1) if result[x]]


nums = prime_list(n+1)

answer = 0
left, right = 0,0

while right < len(nums) and left <= right:

    s = sum(nums[left:right+1]) 

    if s < n:
        right += 1

    elif s == n:
        answer += 1
        right += 1
    
    else:
        left += 1

print(answer)