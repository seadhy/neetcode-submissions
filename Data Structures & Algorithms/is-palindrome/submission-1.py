class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = s.replace(' ', '').lower()
        cleaned = ''.join(x for x in cleaned if x.isalnum())
        
        return cleaned == cleaned[::-1]