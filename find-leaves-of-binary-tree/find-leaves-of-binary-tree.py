from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def __init__(self):
        self.solution = []
    
    def _getHeight(self, root: TreeNode) -> int:
        # return -1 for null nodes
        if not root:
            return -1
        
        # first calculate the height of the left and right children
        leftHeight = self._getHeight(root.left)
        rightHeight = self._getHeight(root.right)
        
        currHeight = max(leftHeight, rightHeight) + 1
        
        if len(self.solution) == currHeight:
            self.solution.append([])
        
        self.solution[currHeight].append(root.val)
        
        return currHeight
    
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.solution = []
        
        self._getHeight(root)
        
        return self.solution
