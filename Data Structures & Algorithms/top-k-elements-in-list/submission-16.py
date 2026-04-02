class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ans = []

        bucket = [[] for _ in range(len(nums))]
        for key, val in count.items():
            bucket[val-1].append(key)
        
        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        return ans
        