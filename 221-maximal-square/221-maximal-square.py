class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}
        
        # T: O(mn) and M: O(mn)
        def helper(r, c):
            if r >= ROWS or c >= COLS:
                return 0
            if (r,c) not in cache:
                down = helper(r+1,c)
                right = helper(r,c+1)
                diagonal = helper(r+1,c+1)
                
                cache[(r,c)] = 0
                if matrix[r][c] == "1":
                    cache[(r,c)] = 1 + min(down, right, diagonal)
            return cache[(r,c)]
        
        helper(0,0)
        return max(cache.values())**2