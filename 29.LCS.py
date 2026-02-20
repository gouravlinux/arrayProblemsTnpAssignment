class Solution:
    def solve(self, i, j, m, n, ls1, ls2, dp):
        if i >= m or j >= n:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if ls1[i] == ls2[j]:
            res = self.solve(i + 1, j + 1, m, n, ls1, ls2, dp)
            return res + 1
        else:
            exclude_i = self.solve(i, j + 1, m, n, ls1, ls2, dp)
            include_i = self.solve(i + 1, j, m, n, ls1, ls2, dp)
            return max(exclude_i, include_i)

    def lcs(self, ls1, ls2):
        m = len(ls1)
        n = len(ls2)
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.solve(0, 0, m, n, ls1, ls2, dp)

if __name__ == '__main__':
    obj = Solution()
    ls1 = [1,2,3,4]
    ls2 = [3,4,1,2,1,3]
    res = obj.lcs(ls1,ls2)
    print(res)