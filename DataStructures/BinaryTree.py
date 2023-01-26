from BinaryTreeNode import Node


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, tree, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "Preorder: ")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "Inorder: ")
        else:
            return 'Traversal type ' + str(traversal_type) + 'not supported'

    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value)+"-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value)+"-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def append_node(self, value):
        pass

