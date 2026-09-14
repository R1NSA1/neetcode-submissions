class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''
        for c in s:
            if c.isalnum():
                result += c.lower()
            else:
                continue
        return result == result[::-1]
