for _ in range(int(input())):
    answer = 1

    n,m = map(int, input().split())

    for i in range(m,m-n,-1):
        answer *= i
    for i in range(n,1,-1):
        answer //= i

    print(answer)