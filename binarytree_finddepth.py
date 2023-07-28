https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def levelwise(root,q,count):

    while len(q) > 0:
        a = q.popleft()

        if a==None:
            count[0] += 1
            if len(q)>0:
                a=q.popleft()
            else:
                break

        if a.left!=None:
            q.append(a.left)

        if a.right != None:
            q.append(a.right)

        if a.left !=None or a.right != None:
            q.append(None)

        if len(q) >0:
            levelwise(q[0], q,count)

    return count[0]


root = Node(30)
root.left=Node(15)
root.right=Node(40)
# root.left.left=Node(10)
# root.left.right=Node(20)
q=deque()
q.append(root)
count=[1]
print(levelwise(root,q,count))