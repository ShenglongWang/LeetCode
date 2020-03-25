"""
@version:01.00.00
@Author:Shenglong
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    '''
    解题思路：
    一个二叉搜索树的前序遍历其实就是所有节点值的升序排列。
    按照此思路，先前序遍历所有节点，并将节点值存入list中。
    遍历结束后，对节点值list进行排序，然后对先序遍历中的节点值进行替换。
    '''
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        temp = []
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root)
                temp.append(root.val)
                inorder(root.right)
        inorder(root)
        temp = sorted(temp)
        for i in range(len(temp)):
            res[i].val = temp[i]