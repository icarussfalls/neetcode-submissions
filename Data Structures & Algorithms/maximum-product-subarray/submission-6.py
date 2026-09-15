class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        currMin = 1
        currMax = 1
        for n in nums:
            if n == 0:
                currMin = 1
                currMax = 1
                continue
            tmp = currMax * n
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(tmp, n * currMin, n)
            res = max(res, currMax, currMin)
        return res
