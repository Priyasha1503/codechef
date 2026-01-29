
#https://www.codechef.com/problems/STICKS


# cook your dish here
from collections import Counter
t=int(input())
while t>0:
    n=int(input())
    stick_lengths=list(map(int,input().split()))
    possible_rectangle=[]
    c=Counter(stick_lengths)
    for i in c:
        if c[i]>1:
            #for x in range(0,c[i]//2):
                #possible_rectangle.append(i)
        
    possible_rectangle.sort(reverse=True)
    if len(possible_rectangle)>1:
        print(possible_rectangle[0]*possible_rectangle[1])
    else:
        print(-1)
    t-=1
