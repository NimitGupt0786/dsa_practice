https://leetcode.com/problems/implement-stack-using-queues/
class MyStack(object):

    def __init__(self):
        self.stack=[]

    def push(self, x):
        lists=self.stack
        lists.append(x)
    
    def empty(self):   
        lists=self.stack
        if(len(lists)==0):
            return True
        else:
            return False

    def pop(self):
        lists=self.stack
        return lists.pop()
        

    def top(self):
        lists=self.stack
        return lists[-1]
        