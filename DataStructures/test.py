from LinkedList import LinkedList
from BinaryTree import BinaryTree
from BinaryTreeNode import Node

# Linked List test
'''lista = LinkedList()
lista.append_value(4)
lista.append_value(8)
lista.append_value(16)
print(lista)'''

# Binary Tree test
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print(tree.print_tree(tree, "preorder"))
print(tree.print_tree(tree, "inorder"))

