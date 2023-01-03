class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
 
        total_sum = sum(nums)
        curr_sum = sum([i*nums[i] for i in range(len(nums))])
        ans = curr_sum
        for i in range(len(nums)-1,0,-1):
            curr_sum=curr_sum + total_sum - nums[i]*(len(nums))
            ans = max(ans,curr_sum)
        return ans
