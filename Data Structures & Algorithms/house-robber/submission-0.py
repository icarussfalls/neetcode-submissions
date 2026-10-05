class Solution:
    def rob(self, nums: List[int]) -> int:
        # i have already done this, but in different way
        rob1, rob2 = 0, 0

        for n in nums:
            new_rob = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = new_rob

        return rob2