
def sol():
    
    N = int(input())
    
    ans = 1
    fin = 1
    
    while(N > fin):
        
        fin += (ans * 6)
        
        ans += 1
    
    print(ans)