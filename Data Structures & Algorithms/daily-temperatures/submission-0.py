class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # So we have a list of temperatures. Wwe need to go through it
        # once. I think it's possible to do it only once. 

        # This sounds like it will work but we need a way to keep track of the index. 
        # Maybe we can make it a stack of a tuple and then calculate the diff?
        monotonic_stack = []

        # Creating a sequence of solutions.
        solutions = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            
            while monotonic_stack and temp > monotonic_stack[-1][1]:
                idx, covered_temp = monotonic_stack.pop()
                solutions[idx] = i - idx

            # Check if we need to drop any temperature.
            monotonic_stack.append((i, temp))

        return solutions