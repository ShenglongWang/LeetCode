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
    #solution1:

    def isBalanced(self, root: TreeNode, length=1) -> bool:
        if not root: return length
        left = self.isBalanced(root.left, length+1)
        if not left: return
        right = self.isBalanced(root.right, length+1)
        if not right: return
        return abs(left-right) <= 1 and max(left, right)
    '''

    '''  
    #solution2:
    
    #自下而上，递归到最后一个节点，让其value = 深度1.
    #每个节点其左右子树中最大深度n（value） + 1
    #最后递归判断每个节点的左右子树深度差小于等于1
    #时间复杂度O(N) * 2, 将value置位深度O(N), 判断子树中是否有深度差大于1的O(N)

    def storeHeight(self, root: TreeNode):
        if root == None:
            return 
        self.storeHeight(root.left)
        self.storeHeight(root.right)
        if root.left != None and root.right != None:
            root.val = 1 + max(root.left.val, root.right.val)
        elif root.left != None:
            root.val = 1 + root.left.val
        elif root.right != None:
            root.val = 1 + root.right.val
        else:
            root.val = 1
    def judge(self, root: TreeNode) -> bool:
        if root == None:
            return True
        left = 0 if root.left == None else root.left.val
        right = 0 if root.right == None else root.right.val
        #不能单纯的判断根的左节点和右节点的值，有可能出现根的左右子树深度相差为1，但左子树
        #或者右子树中存在深度差大于1的子树。需递归判断每一个节点的左右子树是不是完全平衡树。
        return abs(left - right) <= 1 and self.judge(root.left) and self.judge(root.right)

    def isBalanced(self, root: TreeNode) -> bool:
        self.storeHeight(root)
        return self.judge(root)
    '''

    # sulotion3:

    #递归获取各个节点左右子树的深度，若出现某个左右子树深度差大于1，则将深度置位-1
    #当判断节点的某个子树深度为-1，直接将节点的深度也置位-1.
    #以此类推，最后判断根节点深度是否为-1，如果为-1，则其子树中必定有深度差大于1的。
    #时间复杂度O(N)

    def dfslength(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left = self.dfslength(root.left)
        if left == -1:
            return -1
        right = self.dfslength(root.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    def isBalanced(self, root: TreeNode) -> bool:
        if self.dfslength(root) == -1:
            return False
        else:
            return True