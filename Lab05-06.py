class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, data):
        pNew = BSTNode(data)
        if self.is_empty():
            self.root = pNew
        else:
            start = self.root
            while start:
                if data < start.data:
                    if start.left is None:
                        start.left = pNew
                        break
                    else:
                        start = start.left
                else:
                    if start.right is None:
                        start.right = pNew
                        break
                    else:
                        start = start.right

    def delete(self, data):
        def deleteNode(root, data):
            if root is None:
                return None
            if data < root.data:
                root.left = deleteNode(root.left, data)
            elif data > root.data:
                root.right  = deleteNode(root.right, data)
            else:
                if root.right is None:
                    return root.left
                elif root.left is None:
                    return root.right
                else:
                    maxNode = self.findMax(root.left)
                    root.data = maxNode
                    root.left = deleteNode(root.left, maxNode)
            return root
        self.root = deleteNode(self.root, data)

    def preorder(self, root):
        if root != None:
            print("->", root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root != None:
            self.inorder(root.left)
            print("->", root.data, end=" ")
            self.inorder(root.right)

    def postorder(self, root):
        if root != None:
            self.postorder(root.left)
            self.postorder(root.right)
            print("->", root.data, end=" ")

    def traverse(self):
        if self.is_empty():
            print("Empty tree")
        else:
            print("Preorder:", end="")
            self.preorder(self.root)
            print("\nInorder:", end="")
            self.inorder(self.root)
            print("\nPostorder:", end="")
            self.postorder(self.root)

    def findMin(self, start=None):
        if start is None:
            start = self.root
        while start.left:
            start = start.left
        return start.data

    def findMax(self, start=None):
        if start is None:
            start = self.root
        while start.right:
            start = start.right
        return start.data

def test():
    myBST = BST()
    myBST.insert(14)
    myBST.insert(23)
    myBST.insert(7)
    myBST.insert(10)
    myBST.insert(33)
    # myBST.traverse()
    myBST.delete(14)
    myBST.traverse()
    print("\nMin:", myBST.findMin())
    print("Max:", myBST.findMax())
test()
