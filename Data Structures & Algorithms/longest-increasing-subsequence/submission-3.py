import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp = [1] * len(nums)

        # for i in range(len(nums)-1, -1, -1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] < nums[j]:
        #             dp[i]  = max(dp[i], 1+dp[j])

        # return max(dp)
        seq = []
        for x in nums:
            i = bisect.bisect_left(seq, x)
            if i == len(seq):
                seq.append(x)
            else:
                seq[i] = x

        return len(seq)
        