#prefix sufix 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res =[0]*n
        pref =[0]*n
        suf=[0]*n

        pref[0]=suf[n-1]=1
        for i in range(1,n):
            pref[i]=pref[i-1]*nums[i-1]
        for j in range(n-2,-1,-1):
            suf[j]=nums[j+1]*suf[j+1]
        for g in range(n):
            res[g]=pref[g]*suf[g]
        return res