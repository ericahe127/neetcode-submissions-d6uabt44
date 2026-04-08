class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = sum = 0
        prefixSum = {0: 1}

        for num in nums:
            sum += num
            diff = sum - k
            ans += prefixSum.get(diff, 0)
            prefixSum[sum] = 1 + prefixSum.get(sum, 0)

        return ans


        