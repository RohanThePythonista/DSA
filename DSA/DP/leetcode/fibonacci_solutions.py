class Solution:
    def fib(self, n: int, a=0, b=1) -> int:
        # tail recursion
        # ie. input = 5
        # 4, 1, 1
        # 3, 1, 2
        # 2, 2, 3
        # 1, 3, 5
        if n == 0:
            return a
        if n == 1:
            return b

        return self.fib(n - 1, b, a + b)

    def fib2(self, n):
        if n == 0: return 0
        if n == 1: return 1
        return self.fib2(n - 1) + self.fib2(n - 2)


"""
#memoized recursive
memo = {}
def fib(N):

	if N == 0: return 0
	if N == 1: return 1

	if N-1 not in memo: memo[N-1] = fib(N-1)
	if N-2 not in memo: memo[N-2] = fib(N-2)

	return memo[N-1] + memo[N-2]
	
iterative space optimized
def fib(N):
	if N == 0: return 0
	memo = (0,1)
	for _ in range(2,N+1):
		memo = (memo[-1], memo[-1] + memo[-2])

	return memo[-1]
	
bottom up approach
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        
        cache = [0] * (N + 1)
        cache[1] = 1
        for i in range(2, N + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[N]
 top down appraoch using memoization
 class Solution:
    cache = {0: 0, 1: 1}

    def fib(self, N: int) -> int:
        if N in self.cache:
            return self.cache[N]
        self.cache[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.cache[N]

iterative bottom up
class Solution:
    def fib(self, N: int) -> int:
        if (N <= 1):
            return N

        current = 0
        prev1 = 1
        prev2 = 0

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(2, N + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current
"""
