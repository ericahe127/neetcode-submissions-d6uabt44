class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (n * 2)
        ans[:n] = nums[:]
        ans[n: 2*n] = nums[:]
        return ans