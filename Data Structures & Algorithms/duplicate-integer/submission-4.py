class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen: dict = {}
        for num in nums:
            if num in seen.keys():
                return True
            seen[num] = True
        return False