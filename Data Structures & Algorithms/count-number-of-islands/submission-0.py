class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, columns = len(grid), len(grid[0])
        print(f"Processing a grid with size {rows}*{columns}.")

        # Creating a counter for the number of islands.
        counter_islands: int = 0

        # Recursive function to flood the island until nothing is found.
        def flood(r: int, c: int):

            # We reached the sea so just return. Or we reached an invalid index.
            # We can't have a negative index. We can't have an index bigger than the actual
            # size of the grid. It'll fail if that's the case.
            if r < 0 or c < 0 or r >= rows or c >= columns or grid[r][c] != '1':
                return 

            # Flood
            grid[r][c] = '0'

            # Recurse until we floor everything.
            flood(r - 1, c)
            flood(r + 1, c)
            flood(r, c - 1)
            flood(r, c + 1)

        # We go through each row and each column and check if it's the start of
        # an island. If it is, then it's recursion and flooding the island essentially.
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1':
                    # We found an island.
                    counter_islands += 1
                    flood(r, c)
        return counter_islands
        