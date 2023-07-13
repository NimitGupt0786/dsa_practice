https://leetcode.com/problems/implement-queue-using-stacks/
from collections import deque
class MyQueue(object):

    def __init__(self):
        self.q=deque()      

    def push(self, x):  
        self.q.append(x)

    def pop(self):
        return self.q.popleft()
        

    def peek(self):
        return self.q[0]
        

    def empty(self):
        return len(self.q)==0