"""
@version:01.00.00
@Author:Shenglong
"""


class Solution:

    '''
    Solution1:
    解题思路:

    '''
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        def inorder(root):
            if not root:
                return None
            if root.left:
                temp = root.left
                while (temp.right):
                    temp = temp.right
                temp.right = root.right
                root.right = root.left
                root.left = None
            if root.right:
                inorder(root.right)

        inorder(root)

    '''
    Solution2:
    
    '''

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while (root):
            if root.left:
                cur = root.left
                while (cur.right):
                    cur = cur.right
                cur.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
