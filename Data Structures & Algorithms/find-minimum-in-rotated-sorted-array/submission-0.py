class Solution:
    def findMin(self, nums: List[int]) -> int:
        # rotation doesnt matter here, just find min
        # so lets use binary search
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

