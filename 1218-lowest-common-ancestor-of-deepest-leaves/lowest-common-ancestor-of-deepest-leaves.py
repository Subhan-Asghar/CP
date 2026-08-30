# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root :
            return root
        def solve(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            left=solve(root.left)
            right=solve(root.right)
            return max(left,right)+1
        depth=solve(root)
        print(depth)
        def lcs(root,d):
            if not root:
                return None
            if not root.left and not root.right and d==depth-1:
                return root
            left=lcs(root.left,d+1)
            right=lcs(root.right,d+1)
            if left and right:
                return root
            return left if left else right 
        return lcs(root,0)