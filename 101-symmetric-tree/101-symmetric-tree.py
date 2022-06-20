# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)
    
    
    def isMirror(self, t1, t2):
        if not t1 and not t2: return True
        if not t1 or not t2: return False
        return t1.val == t2.val and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)
    
    
    # OR
    
    
    
    # Visits each node once: O(n) time, O(h) space
    def isSymmetric(self, root):
        # Recursively determines if two branches are mirrors of each other
        def isMirror(t1, t2):
            # Base case 1: Both branches are null
            if t1 is None and t2 is None:
                return True

            # Base case 2: One branch is null and the other is not
            if t1 is None or t2 is None:
                return False

            # Base case 3: The values of two roots are different
            if t1.val != t2.val:
                return False

            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        if root is None:
            return True
        return isMirror(root.left, root.right)