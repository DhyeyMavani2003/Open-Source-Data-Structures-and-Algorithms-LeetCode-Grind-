# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Compute the tree's height via recursion
    def height(self, root: TreeNode) -> int:
        # An empty tree has height -1
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))
    
    def isBalanced(self, root: TreeNode) -> bool:
        # An empty tree satisfies the definition of a balanced tree
        if not root:
            return True

        # Check if subtrees have height within 1. If they do, check if the
        # subtrees are balanced
        return abs(self.height(root.left) - self.height(root.right)) < 2 \
            and self.isBalanced(root.left) \
            and self.isBalanced(root.right)
        
        
        
    # OR
    
    
    
    
    # Recursively determine if a binary tree is balanced
    # Visits each node once: O(n) time, O(h) space
    def isBalanced(self, root):
        # Find the height of a tree given its root
        # return -1 if unbalanced
        def height(root):
            # Base case
            if root is None:
                return 0

            left_height  = height(root.left)
            right_height = height(root.right)

            # If tree is unbalanced, return -1
            if left_height == -1 or right_height == -1 or \
                abs(left_height - right_height) > 1:
                return -1

            # Otherwise, return height of tree
            return 1 + max(left_height, right_height)

        return height(root) != -1