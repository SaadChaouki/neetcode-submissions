class Solution:
    def maxArea(self, heights: List[int]) -> int:
        return self._two_pointer(heights)

    def _two_pointer(self, heights: List[int]) -> int:
        
        # Pointers from the left to the right.
        left: int = 0
        right: int = len(heights) - 1

        # Setting the max area.
        max_area = float("-inf")

        # The loop.
        while left < right:
            max_area = max(max_area, self._compute_area(left, right, heights[left], heights[right]))

            if heights[left] <= heights[right]:
                left += 1

            elif heights[left] > heights[right]:
                right -= 1



        return max_area

    def _brute_force(self, heights: List[int]) -> int:
        max_area = float("-inf")
        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):
                max_area = max(max_area, (r - l) * min(heights[l], heights[r]))

        return max_area

    @staticmethod
    def _compute_area(idx_left: int, idx_right: int, height_left: int, height_right: int) -> int:
        area = (idx_right - idx_left) * min(height_left, height_right)
        return area
