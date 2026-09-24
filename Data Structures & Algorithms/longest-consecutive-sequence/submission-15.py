class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Ok so we have a list of [2, 20, 4, 10, 3, 4, 5]
        # We need to find the list of the numbers that we can achieve.

        # First thing is can we sort it? Set then sort would be O(n log n)
        # and is a pretty dumb way of doing it. Let's implement that.
        return self._solve_without_sort(nums)

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

    def _solve_without_sort(self, nums: List[int]) -> int:

        # Move to a set
        nums_set = set(nums)

        if len(nums_set) <= 1:
            return len(nums_set)

        # Recording the max sequence.
        current_sequence_size = 0
        max_sequence = 1

        # Going through the numbers
        for num in nums_set:

            # Check if the number is the start of the a sequence or not.
            is_start_of_sequence = (num - 1) not in nums_set

            # If it's the start of a sequence, we keep checking for the next number
            # and counting the sequence size. 
            if is_start_of_sequence:

                # Calculating the nexwt number we'll be looking for. 
                current_sequence_size = 1
                current_num_in_sequence = num + 1

                # Keep loping until 
                while current_num_in_sequence in nums_set:
                    current_sequence_size += 1
                    current_num_in_sequence += 1

            max_sequence = max(max_sequence, current_sequence_size)

        return max_sequence