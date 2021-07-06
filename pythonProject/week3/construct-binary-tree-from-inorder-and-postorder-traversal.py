# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        ans = self.get_root(inorder, postorder)
        return ans

    def get_root(self, inorder, postorder):
        if len(postorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                break
        root.left = self.get_root(inorder[:i], postorder[:i])
        root.right = self.get_root(inorder[i + 1:], postorder[i: -1])
        return root