def solution(stones, k):

    left = 1
    right = max(stones)+1

    while(left+1 < right):

        mid = (left+right)//2

        if check(stones, k, mid):
            left = mid
        else:
            right = mid

    return left


def check(stones, k, cnt):
    count = 0

    for s in stones:

        if s < cnt:
            count += 1
        else:
            count = 0

        if count >= k:
            return False

    return True