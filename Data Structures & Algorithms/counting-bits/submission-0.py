class Solution:
    def countBits(self, n: int) -> List[int]:
        def return_binary_count(n):
            count = 0
            while n != 0:
                res = n % 2
                if res != 0:
                    n = (n - 1) / 2
                    count += 1
                else:
                    n = n/2
            return count

        out = []
        for i in range(0, n+1):
            out.append(return_binary_count(i))
 
        return out
