class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1st instinct: Can we just be greedy?
        # [1,3,4,5] & amount = 7 => 5 + 1 + 1 (try biggest first)
        
        # Next: DFS - Backtracking BRUTE FORCE
        # [1,3,4,5] & amount = 7 can choose 1,3,4,5 
        # => rem 6,4,3,2 respectively. Build a tree like this 
        # and then trace shallowest depth to be the answer
        
        # Notice:
        # Do not have to solve subproblems again
        # Can do DP Top-down approach! or Bottom up:
        # DP[0] = 0 = # coins to sum to 0
        # DP[1] = 1 = # coins to sum to 1
        # DP[2] = 1+DP[1] = # coins to sum to 2
        # DP[3] = min(1+DP[2],1+DP[0]) = # coins to sum to 3
        # ...
        # DP[7] = min(1+DP[6], 1+DP[4], 1+DP[3], 1+DP[2])
        
        # Time:   O(amount * coins)
        # Memory: O(amount)
        
        dp = [amount+1] * (amount + 1)
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for c in coins:
                if (a - c) >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        return dp[amount] if dp[amount] != (amount + 1) else -1
        
        
        