class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        # This is essentially just the merge interval with an extra step about finding the place to insert the 
        # new one and continue like it is.
        # The advantage here is that the list is already sorted. 
        
        # Flag to check if the new interval was merged in the data or not. Technically, we can add it to the
        # list, sort, and then treat it as a simple problem. However, that will be O(n log n). Can we do
        # it in O(n) since the array is already sorted?
        # Insert is O(n) anways, can we first insert?
        is_interval_merged = False

        if len(intervals) == 0:
            return [newInterval]

        # Adding the newInterval to the intervals
        new_intervals = []
        for interval in intervals:
            if interval[0] > newInterval[0] and is_interval_merged == False:
                new_intervals.append(newInterval)
                is_interval_merged = True
            new_intervals.append(interval)

        if is_interval_merged == False:
            new_intervals.append(newInterval)

        # Creating the lost
        merged_intervals: list = []
        for interval in new_intervals:

            # If there's no interval that was merged, just add do nothing.
            if not merged_intervals:
                merged_intervals.append(interval)
                continue

            if self.overlaps(interval, merged_intervals[-1]):
                merged_intervals[-1] = self.merge(interval, merged_intervals[-1])
            else:
                merged_intervals.append(interval)


        return merged_intervals


    @staticmethod
    def merge(interval_a, interval_b):
        return [min(interval_a[0], interval_b[0]), max(interval_a[1], interval_b[1])]

    @staticmethod
    def overlaps(interval_a, interval_b):
        a_left, a_right = interval_a[0], interval_a[1]
        b_left, b_right = interval_b[0], interval_b[1]
        return b_right >= a_left and b_left <= a_right