from queue import PriorityQueue
q = PriorityQueue()
q.put((-10,10))			# -ve will decide the priority and +ve will be the number
q.put((-40,40))
q.put((-20,20))
while not q.empty():
    priority, element = q.get()
    print(element)