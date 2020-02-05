n = int(input())

scv = list(map(int, input().split()))

def sol(scv,count):

    if sum(scv) == 0:
        return count
    
    else:
        min([
            sum([scv[0]-9, scv[1]-3, scv[2]-1]),
            sum([scv[0]-9, scv[1]-1, scv[2]-3]),
            sum([scv[0]-3, scv[1]-9, scv[2]-1]),
            sum([scv[0]-3, scv[1]-1, scv[2]-9]),
            sum([scv[0]-1, scv[1]-3, scv[2]-9]),
            sum([scv[0]-1, scv[1]-9, scv[2]-3]),
        ])


    return count

