https://leetcode.com/problems/remove-nth-node-from-end-of-list/
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head==None:
            return None
        if head.next == None:
            return None
        a=head
        c=head
        d=head.next
        length=0

        while(head!=None):
            head=head.next
            length += 1

        b=length-n

        if b==0:
            return d

        if b>1:
            for i in range(b-1):
                a=a.next
        a.next=a.next.next
        return c       