
#https://www.codechef.com/problems/HAPPYSTR

#BRUTEFORCE 
'''def func(s,sets):
    for i in range(0,len(s)):
        for j in range(i,len(s)):
            if(j-i+1)>2:
                subs=s[i:j+1]
                flag=0
                for x in subs:
                    if x in sets:
                        pass
                    else:
                        flag=1
                if flag==0:
                    return "Happy"
    return "Sad"'''
    #better appraoch
'''def func(s,sets):
    for i in range(0,len(s)-3+1):
        subs=s[i:i+3]
        flag=0
        for x in subs:
            if x in sets:
                pass
            else:
                flag=1
                break
        if flag==0:
            return "happy"
    return "Sad"'''
def func(s,sets): #chatgpt suggestion - the simplest one
    vowels = {'a', 'e', 'i', 'o', 'u'}
    s = s.lower()

    for i in range(len(s) - 2):
        if s[i] in vowels and s[i+1] in vowels and s[i+2] in vowels:
            return "HAPPY"
    return "SAD"
            

t = int(input())

while t > 0:
    s = input()
    # Your code goes here
    sets={'a','e','i','o','u'}
    print(func(s,sets))
    t-=1
    
    
                        
            
