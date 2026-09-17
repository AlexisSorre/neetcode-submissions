class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c.lower() for c in s if c.isalnum()]
        n = len(cleaned)
        for i in range(n//2):
            right , left = cleaned[n-1-i],cleaned[i]
            if right != left:
                return False  
        return True 