class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        # What's the efficient way of travesing the sequence? Do we need
        # to keep doing it until there are no more overlapping?
        # The brute force O(n2) is to just compare everything single 
        # one with all the others cotinuously.

        # Maybe we can keep a hash map of the intervals and keep adding stuff to them?
        # What about a set? 

        # Can we take an item, create the interval if nothing overlaps with it. Store it
        # then continue? That's probably brute force tho. Letl's do it.

        # Sort the intervals first.
        intervals = sorted(intervals, key=lambda x: x[0])

        # Create a list to hold the intervals.
        merged_intervals = []

        for interval in intervals:

            # If there's no interval merged, just add
            if not merged_intervals:
                merged_intervals.append(interval)
                continue

            if self._is_overlap_interval(interval, merged_intervals[-1]):
                merged_intervals[-1] = self._merge_intervals(interval, merged_intervals[-1])

            else:
                merged_intervals.append(interval)


        # Check if they overlap.
        # If they do, take the min of the left and the max of the right
        # and create a new interval based on that.

        return merged_intervals

    @staticmethod
    def _merge_intervals(interval_a, interval_b):
        return [min(interval_a[0], interval_b[0]), max(interval_a[1], interval_b[1])]

    @staticmethod
    def _is_overlap_interval(interval_a, interval_b):
        a_left, a_right = interval_a[0], interval_a[1]
        b_left, b_right = interval_b[0], interval_b[1]
        return b_right >= a_left and b_left <= a_right