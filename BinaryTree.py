class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def inorder_traversal(self, node):
        res = []
        if node:
            res = self.inorder_traversal(node.left)
            res.append(node.data)
            res = res + self.inorder_traversal(node.right)
        return res

    def pre_order_traversal(self, node):
        res = []
        if node:
            res.append(node.data)
            res += self.pre_order_traversal(node.left)
            res += self.pre_order_traversal(node.right)
        return res

    def post_order_traversal(self, node):
        res = []
        if node:
            res = self.post_order_traversal(node.left)
            res += self.post_order_traversal(node.right)
            res.append(node.data)

        return res


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(1)
root.insert(19)
root.insert(18)
root.insert(13)
root.print_tree()
print("In Order Traversal ==>", root.inorder_traversal(root))
print("Pre Order Traversal ==>", root.pre_order_traversal(root))
print("Post Order Traversal ==>", root.post_order_traversal(root))
