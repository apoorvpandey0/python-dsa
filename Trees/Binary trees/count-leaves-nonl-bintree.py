"""
    Count leaves and non leaves in a Binary Tree
    https://practice.geeksforgeeks.org/problems/count-leaves-in-binary-tree/1
    https://practice.geeksforgeeks.org/problems/count-non-leaf-nodes-in-tree/1/
"""

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
def countLeaves(node):
    if not node: return 0

    # If any child exsists simply go through the child subtree
    if node.left or node.right: return countLeaves(node.left) + countLeaves(node.right)

    # If no child exists, then it is a leaf node
    # And we can return 1
    else: return 1

def countNonLeafNodes(self, root):
    def count(node):
        if not node: return 0

        # If any child exsists simply go through the child subtree and add one
        if node.left or node.right: return count(node.left) + count(node.right) +1

        # If no child exists, then it is a leaf node
        # And we can return 0
        else: return 0
    return count(root)