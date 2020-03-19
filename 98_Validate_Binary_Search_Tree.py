"""
@version:01.00.00
@Author:Shenglong
"""


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        # solution1:
        # 递归判断每个左右子树值，每次给左子树传入当前上一层节点low，以及当前节点为high
        # 每次给右子树传入当前节点值为low，上层节点high。
        '''
        def compara(root, low = float('-inf'), high = float('inf')):
            if not root:
                return True
            if root.val <= low or root.val >= high:
                return False
            if not compara(root.left, low, root.val):
                return False
            if not compara(root.right, root.val, high):
                return False
            return True
        '''

        # solutions2:
        # 使用栈将每个节点以及上下限入栈，然后依次判断每个节点的值是否满足上下限

        '''
        def compara(root):
            if not root:
                return True
            stack = [(root,float('-inf'),float('inf'))]
            while stack:
                root, low ,high = stack.pop()
                if not root:
                    continue
                if root.val <= low or root.val >= high:
                    return False
                stack.append((root.left,low,root.val))
                stack.append((root.right,root.val,high))


            return True
        '''

        # solution3
        # 使用二叉树的顺序遍历，即左中右，判断出栈节点的值一定要比上一次出栈节点的值小

        '''
        def compara(root):
            stack, lowest = [], float('-inf')

            while stack or root:
                #将左子树入栈
                while root:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                if root.val <= lowest:
                    return False
                lowest = root.val
                root = root.right
            return True
        '''

        # solution4
        # solution1 的简写版
        def compara(root, low=None, high=None):
            if not root:
                return True
            if low and root.val <= low.val:
                return False
            if high and root.val >= high.val:
                return False
            return compara(root.left, low, root) and compara(root.right, root, high)

        return compara(root)
