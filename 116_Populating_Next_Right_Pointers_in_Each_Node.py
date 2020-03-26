"""
@version:01.00.00
@Author:Shenglong
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""



class Solution:
    '''
    Solution1:
    使用栈来进行层次遍历
    当遍历栈stack不为空时，当前节点的next为stack[0]
    若为空时，表示当前层遍历结束。
    '''

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        stack, stack1 = [], []
        stack.append(root)
        while (stack):
            while (stack):
                temp = stack.pop(0)
                if stack:
                    temp.next = stack[0]
                else:
                    temp.next = None
                if temp.left:
                    stack1.append(temp.left)
                if temp.right:
                    stack1.append(temp.right)
            stack, stack1 = stack1, stack
        return root



    '''
    Solution2：
    遍历当前层时，将下一层的next处理。
    '''
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root
        current = root
        next = root.left
        while current.left:
            current.left.next = current.right
            if current.next:
                current.right.next = current.next.left
                current = current.next
            else:
                current = next
                next = current.left
        return root

