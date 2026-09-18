class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = "".join(c.lower() for c in s if c.isalnum())

        for i in range((len(s_clean) // 2)):
            if s_clean[i] != s_clean[len(s_clean) - (i + 1)]:
                return False

        return True