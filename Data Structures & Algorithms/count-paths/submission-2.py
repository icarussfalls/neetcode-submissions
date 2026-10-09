class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # second solution from combinations
        return math.comb(m + n - 2, m - 1)