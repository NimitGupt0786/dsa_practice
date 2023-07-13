##implementing queue using collection module
from collections import deque
Q=deque()
Q.append(10)
Q.append(20)
Q.append(30)

print(Q,"Q")
print(Q[0],"Q[0]")
print("Popped element is",Q.popleft())
print("Popped element is",Q.popleft())

print(Q)

print(len(Q))

if len(Q)==0:
    print(True)
else:
    print(False)
