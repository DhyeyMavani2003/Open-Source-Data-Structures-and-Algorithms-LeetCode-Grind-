# O(n) time | O(n) space
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        summ = {}
        ans = []

        self.dfs(root, summ)
        maxVal = max(summ.values())
        for key, val in summ.items():
            if val == maxVal:
                ans.append(key)
        return ans
        
    
    def dfs(self, root, summ):
        if root is None:
            return 
        self.dfs(root.left, summ)
        self.dfs(root.right, summ)

        if root.left:
            root.val += root.left.val
        if root.right:
            root.val += root.right.val
        if root.val not in summ:
            summ[root.val] =1
        else:
            summ[root.val]+=1