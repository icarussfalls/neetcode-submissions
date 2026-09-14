class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seet = set()
        for i in range(len(nums)):
            seet.add(nums[i])
        if len(nums) != len(seet):
            return True
        return False
        