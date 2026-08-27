# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        result="z"*26
        def solve(root,path):
            nonlocal result
            if not root:
                return 
            path.append(chr(root.val+97))
            if not root.left and not root.right:
                val="".join(path)[::-1]
                if val<result:
                    result=val
                path.pop()
                return 
            solve(root.left,path)
            solve(root.right,path)
            path.pop()
        solve(root,[])
        return result

