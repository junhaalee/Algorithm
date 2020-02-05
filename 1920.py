x = int(input())
x_list = sorted(list(map(int, input().split())))

m = int(input())
m_list = list(map(int, input().split()))

def find(n, n_list):

    while(len(n_list) != 1):

        if n < n_list[len(n_list)//2]:
            n_list = n_list[:len(n_list)//2]

        elif n > n_list[len(n_list)//2]:
            n_list = n_list[len(n_list)//2:]
            
        elif n == n_list[len(n_list)//2]:
            print(1)
            break

    if len(n_list) == 1:
        if n_list[0] != n : print(0)
        else: print(1)

for i in range(len(m_list)):
    find(m_list[i],x_list)

