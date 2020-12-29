def solution(n):

    one = bin(n)[2:].count('1')

    n += 1

    while True:
        
        temp = bin(n)[2:].count('1')

        if temp == one:
            break
        else:
            n+= 1

    return n