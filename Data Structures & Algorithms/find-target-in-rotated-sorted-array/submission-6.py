class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def find_pivot(low, high):
            if low == high:                     # one element left: that's the minimum
                return low
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                return find_pivot(mid + 1, high)   # break is to the right of mid
            return find_pivot(low, mid)            # mid could be the minimum

        # Applying the same search approach to find the index of the target.
        def bs(low: int, high: int) -> int:
            if low > high:
                return -1
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return bs(low, mid - 1)
            else:
                return bs(mid + 1, high)
    
        
        n = len(nums)
        pivot = find_pivot(0, n - 1)
    
        
        # Checking if the target is on the other side.
        if nums[pivot] <= target <= nums[n - 1]:
            return bs(pivot, n - 1)
        return bs(0, pivot - 1)

