
#https://www.codechef.com/problems/SIMDISH

# cook your dish here
t=int(input())
while t>0:
    d1=input().split()
    d2=input().split()
    dishes=set(d2)
    cnt=0
    for i in d1:
        if i in dishes:
            cnt+=1
    if cnt>=2:
        print("similar")
    else:
        print("dissimilar")
    t-=1
    
