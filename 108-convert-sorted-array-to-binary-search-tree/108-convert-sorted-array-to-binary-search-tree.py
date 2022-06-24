# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
recursive approach
have to create each node
[]
'''


class Solution:
    def helper(self, arr,l,r):
        if l > r: return None
        mid = (l+r)//2
        currNode = TreeNode(arr[mid])
        currNode.left = self.helper(arr,l, mid-1)
        currNode.right = self.helper(arr,mid+1,r)
        return currNode
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums,0,len(nums)-1)
    
        