class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a,b =0,0 #dp[i+1] #dp[i+2]
        for i in range(len(cost)-1,-1,-1):
            a, b = cost[i] +min(a, b),a 
        return min(a,b)












