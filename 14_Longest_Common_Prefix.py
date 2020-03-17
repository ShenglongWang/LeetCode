"""
@version:01.00.00
@Author:Shenglong
@solution：
首先判断字符串列表是否为0或者1,0则返回空字符串，1则返回第一个字符串。
对字符串列表进行，排序。保证最短的字符串为列表第一个。
从第一个字符串的第一个字符开始j开始，判断第i个字符串j位的字母是否等于第i+1个字符串j位的字母。
若所有字符串的第j位都相等，则将第j位字母加入返回结果；若有某个字符串的第j位不相等，结束程序。返回结果
"""

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        '''
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        strs.sort()

        res = ""

        for x, y in zip(strs[0],strs[-1]):
            if x==y:
                res+=x
            else:
                break
        return res
        '''

        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        res = ""

        strs.sort()
        for j in range(len(strs[0])):
            for i in range(len(strs) - 1):
                if strs[i][j] == strs[i + 1][j]:
                    continue
                else:
                    return res
            res += strs[i][j]
        return res



def main():
    strs = ["flower","flow","flight"]
    s = Solution()
    res = s.longestCommonPrefix(strs)
    print(res)


if __name__ == '__main__':
    main()