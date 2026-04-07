class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        n = len(nums) // 3

        for x in nums:
            count[x] += 1
            if len(count) <= 2:
                continue
            
            new_count = defaultdict(int)
            for num, c in count.items():
                if c > 1:
                    new_count[num] = c-1
            count = new_count

        ans = []
        for x in count:
            if nums.count(x) > n:
                ans.append(x)

        return ans
