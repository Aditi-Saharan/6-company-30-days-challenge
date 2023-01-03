class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        nums.sort()
        n = len(nums)
        dp = [[nums[i]] for i in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i]%nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]

        return max(dp, key = len)


        
        
        
        
                
        
        
