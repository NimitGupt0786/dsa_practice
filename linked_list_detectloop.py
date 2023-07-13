https://www.codingninjas.com/studio/problems/cycle-detection-in-a-singly-linked-list_628974
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def detectCycle(head) :
    slow=head
    fast=head

    while(fast!= None and fast.next!= None ):
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False    