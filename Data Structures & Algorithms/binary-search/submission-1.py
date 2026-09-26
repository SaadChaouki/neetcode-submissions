class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Remove the impossible cases first.
        # if target < nums[0] or target > nums[-1]: return -1

        # Get the middle of the array.
        # Check if the number is in the right or left side.
        # Go to that side.
        # Repeat

        def bs(subset: List[int], shift = 0):
            
            if len(subset) == 1:
                if target == subset[0]:
                    return shift
                else:
                    return -1
            if len(subset) == 0:
                return -1

            # Splitting the array.
            split_idx = len(subset) // 2
            left, right = subset[:split_idx], subset[split_idx:]

            # Checking if we need to go left or right.
            if target >= right[0]:
                return bs(right, shift + split_idx)
            else:
                return bs(left, shift + 0)

        return bs(nums)

            