class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Ok so we have a list of [2, 20, 4, 10, 3, 4, 5]
        # We need to find the list of the numbers that we can achieve.

        # First thing is can we sort it? Set then sort would be O(n log n)
        # and is a pretty dumb way of doing it. Let's implement that.
        return self._sort_solution(nums)

    def _sort_solution(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        
        # We sort the set and remove the duplicates as we don't count for the duplicates.
        sorted_set = sorted(set(nums))

        # We need a variable to keep track of the longest sequence.
        current_sequence = 1
        longest_sequence = 1

        # For each 
        for i in range(len(sorted_set) - 1):
            if sorted_set[i] + 1 == sorted_set[i + 1]:
                current_sequence += 1
                longest_sequence = max(longest_sequence, current_sequence)
            else:
                current_sequence = 1
        return longest_sequence