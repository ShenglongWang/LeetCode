"""
@version:01.00.00
@Author:Shenglong
"""


class Solution:

    # solution1:
    # 使用递归，按照左中右的顺序遍历

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        return self.inorder(root, res)

    def inorder(self, root: TreeNode, res=[]):
        if root != None:
            if root.left != None:
                self.inorder(root.left, res)
            res.append(root.val)
            if root.right != None:
                self.inorder(root.right, res)
        return res

    # solution2:
    # 使用栈遍历二叉树，如果左子树不为空，一直遍历左子树
    '''
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        curr = root
        while(curr != None or stack != []):
            while(curr != None):
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
    '''