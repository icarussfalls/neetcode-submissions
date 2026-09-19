class Solution:
    def hammingWeight(self, n: int) -> int:
        # need to convert to binary
        # count the number of 1 bits
        count = 0
        while n != 0:
            if n % 2 != 0:
                count += 1
                n = (n - 1) / 2
            else:
                n = n / 2
        return count

