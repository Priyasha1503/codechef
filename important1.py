
#https://www.codechef.com/practice/course/arrays-strings-sorting/INTARR01/problems/EQUALELE

# cook your dish here
from collections import Counter
t=int(input())
while(t>0):
    n=int(input())
    nums=list(map(int,input().split()))
    c=Counter(nums)
    maxs=0 #updatig the most freq element
    for i in c:
        if c[i]>maxs:
            maxs=c[i]
    #print("maxs",maxs)
    print(len(nums)-maxs)
    
    t-=1
