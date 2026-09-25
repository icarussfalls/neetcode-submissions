class Solution:
    def climbStairs(self, n: int) -> int:
        # number of distinct ways, can do 1 or 2
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one

            

            
        