def solution(N):
    if N == 1:
        return 4
    elif N == 2:
        return 6
    else:
        return solution(N-1)+solution(N-2)
