



def solution():
    
    f_cost, cost, pro = list(map(int, input().split()))
    
    total_cost = f_cost
    total_pro = 0
    
    if int(cost) > int(pro):
        idx = -1
    else:
        idx = 1
        
        while(pro < cost):
            
            total_cost += int(cost)
            total_pro += int(pro)
            
            idx += 1
    print(idx)
        
    return idx