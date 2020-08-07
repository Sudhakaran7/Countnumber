class Solution2:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp=[1]*(n+1)
        for i in range(1,n+1):    
            base = 9
            for digit in range(1, i):
                base = base*(10-digit)
            dp[i]=base+dp[i-1]
        return dp[-1]
 
val=Solution2()
n=int(input())
print(val.countNumbersWithUniqueDigits(n))
