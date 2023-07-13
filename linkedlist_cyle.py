https://leetcode.com/problems/linked-list-cycle-ii/
class Solution(object):
    def detectCycle(self, head):
        if (head==None or head.next==None):
            return None
        slow=head
        fast=head

        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
            if(slow == fast):
                break

        if fast==None or fast.next==None:
            return None

        fast = head

        while(fast!=slow):
            fast=fast.next
            slow=slow.next
        return slow