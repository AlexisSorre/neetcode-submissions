#algorithme de Kadane O(n) temps, O(1) mémoire
# Idée : on parcourt la liste en gardant la somme du bloc en cours (cur)
# Si ce bloc devient négatif, il ne peut que réduire la somme de la suite donc on le jette et on recommence un nouveau bloc
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cur = 0
        for n in nums:
            cur = max(n, cur + n)   
            res = max(res, cur)     
        return res
        