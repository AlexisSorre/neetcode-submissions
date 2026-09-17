class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c.lower() for c in s if c.isalnum()]
        n = len(cleaned)
        for i in range(n//2):
            right, left = cleaned[n-1-i], cleaned[i]
            if right != left:
                return False 
        return True 
        

        right, left = len(s)-1, 0
        while left < right:
            while left < right and not s[left].isalnum():
                left +=1
            while left < right and not s[right].isalnum():
                right -=1
            if s[left] != s[right]:
                return False 
        return True  