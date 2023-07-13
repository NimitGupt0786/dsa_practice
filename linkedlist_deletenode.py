https://leetcode.com/problems/delete-node-in-a-linked-list/
class Solution(object):
    def deleteNode(self, node):
        a=node.next
        b=node.next.next
        node.val=a.val
        node.next=b
        