class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = "".join(c.lower() for c in s if c.isalnum())

        for a, b in zip(s_clean, s_clean[::-1]):
            if a != b:
                return False

        return True