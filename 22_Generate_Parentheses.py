"""
@version:01.00.00
@Author:Shenglong
"""
class Solution:
    def generateParenthesis(self, n: int):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()
        def valid(A):
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0
        ans = []
        generate()
        return ans




def main():
    s = Solution()
    print(s.generateParenthesis(3))


if __name__ == '__main__':
    main()