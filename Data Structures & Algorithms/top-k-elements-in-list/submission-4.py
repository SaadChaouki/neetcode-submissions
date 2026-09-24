class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self._without_sort_solution(nums, k)

    def _without_sort_solution(self, nums: List[int], k: int) -> List[int]:

        # Creating a sequence to hold all the values.
        indices = [[] for _ in range(len(nums) + 1)]
        
        # Same counts.
        frequency: dict = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # Populating the indices with their numbers
        for num, freq in frequency.items():
            indices[freq].append(num)

        # Walking down the list.
        res = []
        for freq in range(len(indices) - 1, 0, -1):
            for num in indices[freq]:
                res.append(num)
                if len(res) == k:
                    return res


    def _sorted_solution(self, nums: List[int], k: int) -> List[int]:

        # Solution for O(n log n)
        # First things first, count the frequencies. This is done in 
        # O(n) time.
        frequency: dict = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # Once that's done, we need to pull the top k, should we sort?
        # Yeah we need to sort.
        sorted_frequency = [k for k, v in sorted(frequency.items(), key=lambda item: item[1], reverse=True)][:k]
        return sorted_frequency