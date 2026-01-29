
#https://www.codechef.com/problems/LINCHESS


# cook your dish here
t=int(input())
while t>0:
    n,k=input().split()
    pawns=list(map(int,input().split()))
    n,k=int(n),int(k)
    min_moves=float('inf')
    player=-1
    for i in range(0,len(pawns)):
        if k%pawns[i]==0 and pawns[i]<k:
            move=(k//pawns[i])-1
            if min_moves>move:
                min_moves=move
                player=pawns[i]
    if min_moves!=float('inf'):
        print(player)
    else:
        print(-1)
    t-=1
    
