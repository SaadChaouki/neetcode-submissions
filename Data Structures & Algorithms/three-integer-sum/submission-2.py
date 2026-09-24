class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # We need pointers. One will start from the left, one from the right. What about the other?

        # Sorted the numbs
        sorted_nums: List[int] = sorted(nums)

        solutions = []

        for i in range(len(sorted_nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]: continue

            # Two pointers.
            overall_num = sorted_nums[i]
            j = i + 1
            k = len(sorted_nums) - 1

            while j < k:
                # Calculate the sum.
                current_sum = overall_num + sorted_nums[j] + sorted_nums[k]
                if current_sum > 0:
                    k -= 1
                elif current_sum < 0:
                    j += 1
                else:
                    solutions.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    j += 1
                    k -= 1
                    while j < k and sorted_nums[j] == sorted_nums[j - 1]:
                        j += 1

        return solutions
    


    def _stupid_solution(self, nums: List[int]) -> List[List[int]]:
        # Brute force approach.
        found = set()
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        found.add(tuple(sorted((nums[i], nums[j], nums[k]))))
        return [list(t) for t in found]

