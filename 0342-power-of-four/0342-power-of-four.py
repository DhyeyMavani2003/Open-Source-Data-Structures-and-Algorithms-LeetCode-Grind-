class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        for i in range(16):
            if n == 4**i:
                return True
            
        return False
            