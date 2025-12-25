
#https://www.codechef.com/problems/LAPIN


t=int(input())
while t>0:
    s=input()
    mid=(len(s)-1)//2
    if len(s)%2==0: #even
        s1=s[0:mid+1]
        s2=s[mid+1:]
    else:#if sting length is odd
        s1=s[0:mid]
        s2=s[mid+1:]
    l1=list(s1)
    l2=list(s2)
    l1.sort()
    l2.sort()
    #print(l1,l2)
    flag=0
    for i in range(0,len(l1)):
        if l1[i]==l2[i]:
            pass
        else:
            flag=1
    if flag==0:
        print("YES")
    else:
        print("NO")
            
    t-=1
