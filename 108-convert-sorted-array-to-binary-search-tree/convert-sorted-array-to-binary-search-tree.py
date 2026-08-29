# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        memo={}
        def solve(l,h):
            mid=(l+h)//2
            if l>h:
                return None
            node=TreeNode(val=nums[mid])
            node.left=solve(l,mid-1)
            node.right=solve(mid+1,h)
            return node
        return solve(0,len(nums)-1)