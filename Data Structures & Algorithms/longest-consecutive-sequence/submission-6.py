class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        num_set = set(nums)
        streak = 0
        for x in num_set:
            if x-1 not in num_set:
                streak = 1
                while x + streak in num_set:
                    streak += 1
            ans = max(ans, streak)

        return ans

        