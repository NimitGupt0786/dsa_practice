class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def treeinput(root):
    val=int(input("root: "))

    if val == -1:
        return None

    root = Node(val)

    print("Enter the left child of root",root.data)
    root.left=treeinput(root.left)
    print("Enter the right child of root",root.data)
    root.right=treeinput(root.right)

    return root

def print_level_wise(root):
    if root == None:
        return

    if root.left != None:
        print("L:",root.left.data,end=", ")

    if root.right != None:
        print("R: ",root.right.data,end="")

    print()

    print_level_wise(root.left)
    print_level_wise(root.right)

rootnode =None
rootnode = treeinput(rootnode)
print_level_wise(rootnode)