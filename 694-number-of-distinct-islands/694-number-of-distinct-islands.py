class Solution:
    def numDistinctIslands(self, grid):
        
        islands = set()  
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                island = []
                front = [(i,j)]
                
                while front:
                    nxt = []
                    for x,y in front:
                        if 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] == 1:
                            grid[x][y] = 0
                            island.append((x-i,y-j))  # minus the current (i,j) in the big for loop 
                            for m,n in (x+1, y), (x-1,y), (x, y+1), (x, y-1):
                                nxt.append((m,n))
                    front = nxt 
                
                if island and str(island) not in islands:
                    islands.add(str(island))
                    
        return len(islands)
    
    # Similar to LC 200 Number of Islands
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(start, shape, i, j):
            if i>=0 and j>=0 and i<len(grid) and j<len(grid[0]) and grid[i][j] == 1:
                shape.append((i-start[0], j-start[1])) # track shape using starting coords
                grid[i][j] = 0 # make sure we don't visit again
                dfs(start,shape,i+1,j)
                dfs(start,shape,i-1,j)
                dfs(start,shape,i,j+1)
                dfs(start,shape,i,j-1)
            return shape

        unique_islands, islands = set(), 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island = tuple(dfs((i,j), [], i, j)) # shape of island we just visited
                    if island not in unique_islands:
                        unique_islands.add(island)
                        islands += 1
        return islands
    
    
    