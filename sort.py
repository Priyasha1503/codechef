
#https://www.codechef.com/practice/course/arrays/ARRAYS/problems/RATINGINPRAC?tab=statement

t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    # Your code goes here
    flag=0
    for i in range(0,n-1):
        if d[i]<=d[i+1]:
            flag+=1
            pass
        else:
            print("No")
            break
    if flag==n-1:
        print("Yes")
    t -= 1
