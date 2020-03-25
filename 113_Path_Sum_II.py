"""
@version:01.00.00
@Author:Shenglong
"""

'''
解题思路：
每次递归时，减去当前节点的值。
直到叶子节点时，判断叶子节点值是否等于传入的sum值
若相等，则返回 [[叶子节点value]]
不相等，返回[]

遍历完左右子树后，返回值为[[value1,value2,value3]]
将当前节点的值放在每个返回的子列表之前。
'''

class Solution:

    #So
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        if not root:
            return []

        if not root.left and not root.right:
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        left = self.pathSum(root.left)
        right = self.pathSum(root.right)

        res = [[root.val] + temp for temp in left + right]
        return re


    #Solution2:
    '''
    解题思路:
    从上向下遍历，每遍历一个节点，就将它加入temp，sum减去当前节点的值
    当遍历到叶节点，并且sum等于0 的时候，将temp数组的值加入返回数组res中。
    注：此处是要将temp数组的值加入，并不是将temp加入。
    '''

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        self.res = []

        def dfs(root, num, temp):
            if not root:
                return None
            temp.append(root.val)

            #此处做一次运算，后续遍历左右子树不在做运算，提高运行速度。
            num -= root.val
            if 0 == num and not root.left and not root.right:
                #若此处使用self.append(temp)，则父节点左右子树遍历结束后，会将父节点的值pop出temp数组。
                #一直返回到根节点，temp中的数值全部被pop掉，返回[[],[]]类似结果.
                #res.append(temp) 是将temp引用加入到res，而res.append(temp[:]),是将temp[:] 返回的值加入res
                self.res.append(temp[:])
            dfs(root.left, num, temp)
            dfs(root.right, num, temp)
            temp.pop()

        dfs(root, sum, [])
        return self.res
