class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        other = len(nums) # larger n

        for i, n in enumerate(nums):
            total += n
            other += i

        return other - total