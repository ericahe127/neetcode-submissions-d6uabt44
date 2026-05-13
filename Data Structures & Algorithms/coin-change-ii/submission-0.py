class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        
        # Base case: 1 way to make amount 0
        dp[0] = 1
        
        # CRITICAL: Loop over coins FIRST to ensure combinations, not permutations
        for coin in coins:
            # We only start updating from the coin's value 
            # (you can't make amount 2 using a 3 coin)
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
                
        return dp[amount]
        