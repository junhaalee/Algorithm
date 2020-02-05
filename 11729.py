n = int(input())

def hanoi(disk, start, mid, end):
    if disk == 1:
        print(start, end)
    else:
        hanoi(disk-1, start, end, mid)
        print(start, end)
        hanoi(disk-1, mid, start, end)

print((2**n) -1)
hanoi(n, 1,2,3)