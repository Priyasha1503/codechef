
#https://www.codechef.com/practice/course/arrays/ARRAYS/problems/DISCOUNTT

class Solution:
    def check_coupon(self, n, x, y,costs):
        # write your code here
        
        sums=sum(costs)
        disc=0
        for i in range(0,len(costs)):
            if costs[i]<=y:
                pass
            else:
                disc+=(costs[i]-y)
        if x+disc<sums:
                return "coupon"
        else:
                return "no coupon"
