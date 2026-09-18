class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        solutions = []
        complements = {}

        for i, num in enumerate(nums):
            needs = target - num
            if needs in complements:
                return [complements[needs], i]
            else:
                complements[num] = i