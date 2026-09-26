class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def find_pivot(nums):
            low, high = 0, len(nums) - 1

            # Keep going until don't have anymore items.
            while low < high:
                mid = (low + high) // 2
                if nums[mid] > nums[high]:
                    low = mid + 1
                else:
                    high = mid
            return low

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
    
        

        pivot = find_pivot(nums)
        n = len(nums)

        
        # Checking if the target is on the other side.
        if nums[pivot] <= target <= nums[n - 1]:
            return bs(pivot, n - 1)
        return bs(0, pivot - 1)

