class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for p in range(n + 1):
            for d in range(p + 1):
                if p < n:
                    dp[p + 1][d] += ((n - p) * dp[p][d]) % MOD
                if d < p:
                    dp[p][d + 1] += ((p - d) * dp[p][d]) % MOD
        return dp[n][n]