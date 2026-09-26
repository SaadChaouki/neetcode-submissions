class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0: 1}      # prefix sum -> times seen; 0 covers subarrays starting at index 0
        running = 0
        matches = 0

        for num in nums:
            running += num
            # an earlier prefix of (running - k) means the stretch since then sums to k
            matches += seen.get(running - k, 0)
            seen[running] = seen.get(running, 0) + 1

        return matches