class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]

        for key, val in freq.items():
            buckets[val].append(key)

        ans = []
        for x in buckets[n+1:]:
            for val in x:
                ans.append(val)

        return ans
    