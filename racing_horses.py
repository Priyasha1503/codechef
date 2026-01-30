

#https://www.codechef.com/problems/HORSES

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    # your code goes here
    mins=float('inf')
    s.sort()
    for i in range(1,len(s)):
        mins=min(abs(s[i]-s[i-1]),mins)
    print(mins)
    t-=1
