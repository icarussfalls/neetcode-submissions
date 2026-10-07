class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        
        # base case
        n = len(s)
        dp = [0] * (n+1)
        # other base
        dp[0] = 1 # one way from starting line
        dp[1] = 1 # one way to decode the first character

        for i in range(2, n+1):
            # choice 1
            # we arrived from left branch, so one digit hop
            if s[i-1] != "0":
                dp[i] += dp[i-1]

                # choice two, did we arrive via 2 digit leap
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        return dp[n]


