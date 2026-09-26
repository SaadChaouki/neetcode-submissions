class Solution:
    def search(self, nums, target):
        def bs(lo, hi):
            if lo > hi:                      # empty range: not found
                return -1
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return bs(mid + 1, hi)       # search right half
            return bs(lo, mid - 1)           # search left half
        return bs(0, len(nums) - 1)

            