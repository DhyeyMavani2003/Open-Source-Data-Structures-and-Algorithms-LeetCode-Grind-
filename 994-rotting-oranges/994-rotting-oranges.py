class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        queue = []
        day = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                    
        while queue:
            r, c, day = queue.pop(0)
            
            for nr, nc in [r+1, c], [r-1, c], [r, c+1], [r, c-1]:
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    queue.append((nr, nc, day + 1))
                    grid[nr][nc] = 2
                    
        for row in grid:
            if 1 in row:
                return -1
            
        return day