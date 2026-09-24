class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # We have a list of numbers and for each one we need to do the multiplication
        # of all the numbers besides that index. So we need to select an index, drop it
        # then calculate the product.

        # We can just replace the item in the list with 1 and then multiply the lost.

        # Creating a list to hold the sequences.
        solutions = [1] * len(nums)

        # Keeping a running total of the multiplciations so far.
        previous_left = 1

        # Going through the list, replacing the item with 0.
        for idx in range(0, len(nums)):
            solutions[idx] *= previous_left
            previous_left = previous_left * nums[idx]

        previous_right = 1
        for idx in range(len(nums) - 1, -1, -1):
            solutions[idx] *= previous_right
            previous_right = previous_right * nums[idx]

        return solutions