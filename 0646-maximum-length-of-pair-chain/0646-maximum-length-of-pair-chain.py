class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        
        sorted_pairs = sorted(pairs, key=lambda x: x[0])
        n = len(sorted_pairs)

        # dp[i] stores the length of the longest chain starting from index i
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            dp[i] = 1  # Minimum chain length is 1

            for j in range(i + 1, n):
                if sorted_pairs[i][1] < sorted_pairs[j][0]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)