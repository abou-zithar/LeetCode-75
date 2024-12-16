class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        i=0
         # Count rows
        row_count = Counter(tuple(row) for row in grid)
        
        # Extract columns and count
        column_count = Counter(tuple(grid[i][j] for i in range(n)) for j in range(n))
        
        # Count matches between rows and columns
        matches = 0
        for row, count in row_count.items():
            if row in column_count:
                matches += count * column_count[row]
        
        return matches


        
            
        