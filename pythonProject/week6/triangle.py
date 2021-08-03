class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0] * i for i in range(1, len(triangle) + 1)]
        dp = [[0]] + dp
        #dp[i][j] 表示终点为 i j 的路径和是多少
        for i in range(1, len(triangle) + 1):
            for j in range(i):
                if j == 0:
                    dp[i][j] = triangle[i - 1][j] + dp[i - 1][j]
                elif j == i - 1:
                    dp[i][j] = triangle[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = triangle[i - 1][j] + min(dp[i - 1][j - 1], dp[i - 1][j])
        ans = 10 ** 9
        for i in range(len(dp[-1])):
            ans = min(ans, dp[-1][i])
        return ans