
#https://www.codechef.com/practice/course/stacks-and-queues/STAQUEF/problems/PPMUH01

class QueueUsingStacks:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    
    def pushElement(self, x):
        self.stack1.append(x)
        
    def popElement(self):
        if self.stack2!=[]:
            return self.stack2.pop(-1)
        else:
            while self.stack1:
                x=self.stack1.pop()
                self.stack2.append(x)
            return self.stack2.pop()
        
    def peekElement(self):
        if self.stack2!=[]:
            return self.stack2[-1]
        else:
            while self.stack1:
                x=self.stack1.pop()
                self.stack2.append(x)
            return self.stack2[-1]
        
    def isEmptyResult(self):
        if  self.stack1==[] and self.stack2==[]:
            return True
            
        else:
            return False
