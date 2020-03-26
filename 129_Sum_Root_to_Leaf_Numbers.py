"""
@version:01.00.00
@Author:Shenglong
"""


class Solution1:

    '''
    解题思路：
    每次递归一层，传入的num值为上一层num值乘以10加当前节点的值
    直到叶子节点时，将num值存入res数组，当遍历完所有叶子节点。将res数组中的值求和即可。
    '''
    def sumNumbers(self, root: TreeNode) -> int:
        res = []

        def inorder(root, num):
            if not root:
                return 0
            if not root.left and not root.right:
                res.append(num * 10 + root.val)
            if root.left:
                inorder(root.left, num * 10 + root.val)
            if root.right:
                inorder(root.right, num * 10 + root.val)

        inorder(root, 0)

        return sum(res)


    '''
    Solution2：
    递归求和
    '''

    def sumNumbers(self, root: TreeNode) -> int:
        res = []

        def inorder(root, num):
            if not root:
                return 0
            num = num * 10 + root.val
            if not root.left and not root.right:
                return num
            return inorder(root.left, num) + inorder(root.right, num)

        return inorder(root, 0)