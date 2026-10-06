class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob(num):
            rob1, rob2 = 0, 0
            # boundary case somewhere here
            for n in num:
                temp = max(n+rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(nums[0], rob(nums[1:]), rob(nums[:-1]))