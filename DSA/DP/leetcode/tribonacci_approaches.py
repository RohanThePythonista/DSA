class Solution:
    def tribonacci(self, n: int) -> int:
        #         fib = [0]*41
        #         fib[0] = 0
        #         fib[1] = 1
        #         fib [2] = 1
        #         for i in range(n+1):
        #             fib[i+3] = fib[i] + fib[i+1] + fib[i+2]
        #         return fib[n]
        dp = [0, 1, 1]
        for i in range(3, n + 1):
            dp[i % 3] = sum(dp)
        return dp[n % 3]


"""
  def tribonacci(self, n):
        a, b, c = 0, 1, 1
        for _ in range(n): a, b, c = b, c, a + b + c
        return c
        
int tribonacci(int n) {
  int dp[3] = {0, 1, 1};
  for (int i = 3; i <= n; ++i)
    dp[i%3] += dp[(i+1)%3] + dp[(i+2)%3];
  return dp[n%3];
}
"""
