class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # First things first, count the frequencies. This is done in 
        # O(n) time.
        frequency: dict = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # Once that's done, we need to pull the top k, should we sort?
        # Yeah we need to sort.
        sorted_frequency = [k for k, v in sorted(frequency.items(), key=lambda item: item[1], reverse=True)][:k]
        return sorted_frequency