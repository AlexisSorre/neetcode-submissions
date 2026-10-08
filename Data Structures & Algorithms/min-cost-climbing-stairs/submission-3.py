class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1]*len(cost)

        def dfs(i):
            if i>=len(cost):
                return 0
            if memo[i]!=-1:
                return memo[i]
            memo[i]=cost[i] +min(dfs(i+1),dfs(i+2))
            return memo[i]
            
        return min(dfs(0), dfs(1))
#le memo diminue la complexite en temps car chaque dfs(i) n'est calculé qu'une fois donc la taille du mémo mais il garde cette complexite en espace 