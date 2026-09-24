class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}      # char -> count inside the window
        max_freq = 0     # highest count of any single char seen in a window
        left = 0

        for right, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1
            max_freq = max(max_freq, counts[char])

            # chars to replace = window size - most common char
            if (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1

        return len(s) - left