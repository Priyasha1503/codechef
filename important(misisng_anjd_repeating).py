

#https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/MISSNDREPEAT

class Solution:
    def findRepeatingAndMissing(self, arr):
        # write your code here
        '''mpp=dict()
        for i in range(0,len(arr)):
            if arr[i] not in mpp:
                mpp[arr[i]]=1
            else:
                mpp[arr[i]]+=1
        res1=-1
        res2=-1
        for i in range(1,n+1):
            if i not in mpp:
                res2=i
            else:
                if mpp[i]==2:
                    res1=i
        return [res1,res2]'''
        
        
        '''if len(arr)==2:
            if arr[0]==1:
                return [1,2]
            elif arr[0]==2:
                return [2,1]'''
            
        arr.sort()
        res=[-1,-1] #0 index for repeating and 1 index missing
        if arr[0]!=1:
            res[1]=1
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]:
                res[0]=arr[i]
            elif arr[i]-1==arr[i-1]:
                pass
            else:
                res[1]=arr[i]-1

        if res[1]==-1:
            res[1]=arr[-1]+1
        return res
                
