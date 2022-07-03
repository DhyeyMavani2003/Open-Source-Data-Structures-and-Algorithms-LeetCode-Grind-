class Solution:
    def trapRainWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        pq = []
        
        for i in range(m):
            visited.add((i, 0))
            heapq.heappush(pq, (grid[i][0], i, 0))
            visited.add((i, n-1))
            heapq.heappush(pq, (grid[i][n-1], i, n-1))
        
        for j in range(n):
            visited.add((0, j))
            heapq.heappush(pq, (grid[0][j], 0, j))
            visited.add((m-1, j))
            heapq.heappush(pq, (grid[m-1][j], m-1, j))
        
        
        res = 0
        while pq:
            val, x, y = heapq.heappop(pq)
            
            if x > 0 and (x-1, y) not in visited:
                visited.add((x-1, y))
                if grid[x-1][y] < val:
                    res += (val-grid[x-1][y])
                    grid[x-1][y] = val
                heapq.heappush(pq, (grid[x-1][y], x-1, y))
                
            if y > 0 and (x, y-1) not in visited:
                visited.add((x, y-1))
                if grid[x][y-1] < val:
                    res += (val-grid[x][y-1])
                    grid[x][y-1] = val
                heapq.heappush(pq, (grid[x][y-1], x, y-1))
            
            if x < m-1 and (x+1, y) not in visited:
                visited.add((x+1, y))
                if grid[x+1][y] < val:
                    res += (val-grid[x+1][y])
                    grid[x+1][y] = val
                heapq.heappush(pq, (grid[x+1][y], x+1, y))
            
            if y < n-1 and (x, y+1) not in visited:
                visited.add((x, y+1))
                if grid[x][y+1] < val:
                    res += (val-grid[x][y+1])
                    grid[x][y+1] = val
                heapq.heappush(pq, (grid[x][y+1], x, y+1))
        
        return res
    