class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        res = nums[0]

        for n in nums[1:]:
            candidates = (n, n * currMax, n * currMin)
            currMax = max(candidates)
            currMin = min(candidates)
            
            res = max(res, currMax)

        return res
