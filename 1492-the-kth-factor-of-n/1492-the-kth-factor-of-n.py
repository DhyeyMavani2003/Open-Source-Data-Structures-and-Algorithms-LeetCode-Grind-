class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        divisors = []
        sqrt_n = int(n**0.5)
        for x in range(1, sqrt_n + 1):
            if n % x == 0:
                k -= 1
                divisors.append(x)
                if k == 0:
                    return x
        if sqrt_n * sqrt_n == n:
            k += 1
        
        numberOfDivisors = len(divisors)
        return n // divisors[numberOfDivisors - k] if k <= numberOfDivisors else -1
        