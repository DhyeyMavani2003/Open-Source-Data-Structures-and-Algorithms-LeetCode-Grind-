class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        n = n%14 if n%14!=0 else 14
        for _ in range(n):
            new = [0]*8
            for i in range(1,7):
                if cells[i-1]==cells[i+1]: new[i] = 1
            cells = new
        return cells