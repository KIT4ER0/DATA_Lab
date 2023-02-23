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
        if self.root is None:
            self.root = pNew
        else:
            current_node = self.root
            while current_node:
                if data < current_node.data:
                    if current_node.left is None:
                        current_node.left = pNew
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = pNew
                        break
                    else:
                        current_node = current_node.right

    def delete(self, data):
        def deleteNode(root, data):
            if root is None:
                return None
            if data < root.data:
                return deleteNode(root.left, data)
            elif data > root.data:
                return deleteNode(root.right, data)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:
                    minNode = self.findMin(root.right)
                    root.data = minNode
                    root.right = deleteNode(root.right, minNode)
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
        print("Preorder: ", end="")
        self.preorder(self.root)
        print("\nInorder: ", end="")
        self.inorder(self.root)
        print("\nPostorder: ", end="")
        self.postorder(self.root)

    def findMin(self, current_node=None):
        if current_node is None:
            current_node = self.root
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.data

    def findMax(self, current_node=None):
        if current_node is None:
            current_node = self.root
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.data

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
