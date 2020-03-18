class Solution:
    def generate(self, numRows: int):
        res = []
        for i in range(numRows):
            temp = []
            if i == 0:
                res.append([1])
                continue
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(res[i-1][j-1]+res[i-1][j])
            res.append(temp)
        return res


if __name__ == '__main__':
    temp = Solution()
    res = temp.generate(5)