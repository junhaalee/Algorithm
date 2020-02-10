n = int(input())

location = [list(map(int, input().split())) for _ in range(n)]

location = [[0, 0], [10, 10], [0, 10], [10, 0]]

def dist(a,b):
    return (a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1])

