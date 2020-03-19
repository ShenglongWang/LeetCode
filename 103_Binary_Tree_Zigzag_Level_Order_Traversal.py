"""
@version:01.00.00
@Author:Shenglong
"""


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        # 解法与102 题一样，只不过在将一层的值加入结果数组时，判断是不是反向加入即可。
        res = []
        if not root:
            return res

        from collections import deque

        stack, stack2 = deque(), deque()

        stack.append(root)
        flag = True

        while stack:
            temp = []
            while stack:
                node = stack.popleft()
                temp.append(node.val)
                if node.right:
                    stack2.append(node.right)
                if node.left:
                    stack2.append(node.left)
            if flag:
                temp.reverse()
            res.append(temp)
            stack, stack2 = stack2, stack
            flag = not flag
        return res